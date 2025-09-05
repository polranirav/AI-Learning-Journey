# 03 — Why Deep Learning Now?

A video-aligned summary explaining **why deep learning became famous and powerful in the 2010s**, organized around the same five drivers your instructor highlighted.

---

## Table of contents
- [Overview](#overview)
- [The five drivers (high level)](#the-five-drivers-high-level)
- [1) Data & Public Datasets](#1-data--public-datasets)
- [2) Frameworks & Libraries](#2-frameworks--libraries)
- [3) Model Architectures & Transfer Learning](#3-model-architectures--transfer-learning)
- [4) Hardware (GPU/TPU/ASIC/FPGA/NPU)](#4-hardware-gputpuasicfpganpu)
- [5) Community Momentum](#5-community-momentum)
- [Practical implications for you](#practical-implications-for-you)
- [Starter hardware guide (from the talk)](#starter-hardware-guide-from-the-talk)
- [Quick checklist](#quick-checklist)

---

## Overview
- Work on neural networks dates back decades (e.g., late 1960s), but deep learning **surged in popularity around 2010–2012**.
- The instructor groups the reasons into **five drivers**: **datasets, frameworks, architectures, hardware, community**—together these unlocked today’s progress.

---

## The five drivers (high level)
1) **Data (and labeled public datasets)**  
2) **Frameworks & libraries** that hide low-level complexity  
3) **Model architectures** (ready patterns) and **transfer learning**  
4) **Hardware** specialized for parallel math (GPU/TPU/etc.)  
5) **Community** sharing code, models, and tutorials

---

## 1) Data & Public Datasets
- DL is **data-hungry**; performance improves as data grows.
- Two revolutions boosted data availability: **smartphones** everywhere + **cheaper internet** → massive daily data generation.
- Industry invested to convert raw app/media data into **labeled** datasets and then released many as **public datasets**, accelerating research.
- Examples from the video:
  - **MS COCO** for **object detection** (images with bounding boxes + labels)
  - **YouTube-8M** for **video** understanding (millions of labeled clips)
  - **SQuAD** for **question answering** (text)
  
---

## 2) Frameworks & Libraries
- Training DL from scratch is hard; low-level math and kernels take time.
- Modern frameworks **abstract** those internals so you can focus on the application.
- The talk calls out the shift to high-level, production-ready libraries in DL—similar to how scikit-learn helps in classical ML.

---

## 3) Model Architectures & Transfer Learning
- Availability of **standard architectures** gives a head start for many tasks (the lesson mentions having “ready” backbones).
- **Transfer learning** pattern emphasized: start from a **pretrained** model and fine-tune on your dataset to reach strong results with less data/time.

---

## 4) Hardware (GPU/TPU/ASIC/FPGA/NPU)
- DL training relies on huge **matrix multiplications** → ideal for **parallel processing**.
- Around 2010, the field broadly moved from CPU to **GPU** for training to dramatically cut training time.
- Beyond GPUs:
  - **TPU** (by Google): application-specific hardware for DL workloads.
  - **ASICs/NPUs** (on phones): dedicated neural processing in mobile chips.
  - **FPGAs**: reprogrammable chips used in industry pipelines (e.g., at search scale) for efficient, low-power inference.
- Key takeaway from the talk: specialized hardware **unlocked speed**, which in turn **accelerated research**.

---

## 5) Community Momentum
- As companies released datasets, code, and papers, progress compounded.
- Open resources + tutorials + model zoos → faster learning curves and quicker iteration.

---

## Practical implications for you
- Expect better results as you scale data and compute.
- For small projects, start simple; when you need more accuracy and can leverage pretrained models + GPUs, deep learning pays off.
- Choose hardware according to your **project size** and **deployment target** (PC, phone, edge device).

---

## Starter hardware guide (from the talk)
- **Just starting / tiny projects** → CPU can be enough.
- **Training larger networks** → move to **GPU**.
- **On-device/mobile apps** → use mobile CPU/GPU/DSP or **NPU**.
- **Edge wearables (watch/glasses)** → small **ASIC/MCU/“H-tube”/NPUs** style accelerators (per the examples in the talk).

---

## Quick checklist
1. Do you have (or can you get) **labeled data**? If yes, DL scales.
2. Pick a **framework** (PyTorch/TensorFlow) to avoid low-level pain.
3. Start from a **known architecture**; try **transfer learning** first.
4. Match **hardware** to problem size (CPU→GPU→TPU/FPGA/NPU).
5. Lean on the **community** (open datasets, model hubs, tutorials).

