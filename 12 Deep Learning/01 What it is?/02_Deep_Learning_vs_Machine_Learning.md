# 02 — Deep Learning vs Machine Learning

A memory-friendly, video-aligned summary you can skim before coding or interviews.

---

## Table of contents
- [Overview](#overview)
- [Key differences (at a glance)](#key-differences-at-a-glance)
- [How performance scales with data](#how-performance-scales-with-data)
- [Hardware & compute](#hardware--compute)
- [Training time vs. prediction time](#training-time-vs-prediction-time)
- [Features: manual vs. learned (representation learning)](#features-manual-vs-learned-representation-learning)
- [Interpretability](#interpretability)
- [When to choose what (decision guide)](#when-to-choose-what-decision-guide)
- [Use-case patterns](#use-case-patterns)
- [Pitfalls & myths](#pitfalls--myths)
- [Quick checklist](#quick-checklist)

---

## Overview
**Deep Learning (DL)** is a subfield of ML that uses multi-layer neural networks.  
This lesson compares DL and **traditional Machine Learning (ML)** on practical axes (data, hardware, time, features, interpretability) and explains why DL doesn’t *replace* ML—each has the right job.

---

## Key differences (at a glance)

| Axis | Machine Learning | Deep Learning |
|---|---|---|
| **Data need** | Works with small→medium datasets | **Data-hungry**; really shines with lots of data |
| **Hardware** | CPU is often fine | **GPU/TPU** preferred for heavy matrix ops |
| **Training time** | Usually shorter | Often **long** (hours→weeks for big jobs) |
| **Prediction time** | Can be slower for some algos | Often **fast** once trained |
| **Features** | **Manual** feature engineering | **Automatic** (representation learning) |
| **Interpretability** | Easier to explain (trees, linear models) | Often a **black box** |

> Bottom line: pick the tool that fits the data size, compute budget, timelines, and need for interpretability.

---

## How performance scales with data
- With **limited data**, classic ML models often perform **better** than DL.
- As **data increases**, ML performance tends to **plateau**, while DL models usually **keep improving** (near-linear gains) because they learn richer representations.
- Practical read: If you expect data growth (or can augment/collect more), DL pays off. If not, ML may be the better baseline.

---

## Hardware & compute
- **ML**: can train on **CPUs** comfortably.
- **DL**: benefits from **GPUs/TPUs** due to large matrix multiplications; CPU-only training is typically slow.

---

## Training time vs. prediction time
- **Training**: DL generally takes **longer** to train than ML (especially on large datasets/architectures).
- **Prediction (inference)**: DL can be **very fast** once trained, whereas some ML models (e.g., k-NN, some kernel methods) can be slower at prediction time.

---

## Features: manual vs. learned (representation learning)
- **ML**: you **hand-craft** features (domain knowledge, feature selection).
- **DL**: the network **learns features automatically** from raw/low-level inputs; deeper layers compose simple patterns into complex concepts.

---

## Interpretability
- **ML**: models like logistic regression and decision trees provide **clear explanations** (weights, feature importance, decision paths).
- **DL**: high accuracy but often **opaque**—hard to justify individual decisions without extra tooling (e.g., saliency/SHAP/LRP).

---

## When to choose what (decision guide)
Use **ML** when:
- Data is **small/medium**, labeling is expensive, or you need **explanations**.
- You need a **quick baseline** or have limited compute/time.
- Tabular problems with strong, well-engineered features.

Use **DL** when:
- You have **lots of data** (or can scale data/augmentation).
- Tasks involve **images, audio, text**, or complex signals.
- You want **state-of-the-art** accuracy and can train on **GPUs/TPUs**.

> Heuristic: start with a strong ML baseline. If data or accuracy demands grow, graduate to DL.

---

## Use-case patterns
- **ML-leaning**: credit scoring, small tabular datasets, explainable dashboards.
- **DL-leaning**: computer vision (classification/detection/segmentation), NLP (classification, QA, translation), speech (ASR/TTS), and large-scale multimodal tasks.

---

## Pitfalls & myths
- **Myth**: “DL replaces ML.”  
  **Reality**: They’re complementary. Think **needle vs. sword**—use the right tool for the job.
- **Pitfall**: Choosing DL without GPUs or enough data → long training, weaker results than a well-tuned ML model.
- **Pitfall**: Ignoring interpretability requirements in regulated domains.

---

## Quick checklist
1. **Data size?** Small→ML, Large→DL (or plan to collect/augment).
2. **Hardware?** No GPU→ML first; Have GPU(s)→DL viable.
3. **Timeline?** Need fast training/iteration→ML; can invest time→DL.
4. **Explainability?** Must explain decisions→favor ML or add XAI to DL.
5. **Signal type?** Vision/NLP/Audio→DL usually wins; tabular→try ML first.

---
