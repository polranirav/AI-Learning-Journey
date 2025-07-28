
# ⚡ 3 – Redis for LLM Caching (Speed Up Repeated Prompts)

Calling large language models (LLMs) like GPT, Claude, or Gemini can be **expensive and slow**. Redis is the perfect tool to **cache previously computed outputs**.

---

## 🧩 Project Scenario

You have a web app or chatbot that frequently gets **repetitive prompts** like:
> “Explain transformers in simple terms.”

Instead of paying for every request, cache results using Redis.

---

## ⚙️ Tech Stack

| Component        | Tool              |
|------------------|-------------------|
| Cache Layer      | Redis             |
| LLM API          | OpenAI / Claude   |
| Language         | Python            |
| Library          | redis-py          |

---

## 🛠️ 1. Setup Redis

### Install Redis locally:

```bash
brew install redis      # macOS
sudo apt install redis  # Ubuntu
```

### Install Redis client:

```bash
pip install redis openai
```

---

## 🔌 2. Connect to Redis

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
```

---

## 💡 3. LLM Call with Redis Cache

```python
import openai

def ask_llm(prompt: str) -> str:
    # Check cache first
    cached = r.get(prompt)
    if cached:
        print("✅ Cache hit")
        return cached.decode()

    # Else, call LLM
    print("❌ Cache miss")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content

    # Cache it for 1 hour
    r.setex(prompt, 3600, answer)
    return answer
```

---

## 🧪 Test It

```python
print(ask_llm("Explain Transformers in 1 sentence."))
print(ask_llm("Explain Transformers in 1 sentence."))  # Second call will hit cache
```

---

## 📦 Redis Key Structure (Best Practice)

| Key Example                             | Value Type     | Purpose                      |
|-----------------------------------------|----------------|------------------------------|
| `prompt:Explain Transformers`           | string         | Store response               |
| `chat:user123:session456`               | JSON           | Conversation memory          |
| `usage:user42:count`                    | counter        | Rate limiting / billing      |
| `model:gpt-4:config`                    | JSON/dict      | Track model config/version   |

---

## 🚀 Advanced: JSON Hash Cache

```python
prompt_key = "cache:gpt:prompt"
r.hset(prompt_key, prompt, answer)
r.expire(prompt_key, 3600)
```

---

## 📁 Project Layout

```
redis-llm-cache/
├── cache.py         # Redis connection logic
├── llm_cache.py     # Main logic to check/store LLM calls
├── test.py          # Run tests
├── requirements.txt
```

---

## 💼 Real-World Use Cases

| Use Case                     | Redis Feature   |
|------------------------------|-----------------|
| LLM response reuse           | String TTL keys |
| Prevent repeated prompts     | Hash keys       |
| Prompt deduplication         | Set with TTL    |
| App state tracking           | JSON / key tree |

---

## ✅ Production Tips

- Use `setex()` instead of `set()` to auto-expire cache
- Normalize prompts (strip, lowercase) before caching
- Use `redis-py` connection pool for speed
- Monitor Redis memory and TTL hit ratio

---

📁 **Next File:** [`4_streaming_user_logs_redis.md`](./4_streaming_user_logs_redis.md)
