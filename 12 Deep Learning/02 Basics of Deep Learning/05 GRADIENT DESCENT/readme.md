# GRADIENT DESCENT — ONE-FILE, SIMPLE GUIDE

Goal
----
We want to **minimize a loss** (also called an objective) J(θ) by moving the model parameters θ a little bit **downhill** along the negative gradient:
θ ← θ − η · ∇θ J(θ)
Here, **∇θ J(θ)** is the gradient (the direction of steepest increase), and **η** (eta) is the **learning rate** (the step size). Think of standing on a hill and taking steps downhill until you reach a valley. 

Key ideas (in plain words)
--------------------------
1) **Parameters (θ)**: the numbers inside your model (weights, biases).  
2) **Loss J(θ)**: a single score that says “how wrong” the model is; smaller is better.  
3) **Gradient ∇θ J(θ)**: tells you which way J(θ) increases the fastest.  
4) **Update rule**: step **against** the gradient so the loss goes down.  
5) **Learning rate (η)**: too big → jump around or diverge; too small → very slow.

Where gradient descent fits
---------------------------
- **Backpropagation** computes the gradients efficiently (using the chain rule).
- **Gradient descent** uses those gradients to update θ with the rule above.

Three variants (same idea, different amount of data per step)
-------------------------------------------------------------
A) **Batch Gradient Descent (BGD)**  
   • Uses **all training examples** to compute one gradient, then does **one update**.  
   • Very **stable** (smooth loss curve), but each step can be **slow** and **needs more memory**.  
   • Updates per epoch = **1** (i.e., one update after processing the whole dataset).

B) **Stochastic Gradient Descent (SGD)**  
   • Uses **one example at a time** to compute the gradient and update immediately.  
   • **Very fast cheap steps**, but **noisy**; the loss jumps up and down (can help escape local minima).  
   • Updates per epoch = **number of examples** (many small updates).

C) **Mini-Batch Gradient Descent (MBGD)**  
   • Uses a **small batch** (e.g., 32/64/128 samples) per update.  
   • **Best of both worlds**: faster than full batch, more stable than pure SGD, fits on GPU/CPU memory.  
   • Typical choice in practice.  
   • Batch sizes are often powers of two (32, 64, 128, …) for efficient memory use.

Simple pseudocode (vectorized where possible)
---------------------------------------------
Let X be inputs, y be targets, θ be parameters, η be learning rate, B be batch size.

Common loop pieces (do this each epoch):
1) **Shuffle** the data (important for SGD/mini-batch).  
2) Split into batches of size B (for mini-batch), or B = N for full batch, or B = 1 for SGD.  
3) For each batch (X_b, y_b):  
   a) Compute predictions ŷ_b = model(X_b, θ)  
   b) Compute loss L_b = J(θ; X_b, y_b)  
   c) Compute gradients g = ∇θ J(θ; X_b, y_b)  ← backprop does this  
   d) Update θ ← θ − η · g

Notes:  
- If the dataset size **N** is not divisible by **B**, the **last batch** is smaller; that’s fine.  
- **Vectorize** operations (use matrix multiplies) to avoid slow Python loops.

How to choose between the three
-------------------------------
- **Speed per update**: SGD > Mini-Batch > Batch  
- **Stability of loss**: Batch > Mini-Batch > SGD  
- **Wall-clock to a good solution** (typical): Mini-Batch is the sweet spot.  
- **Very large datasets**: prefer Mini-Batch/SGD (Batch may not fit in memory).  
- **Small datasets**: Batch can be okay and very stable.

What to log and watch
---------------------
- **Training loss** per batch (or moving average for SGD).  
- **Validation loss** per epoch (to detect overfitting).  
- **Learning rate behavior** (try decay schedules if plateaus).  
- **Gradient norms** (very large → lower η; very small → increase η or try normalization).

Learning rate (η) tips
----------------------
- Start with a small value (e.g., 0.1, 0.01, or 0.001 depending on model/scale).  
- If loss **explodes**, lower η; if loss **barely decreases**, raise η a bit.  
- Use **schedules**: step decay, cosine decay, or **warmup then decay**.  
- Consider **momentum/Adam** later, but first understand plain gradient descent.

Preprocessing helps convergence
-------------------------------
- **Standardize/normalize inputs** (mean 0, std 1 or to [0,1]) for smoother training.  
- **Shuffle** each epoch (especially for SGD/mini-batch).  
- **Initialize** weights sensibly (e.g., He/Glorot for deep nets).

Intuition for trajectories
--------------------------
- **Batch GD**: smooth downhill path to a basin (few updates, steady curve).  
- **SGD**: jittery path (noisy), can **jump out of shallow local minima**; may hover instead of settling exactly.  
- **Mini-batch**: moderate noise → usually **fast and reliable**.

Two tiny worked examples (formulas you can use by hand)
-------------------------------------------------------

1) **Linear regression with MSE**  
   Model: ŷ = w·x + b (scalar case for simplicity)  
   Loss (per example): ℓ = ½(ŷ − y)²  
   For a batch of size B: L = (1/B) Σ ½(ŷ_i − y_i)²  
   Gradients:
   ∂L/∂w = (1/B) Σ (ŷ_i − y_i) x_i  
   ∂L/∂b = (1/B) Σ (ŷ_i − y_i)  
   Update:
   w ← w − η · ∂L/∂w  
   b ← b − η · ∂L/∂b

2) **Logistic regression with binary cross-entropy**  
   Model: z = w·x + b,  ŷ = σ(z) = 1/(1+e^(−z))  
   Loss (per example): ℓ = −[ y·log(ŷ) + (1−y)·log(1−ŷ) ]  
   For a batch of size B: L = (1/B) Σ ℓ_i  
   Useful identity: ∂ℓ/∂z = (ŷ − y)  
   Gradients:
   ∂L/∂w = (1/B) Σ (ŷ_i − y_i) x_i  
   ∂L/∂b = (1/B) Σ (ŷ_i − y_i)  
   Update is the same pattern as above.

Batch vs. SGD vs. Mini-batch — quick compare
--------------------------------------------
- **Updates per epoch**:  
  • Batch: 1  
  • SGD: N (every single sample)  
  • Mini-batch: N/B  
- **Compute/time per update**:  
  • Batch: heavy  
  • SGD: very light  
  • Mini-batch: moderate  
- **Memory**:  
  • Batch: highest (process all examples)  
  • SGD: lowest (one example)  
  • Mini-batch: controllable by B  
- **Loss curve**:  
  • Batch: smooth  
  • SGD: noisy  
  • Mini-batch: mildly noisy  
- **Escaping local minima**:  
  • Batch: harder  
  • SGD: easiest (noise helps)  
  • Mini-batch: in-between

Common pitfalls (and fixes)
---------------------------
- **Diverging loss**: η too large → reduce η; check for bad data/NaNs.  
- **Stagnation**: η too small → increase η; normalize inputs; try a schedule.  
- **Overfitting**: training loss ↓, validation loss ↑ → regularize, use early stopping, more data/augment.  
- **Unbalanced classes** (classification): use proper metrics, class weights, or sampling.  
- **Batch size too big**: can hurt generalization (try smaller B).  
- **No shuffling**: leads to biased updates; always shuffle each epoch.

Practical defaults (just to start)
----------------------------------
- **Mini-batch size**: 32, 64, or 128 (use what fits memory; powers of two are efficient).  
- **Learning rate**: start with 0.01 for simple models; 0.001 for deeper nets; adjust based on loss behavior.  
- **Epochs**: monitor validation loss; stop when it plateaus (early stopping with patience).  
- **Shuffling**: True every epoch.

Why the last batch can be smaller
---------------------------------
If N is not divisible by B, the final mini-batch just has **N mod B** samples. This is normal and supported by all frameworks.

Vectorization note
------------------
Matrix multiply lets you compute all predictions in a batch at once (fast/optimized). This is why **batch/mini-batch** training can be much faster than naive per-sample loops in high-level languages.

Summary (one line)
------------------
Use **θ ← θ − η · ∇θ J(θ)**; prefer **mini-batch** training with shuffling, sensible η, and normalized inputs; watch your losses and adjust.