# 01 — What is Deep Learning? (and how it works)

A practical, memory-friendly summary. Keep this as your first note in the Deep Learning track.

---

## Table of contents
- [What is Deep Learning?](#what-is-deep-learning)
- [Where DL fits (AI → ML → DL)](#where-dl-fits-ai--ml--dl)
- [Neural networks: the mental model](#neural-networks-the-mental-model)
- [How learning happens (training loop)](#how-learning-happens-training-loop)
- [Deep Learning vs Machine Learning (quick compare)](#deep-learning-vs-machine-learning-quick-compare)
- [Why Deep Learning is popular now](#why-deep-learning-is-popular-now)
- [Where DL is used (common applications)](#where-dl-is-used-common-applications)
- [Mini PyTorch pattern (copy-paste starter)](#mini-pytorch-pattern-copypaste-starter)
- [Sanity checks & pitfalls](#sanity-checks--pitfalls)
- [Good defaults & tuning tips](#good-defaults--tuning-tips)
- [Glossary (short definitions)](#glossary-short-definitions)
- [Quick start checklist](#quick-start-checklist)

---

## What is Deep Learning?
**Simple:** A way to map inputs → outputs using **neural networks with many layers** that learn features directly from data.

**Technical:** A subfield of ML that uses **artificial neural networks** and **representation learning**—stacked layers automatically extract higher-level features from raw inputs (pixels, audio samples, tokens, etc.).

**Why it matters (representation learning):**
- Classic ML relies on **manual feature engineering**.
- DL learns features **for you**: early layers find simple patterns (edges/tones), deeper layers compose them into complex concepts (shapes/objects/semantics).

---

## Where DL fits (AI → ML → DL)
- **AI**: any technique that makes machines “smart”.
- **Machine Learning (ML)**: learns patterns from data (inputs → outputs).
- **Deep Learning (DL)**: ML using **multi-layer neural networks** that also **discover representations** automatically.

---

## Neural networks: the mental model
- **Perceptron / neuron**: takes inputs, computes a weighted sum (+ bias), then applies a **nonlinear activation**.
- **Weights**: learned parameters that connect neurons.
- **Layers**:
  - **Input**: raw features (or embeddings).
  - **Hidden**: transform/compose features (simple → complex).
  - **Output**: task predictions (class scores, regression values).

**Minimal math (forward pass):**  
For one layer, \( y = f(Wx + b) \)  
where \(x\) is input, \(W\) weights, \(b\) bias, and \(f\) a nonlinearity (ReLU, GELU, etc.). Stacking layers composes functions into richer decision boundaries.

---

## How learning happens (training loop)
1. **Forward pass**: run input through layers to get predictions \(\hat{y}\).
2. **Loss**: measure error vs. target \(y\) (e.g., Cross-Entropy for classification, MSE for regression).
3. **Backpropagation (autograd)**: compute gradients of loss w.r.t. every parameter via chain rule.
4. **Optimizer step**: update parameters (SGD/Adam) to reduce loss.
5. **Repeat** for many batches/epochs; monitor validation set to avoid overfitting.

---

## Deep Learning vs Machine Learning (quick compare)

| Axis | Machine Learning | Deep Learning |
|---|---|---|
| **Data need** | small → medium | **data-hungry**, improves with scale |
| **Hardware** | CPU often fine | **GPU/TPU** preferred |
| **Training time** | usually shorter | often **long** |
| **Prediction time** | varies | can be **fast** after training |
| **Features** | **manual** feature engineering | **automatic** (representation learning) |
| **Interpretability** | easier to explain | typically a **black box** |

**Rule of thumb:** prefer classic ML when data is limited + interpretability is important; use DL when you have enough data/compute and need SOTA performance.

---

## Why Deep Learning is popular now
- **Data**: large labeled datasets (vision, text, speech) are widely available.
- **Compute**: **GPUs/TPUs** accelerate matrix operations central to neural nets.
- **Frameworks**: **PyTorch** and **TensorFlow/Keras** simplify building/training.
- **Architectures & transfer learning**: reusable backbones (ResNet, U-Net, YOLO, Transformers) + fine-tuning enable great results with modest data.
- **Community & tooling**: open models, code, tutorials, deployment tools.

---

## Where DL is used (common applications)
- **Vision**: classification, detection, segmentation, self-driving perception.
- **NLP/Speech**: translation, Q&A, summarization, ASR/TTS.
- **Other**: medical imaging, drug discovery, recommender systems, robotics, games.

---

## Mini PyTorch pattern (copy-paste starter)

> A tiny, general skeleton you can adapt. Comments explain **why**, not just **what**.

```python
# Tiny classifier/regressor in PyTorch
# Replace ... with your shapes/dataset.
import torch
import torch.nn as nn

# 1) Define a small model
class TinyNet(nn.Module):
    def __init__(self, in_dim, hidden, out_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),              # nonlinearity → curved decision boundaries
            nn.Linear(hidden, out_dim)
        )
    def forward(self, x):
        return self.net(x)

# 2) Instantiate model/optimizer/loss
model = TinyNet(in_dim=..., hidden=64, out_dim=...)     # start simple
opt = torch.optim.Adam(model.parameters(), lr=1e-3)     # safe default
# For classification, use CrossEntropyLoss; for regression, use MSELoss
loss_fn = nn.CrossEntropyLoss()

# 3) Training loop (mini)
# Assume you have: for x, y in dataloader (x: [B, in_dim], y: labels)
for x, y in dataloader:
    opt.zero_grad()               # reset grads
    logits = model(x)             # forward pass
    loss = loss_fn(logits, y)     # compute loss
    loss.backward()               # autograd → gradients via backprop
    opt.step()                    # update params
```

---

## Sanity checks & pitfalls
- **Overfit a tiny batch** (e.g., 100 samples) to near-zero loss → verifies your model & training loop are wired correctly.
- **Monitor validation**: if val loss rises while train loss falls → overfitting (add dropout/weight decay/data aug/early stopping).
- **Learning rate**: too high → divergence; too low → very slow. Tune by ×/÷ 3.
- **Data issues**: mislabeled data, leakage, or missing shuffling can ruin results—check splits and preprocessing carefully.

---

## Good defaults & tuning tips
- **Optimizer**: Adam with `lr=1e-3` (classification/regression baselines).
- **Batch size**: 32–128 (fit to GPU/CPU memory first).
- **Epochs**: 5–30 for small tasks; use early stopping on val loss.
- **Regularization**: dropout `0.1–0.3`, weight decay `1e-4–1e-2` if overfitting.
- **Learning rate schedule** (optional): cosine decay or step LR once you’re stable.

---

## Glossary (short definitions)
- **Perceptron / neuron**: weighted sum + bias + activation.
- **Weights / bias**: learned parameters.
- **Activation**: nonlinearity (ReLU, GELU, Sigmoid, Tanh) enabling stacked layers to model complex functions.
- **Layer / depth**: transformation stage; depth = # hidden layers.
- **Representation learning**: network learns features automatically.
- **Backpropagation**: gradient computation via chain rule through the graph.
- **Optimizer**: algorithm that updates parameters (SGD, Adam).

---

## Quick start checklist
1. Define task & dataset; create **train/val/test** split.
2. Start with a **small model** suited to your data type (MLP for tabular, CNN for images, Transformer/embeddings for text).
3. Use sensible defaults (Adam 1e-3, batch 32–128, epochs 5–30).
4. **Sanity check**: overfit a tiny subset; verify training curves and metrics.
5. Iterate: LR, width/depth, regularization, data quality/augmentation, and early stopping.
