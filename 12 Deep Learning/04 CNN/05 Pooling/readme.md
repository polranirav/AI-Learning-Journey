# Pooling layers (make maps smaller, add small shift tolerance)

## 1) Why pooling?
- **Reduce size:** feature maps after conv can be big. Pooling shrinks **H×W** fast (less memory, faster compute).
- **Small shift tolerance:** if an edge moves a few pixels, pooled features change less → model is a bit **translation-invariant**.
- **No training needed:** pooling has **no weights**. You only choose window size and stride.

---

## 2) What pooling does (in one line)
Take a small **window** (e.g., `2×2`) and slide it with **stride** (e.g., `2`). Replace the window by **one number** (max, average, etc.). Repeat over the whole map.

---

## 3) Types of pooling (what number do we keep?)
| Type | What it keeps | Good for | Notes |
|---|---|---|---|
| **Max pooling** | Biggest value in the window | Preserve strong edges/features | Most common (`2×2`, stride `2`) |
| **Average pooling** | Mean of values | Smooth downsample | Gentler than max; can blur small peaks |
| **L2 / RMS pooling** | sqrt(mean(square)) | Energy of signal | Middle ground (rare) |
| **Global Avg Pool (GAP)** | Average over entire **H×W** per channel | Replace flatten+FC head | Very common in CNN heads |
| **Global Max Pool** | Max over entire **H×W** per channel | Keep strongest activation | Less common than GAP |

**Tip:** Start with **max pooling**. Use **GAP** near the end of the network to go from maps to a feature vector.

---

## 4) Windows, stride, shapes (simple math)
For input map `H×W×C`, window (kernel) size `K` (square for simplicity), stride `S`, padding `P` (usually `0` = valid):

- `H_out = floor((H + 2P − K)/S) + 1`  
- `W_out = floor((W + 2P − K)/S) + 1`  
- **Channels do not change:** output channels = input channels `C` (pooling is done **per channel**).

**Common picks**
- **MaxPool `2×2, stride 2`** → halves H and W (≈ **4×** fewer activations).
- Use padding `'same'` only if you must align shapes; default is `'valid'`.

---

## 5) Pooling “on volumes” (multi-channel)
Pooling runs **independently on each channel**.  
Example: input `32×32×64` → MaxPool `2×2, S=2` → output `16×16×64`.

---

## 6) Tiny demo (max pool by hand)
Window `2×2`, stride `2`, no padding.

Input `4×4` map  