# app.py — Chat with a YouTube Video (robust captions + local transcription fallback)
# Requires: streamlit, python-dotenv, langchain, langchain-openai, langchain-community,
#           langchain-text-splitters, faiss-cpu, youtube-transcript-api, yt-dlp,
#           faster-whisper, ctranslate2, tiktoken, ffmpeg (system)

import os
import shutil
import tempfile
from pathlib import Path
from typing import List, Tuple, Optional

import streamlit as st
from dotenv import load_dotenv

# Load env (.env) before SDKs
load_dotenv()

# LangChain stack
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# YouTube transcripts
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    CouldNotRetrieveTranscript,
)

st.set_page_config(page_title="Chat with a YouTube Video", page_icon="🎬", layout="wide")


# ---------------------------
# Util / Core functions
# ---------------------------

def require_openai_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        st.sidebar.error("Set OPENAI_API_KEY as an environment variable or in a .env file.")
        st.stop()
    return key


def try_fetch_transcript_api(
    video_id: str,
    preferred_languages: Tuple[str, ...] = ("en",),
    accept_any_language: bool = True,
    target_language_for_translation: Optional[str] = "en",
) -> Optional[List[dict]]:
    """
    Robust transcript fetch workflow:
    1) manual (preferred languages)
    2) auto-generated (preferred languages)
    3) translate ANY transcript to target_language (if possible)
    4) first available transcript (any language)
    Returns list of {'text','start','duration'} or None.
    """
    # Newer API shape
    if hasattr(YouTubeTranscriptApi, "list_transcripts"):
        try:
            tl = YouTubeTranscriptApi.list_transcripts(video_id)

            # 1) Manual in preferred languages
            if preferred_languages:
                try:
                    t = tl.find_manually_created_transcript(list(preferred_languages))
                    return t.fetch()
                except Exception:
                    pass

            # 2) Auto-generated in preferred languages
            if preferred_languages:
                try:
                    t = tl.find_generated_transcript(list(preferred_languages))
                    return t.fetch()
                except Exception:
                    pass

            # 3) Translate any transcript to target language
            if target_language_for_translation:
                for t in tl:
                    try:
                        if getattr(t, "is_translatable", False):
                            return t.translate(target_language_for_translation).fetch()
                    except Exception:
                        continue

            # 4) First available (any language)
            if accept_any_language:
                for t in tl:
                    try:
                        return t.fetch()
                    except Exception:
                        continue

            return None

        except (TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript):
            return None
        except Exception:
            return None

    # Older API shape
    if hasattr(YouTubeTranscriptApi, "get_transcript"):
        # Try preferred languages
        try:
            if preferred_languages:
                return YouTubeTranscriptApi.get_transcript(video_id, languages=list(preferred_languages))
        except Exception:
            pass
        # Try without specifying language (any available)
        try:
            return YouTubeTranscriptApi.get_transcript(video_id)
        except Exception:
            return None

    return None


def fallback_transcribe_with_whisper(video_id: str, model_size: str = "small.en") -> Optional[str]:
    """
    Download audio (yt-dlp) → transcribe (Faster-Whisper).
    Returns raw transcript string or None.
    """
    try:
        import yt_dlp
    except Exception as e:
        raise RuntimeError("yt-dlp not installed. `pip install yt-dlp`") from e
    try:
        from faster_whisper import WhisperModel
    except Exception as e:
        raise RuntimeError("faster-whisper not installed. `pip install faster-whisper ctranslate2`") from e

    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found. On macOS: `brew install ffmpeg`")

    tmpdir = Path(tempfile.mkdtemp(prefix="yt_audio_"))
    audio_path = tmpdir / f"{video_id}.m4a"
    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        "format": 'bestaudio[ext=m4a]/bestaudio/best',
        "outtmpl": str(audio_path),
        "quiet": True,
        "noprogress": True,
        "concurrent_fragment_downloads": 4,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        shutil.rmtree(tmpdir, ignore_errors=True)
        raise RuntimeError(f"Audio download failed: {e}") from e

    try:
        model = WhisperModel(model_size, compute_type="int8")  # fast on CPU
        segments, info = model.transcribe(str(audio_path), language="en", vad_filter=True)
        parts = [s.text.strip() for s in segments if s.text]
        text = " ".join(parts).strip()
        return text or None
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def make_vectorstore(transcript_text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents([transcript_text])
    if not docs:
        raise RuntimeError("No chunks produced from transcript text.")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vs = FAISS.from_documents(docs, embeddings)
    retriever = vs.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    return vs, retriever, docs


def answer_question(retriever, question: str):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    prompt = PromptTemplate(
        template=(
            "You are a helpful assistant.\n"
            "Answer ONLY from the provided transcript context.\n"
            "If the context is insufficient, say you don't know.\n\n"
            "{context}\n"
            "Question: {question}"
        ),
        input_variables=["context", "question"],
    )
    docs = retriever.invoke(question) or []
    snippets = [d.page_content for d in docs]
    context_text = "\n\n".join(snippets)
    final_prompt = prompt.invoke({"context": context_text, "question": question})
    resp = llm.invoke(final_prompt.to_string())
    return resp.content.strip(), snippets


@st.cache_resource(show_spinner=False)
def build_store_for_video(
    video_id: str,
    preferred_langs: Tuple[str, ...],
    accept_any: bool,
    translate_to: Optional[str],
    use_fallback: bool,
    whisper_model: str,
):
    """
    Returns (vector_store, retriever, transcript_text, n_chunks, error_reason)
    """
    error_reason = None
    transcript_text = None

    # 1) Captions
    try:
        with st.status("Fetching captions…", expanded=False):
            captions = try_fetch_transcript_api(
                video_id,
                preferred_languages=preferred_langs,
                accept_any_language=accept_any,
                target_language_for_translation=translate_to if translate_to else None,
            )
            if captions:
                transcript_text = " ".join((c.get("text") or "").strip() for c in captions if c.get("text")).strip()
    except Exception as e:
        error_reason = f"Caption fetch error: {type(e).__name__}: {e}"

    # 2) Fallback
    if not transcript_text:
        if use_fallback:
            try:
                with st.status("Captions missing. Downloading audio & transcribing (Faster-Whisper)…", expanded=False):
                    text = fallback_transcribe_with_whisper(video_id, model_size=whisper_model)
                    if text:
                        transcript_text = text
                    else:
                        error_reason = (error_reason or "") + " | Fallback transcription returned empty text."
            except Exception as e:
                error_reason = (error_reason or "") + f" | Fallback error: {type(e).__name__}: {e}"
        else:
            error_reason = (error_reason or "") + " | Captions not available and fallback is disabled."

    if not transcript_text:
        return None, None, None, 0, (error_reason or "Unknown transcript failure")

    # 3) Vector store
    try:
        with st.status("Building vector store (split → embed → index)…", expanded=False):
            vs, retriever, docs = make_vectorstore(transcript_text)
            return vs, retriever, transcript_text, len(docs), None
    except Exception as e:
        return None, None, None, 0, f"Vector store error: {type(e).__name__}: {e}"


# ---------------------------
# UI
# ---------------------------

st.title("🎬 Chat with a YouTube Video")
st.caption("Enter a YouTube **Video ID** (the part after `v=`). I’ll fetch captions or transcribe the audio, then you can ask questions.")

with st.sidebar:
    st.subheader("Settings")
    require_openai_key()

    # Transcript preferences
    pref_lang_str = st.text_input("Preferred language codes (comma-separated)", value="en")
    preferred_langs = tuple([s.strip() for s in pref_lang_str.split(",") if s.strip()]) or ("en",)
    accept_any = st.toggle("Accept any language if preferred not found", value=True)
    translate_to = st.text_input("Translate transcript to (leave empty to skip)", value="en")

    st.markdown("---")
    use_fallback = st.toggle(
        "Fallback to local transcription when captions are missing (yt-dlp + Faster-Whisper)",
        value=True,
        help="Requires ffmpeg, yt-dlp, faster-whisper.",
    )
    whisper_model = st.selectbox("Faster-Whisper model", ["tiny.en", "base.en", "small.en", "medium.en"], index=2)
    st.markdown("**macOS tip:** `brew install ffmpeg` for fallback.")

# Input row
col1, col2 = st.columns([2, 1], vertical_alignment="bottom")
with col1:
    video_id = st.text_input("YouTube Video ID", placeholder="e.g., Gfr50f6ZBvo", label_visibility="visible")
with col2:
    go = st.button("Process Video", type="primary", use_container_width=True)

if go:
    if not video_id.strip():
        st.error("Please enter a Video ID.")
        st.stop()

    with st.spinner("Preparing…"):
        vs, retriever, transcript_text, n_chunks, err = build_store_for_video(
            video_id.strip(),
            preferred_langs,
            accept_any,
            translate_to if translate_to.strip() else None,
            use_fallback,
            whisper_model,
        )

    if err:
        st.error(f"Could not build a knowledge base.\n\n**Details:** {err}")
        st.info("Tips: check video region/age restrictions, enable fallback, ensure ffmpeg is installed, or try a different video.")
        st.stop()

    st.session_state["retriever"] = retriever
    st.session_state["video_id"] = video_id.strip()
    st.session_state["n_chunks"] = n_chunks
    st.session_state["transcript_preview"] = (transcript_text[:800] + "…") if len(transcript_text) > 800 else transcript_text

if "retriever" in st.session_state:
    with st.expander("Transcript preview", expanded=False):
        st.write(st.session_state["transcript_preview"])
    st.success(f"Vector store ready • chunks: {st.session_state['n_chunks']} • video: {st.session_state['video_id']}")

    st.markdown("### Chat")
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for role, content in st.session_state["messages"]:
        with st.chat_message(role):
            st.markdown(content)

    user_q = st.chat_input("Ask about the video…")
    if user_q:
        st.session_state["messages"].append(("user", user_q))
        with st.chat_message("user"):
            st.markdown(user_q)

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                try:
                    answer, snippets = answer_question(st.session_state["retriever"], user_q)
                except Exception as e:
                    st.error(f"Error while answering: {e}")
                    st.stop()

                st.markdown(answer)
                with st.expander("Show supporting snippets", expanded=False):
                    for i, snip in enumerate(snippets, 1):
                        st.markdown(f"**Snippet {i}**\n\n{snip}")

        st.session_state["messages"].append(("assistant", answer))