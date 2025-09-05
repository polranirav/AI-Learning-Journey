# Convolution (core idea)

## 1) Image basics (H×W×C)
- **Image = grid of numbers.**  
  - Grayscale: shape **H×W×1** (one channel).  
  - Color (RGB): shape **H×W×3** (three channels: R, G, B).
- **Batching:** training uses **N×H×W×C** (or **N×C×H×W** in some libs).
- **Why not flatten to a vector?** You’d lose spatial layout and explode the parameter count. Convolution keeps layout and uses few weights.

---

## 2) What a convolution does (plain view)
- We slide a small **kernel/filter** over the image.
- At each position, we multiply the kernel by the pixel patch and **sum** → one number.  
- Do this everywhere → a **feature map** (also called an activation map).
- **One filter = one output channel**. Many filters = stacked output channels.

**Shapes (one layer):**  
Input **(H, W, C)** → Filters: **F** kernels of size **(K, K, C)** → Output **(H_out, W_out, F)**.

**Output size formulas (2D):**  
Let **stride = S**, **padding = P** on all sides, **kernel = K** (odd K typical).
- `H_out = floor((H + 2P − K)/S) + 1`  
- `W_out = floor((W + 2P − K)/S) + 1`  
- Channels out = **F**.

**Padding types:**
- **valid** = no padding (`P = 0`) → output shrinks.
- **same** = pad so size stays (roughly) same when `S=1` → choose `P = floor(K/2)`.

**Stride (S):**
- How many pixels we jump each slide. Bigger **S** downsamples (smaller output).

**Params per layer:**  
Each filter has **K·K·C** weights + **1** bias → total params  
`= F · (K·K·C + 1)`.

---

## 3) Edge detection (tiny demo with simple kernels)
Kernels are just small number grids that fire on certain patterns.

**Vertical edge kernel (3×3):**
| -1 |  0 | +1 |
|----|----|----|
| -1 |  0 | +1 |
| -1 |  0 | +1 |

**Horizontal edge kernel (3×3):**
| -1 | -1 | -1 |
|----|----|----|
|  0 |  0 |  0 |
| +1 | +1 | +1 |

How it behaves:
- Where the image patch **matches** the kernel’s pattern (e.g., strong left→right change), the sum is **large positive**.
- Where it’s the **opposite**, the sum is **negative**.  
- After **ReLU** (max(0, x)), negative responses drop to 0, positives survive → a clean map of “found edges”.

Tips:
- Use **3×3** kernels as a default. They’re small, cheap, and stack well.
- CNNs **learn** filter values during training, so you rarely hand-craft kernels—these are just for intuition.

---

## 4) Working with RGB (depth-wise sum idea)
- A color image patch has **3 slices** (R, G, B).  
- A filter also has **3 slices** (one per channel).  
- At each position: multiply **R×R_filter**, **G×G_filter**, **B×B_filter**, then **sum across channels** and add bias.  
- That **sum across depth** gives **one** number at that (y, x) → 1 output channel for that filter.

So, with **F** filters, you get **F** output channels (a stack of feature maps).

---

## 5) Multiple filters → stacked feature maps
- If you use **F = 32** filters of shape **(3,3,C)** with `S=1`, `P=1 (same)`, then  
  Input **(H, W, C)** → Output **(H, W, 32)**.
- Early filters often become **edge/texture** detectors; deeper filters combine them into **parts** and then **objects**.

---

## 6) Tiny shape & parameter examples
- **Example A (grayscale):** Input **28×28×1**, **F=8**, **K=3**, **S=1**, **P=1 (same)** → Output **28×28×8**.  
  Params = `8 · (3·3·1 + 1) = 8 · 10 = 80`.
- **Example B (RGB):** Input **64×64×3**, **F=32**, **K=3**, **S=1**, **P=1 (same)** → Output **64×64×32**.  
  Params = `32 · (3·3·3 + 1) = 32 · 28 = 896`.
- **Example C (valid, no pad):** Input **28×28×1**, **K=5**, **S=1**, **P=0** → Output **24×24×F** (because `28−5+1=24`).

---

## 7) “Valid” vs “Same” at a glance
| Setting | Padding P | Output size (S=1) | When to use |
|---|---|---|---|
| **valid** | 0 | shrinks: `(H−K+1)×(W−K+1)` | cut borders, reduce size quickly |
| **same** | `floor(K/2)` | keeps H, W same | preserve resolution in early layers |

---

## 8) Why convolution is efficient
- **Few weights**: `K·K·C` per filter vs `(H·W·C)·units` in a dense layer.  
- **Weight sharing**: same filter reused at all positions → strong generalization.  
- **Keeps layout**: feature maps still have 2D structure → later layers can build on spatial patterns.

---

## 9) Quick FAQ
**Q: Why are outputs sometimes negative?**  
A: The pattern is the “opposite” of the kernel. Apply **ReLU** or take magnitude if needed.

**Q: Why do deeper layers “see more”?**  
A: Stacking increases the **effective receptive field** (each layer looks at a larger area of the original image).

**Q: What sets the number of filters (F)?**  
A: It’s a design knob: more filters = more features (but more compute). Common starts: 16/32/64 and scale up.

---

## 10) Pocket checklist (do this by default)
- Use **3×3** kernels, **stride 1**, **same** padding in early conv blocks.  
- Double filters gradually (e.g., 32→64→128) as you go deeper.  
- Add **ReLU** after each conv.  
- Downsample with **stride 2** conv or pooling when you need smaller maps.  
- Remember shapes: Input `(H,W,C)` + Filters `(K,K,C,F)` → Output `(H_out,W_out,F)` with the formula above.

*If you remember just one line:* **Convolution = small kernel × local patch, sum across space and channels, stack many filters → rich feature maps.**