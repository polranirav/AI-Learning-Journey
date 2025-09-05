# Convolutional Neural Networks (CNNs)

## What is a CNN?
- A CNN is a neural network for **grid data**:  
  **1D** = time series, **2D** = images, **3D** = video/volumes.
- It looks at **small patches** with tiny filters and **reuses** the same filter everywhere (few weights).
- Typical block: **Convolution → (Normalization) → Activation → (Pooling)**.  
  At the end: **GlobalAveragePooling/Dense** to make the prediction.

## Why not a plain ANN for images?
| Issue | Plain ANN (dense) | CNN |
|---|---|---|
| Number of weights | Very high (every pixel connects to every neuron) | Low (shared small filters) |
| Spatial layout | Lost after flatten | Kept (local patches) |
| Shift tolerance | Poor | Better (pool/stride) |
| Overfitting risk | High | Lower |
| Speed/memory | Costly on images | Efficient |

## How a CNN “sees” (simple idea)
- **Filters (kernels)** slide across the image; they light up when a pattern is found.  
- **Early layers** learn edges/corners/texture. **Deeper layers** learn parts/shapes/objects.  
- **Padding** keeps size; **stride** skips positions; **pooling** downsamples and adds small shift tolerance.  
- **Channels** = different feature maps (e.g., RGB in, edge/texture maps inside).

## Where CNNs are used (from your notes)
- **Image classification** (cat vs dog, product types)  
- **Object localization / detection** (find boxes and classes)  
- **Segmentation** (label each pixel)  
- **Pose / keypoints** (human skeleton)  
- **Super-resolution, denoising, deblurring**  
- **Colorization** (B/W → color)  
- **OCR & handwriting**  
- **Medical imaging / 3D volumes**  
- **Audio as images** (spectrograms)  
- **Remote sensing** (satellite/drone)

## Tiny history
- **LeNet-5 (1998, Yann LeCun)**: bank **check digit** reading.  
- Then OCR/handwriting → today’s phone cameras and many apps.

## Inputs and shapes (quick facts)
- Image: **(H, W, C)**, batch: **(N, H, W, C)** or **(N, C, H, W)** (depends on framework).  
- **Resize** to a fixed size. **Normalize** (0–1 or per-channel mean/std).  
- Start small; add depth/width only if needed.

## Beginner defaults (work well)
- **Conv kernel**: 3×3; channels: 32 → 64 → 128 as depth grows.  
- **Activation**: ReLU. **Norm**: BatchNorm after conv.  
- **Downsample**: 2×2 max-pool or conv with stride=2.  
- **Head**: GlobalAveragePooling → Dense(softmax).  
- **Optimizer**: Adam (later: SGD+momentum).  
- **LR**: 1e-3 (Adam) or 1e-2 (SGD+m), then tune.  
- **Augment**: flips, random crop/resize, light color jitter.

## Sanity checklist before training
- Fixed input size and **normalized** values  
- Correct **loss** for the task (softmax CE for single-label, BCE for multi-label)  
- Model can **overfit a tiny subset** (e.g., 32–50 images)  
- Train/val curves: loss ↓, accuracy ↑ (no wild jumps)  
- Save **best on validation** (checkpoint / early stop)

## Mini glossary
- **Convolution**: sliding dot-product between a small kernel and an input patch.  
- **Kernel / filter**: the small weight matrix that detects a pattern.  
- **Feature map**: output channel from a filter.  
- **Receptive field**: input area that affects one output value.  
- **Padding**: add border to keep size. **Stride**: step size while sliding.  
- **Pooling**: downsample by max/avg in a small window.  
- **Parameter sharing**: the same kernel is used at all positions.

## One-page roadmap for this CNN folder
1. **Bio vision link** (local receptive fields → CNN idea)  
2. **Convolution basics** (filters, multi-channel conv, feature maps)  
3. **Padding & stride** (size and compute control)  
4. **Pooling** (max/avg; when to use stride-2 conv)  
5. **Basic stacks & LeNet** (first working CNN)  
6. **CNN vs ANN review** (why CNN wins on images)  
7. **Backprop in CNNs** (high-level view)  
8. **Transfer learning** (pretrained backbones, freeze/fine-tune)  
9. **Practice tips** (pipelines, normalization, light augmentation)  
10. **Mini project** (small image classifier like digits or cats vs dogs)

## Summary
CNNs keep **where** things are, learn **local → global** patterns with **few weights**, and work well on images, audio-as-images, and 3D. Use small clean blocks, match loss to task, add light augmentation, and prefer transfer learning when data is limited.