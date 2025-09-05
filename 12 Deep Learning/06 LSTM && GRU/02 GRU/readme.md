# GRU (Gated Recurrent Unit) — the quick, smart RNN

**Idea in one line:** GRU is a lighter, faster cousin of LSTM that learns long- and short-term patterns in sequences using just two gates—update and reset.

⸻

## Why GRU?
• Fewer parts than LSTM → fewer parameters → faster training. In many tasks GRUs perform on par with LSTMs, while being simpler to tune. Use them when you want strong sequence modeling without the extra bulk.  
• Keeps context over time (solves classic RNN’s vanishing/exploding-gradient troubles) but with a cleaner design.  

⸻

## The moving pieces (plain words)
• Input at time t: x_t (e.g., current word vector).  
• Previous memory: h_{t-1} (what the model remembers so far).  
• Gates:  
  – Reset gate r_t – “How much of the old memory should I look at right now?”  
  – Update gate z_t – “How much of the new proposal should replace the old memory?”  
• Candidate memory: h̃_t – a proposal for the new memory after peeking at x_t and a reset version of h_{t-1}.  
• New memory: h_t – the final, blended memory for this step.  

All these are vectors of the same size (except x_t, whose size depends on your features). Keep this in mind when wiring shapes in code.  

⸻

## How GRU updates memory (step-by-step)
1) Reset what’s not needed:  
r_t = σ(W_r·[h_{t-1}, x_t])  
→ choose which parts of old memory to consult. Think: “glance back selectively.”  

2) Propose the new memory:  
h̃_t = tanh(W_h·[(r_t ⊙ h_{t-1}), x_t])  
→ mix current input with the reset old memory to draft a candidate.  

3) Decide how much to keep vs. replace:  
z_t = σ(W_z·[h_{t-1}, x_t])  
→ 0 = “keep old,” 1 = “use new.”  

4) Blend to get the final memory:  
h_t = (1 − z_t) ⊙ h_{t-1} + z_t ⊙ h̃_t  
→ a smooth switch between past and proposal.  

σ = sigmoid, ⊙ = element-wise multiply, [·,·] = concatenation.

⸻

## A sticky story to remember it
• Reset = “What past should I consult?” (skim the diary)  
• Candidate = “Here’s my new guess.”  
• Update = “How much do I overwrite?”  
• Final memory = “Old + New, mixed smartly.”  

This “skim → draft → overwrite” loop repeats for every time step in your sequence.  

⸻

## When to pick GRU vs LSTM
• Pick GRU when you want speed and simplicity with strong performance on many NLP/sequence tasks.  
• Pick LSTM if your problem really benefits from the extra control of separate long/short memories (some datasets do). Best practice: try both, keep the winner.  

⸻

## Minimal Keras sketch (for intuition)
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import GRU, Dense, Embedding  

model = Sequential([  
    Embedding(input_dim=vocab_size, output_dim=128, input_length=max_len),  
    GRU(64, return_sequences=False),   # 64 = hidden size (h_t dimension)  
    Dense(1, activation='sigmoid')     # e.g., sentiment (0/1)  
])  
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  

Hidden size (64) is the size of h_t, r_t, z_t, and h̃_t. Adjust it for capacity/speed trade-off.  


##
GRU = RNN with two knobs (reset & update) that learn when to remember, when to forget, and how much to rewrite—fast, simple, and usually very competitive.