# Padding & Stride (shape control)

## 1) Why padding is needed (border loss)
- **Shrink problem:** a `K×K` filter cannot sit on the outer ring without falling off. With **valid** conv (`P=0`), output gets smaller each layer → you keep losing border information.
- **Border bias:** center pixels are used in many filter positions; border pixels are used in few. Without padding, borders matter less.
- **Fix:** add **padding** around the image so the filter can slide everywhere fairly and output size stays under control.

---

## 2) Zero padding (output size control)
- **Zero padding** adds rows/cols of zeros around the image (most common). Other types exist (reflect, replicate), but start with zeros.
- **Output size (2D conv):**  
  Given input `H×W×C`, kernel `K` (square for simplicity), stride `S`, padding `P` on all sides:
  - `H_out = floor((H + 2P − K)/S) + 1`  
  - `W_out = floor((W + 2P − K)/S) + 1`  
  - Channels out = number of filters `F`.
- **Valid vs Same:**
  - **valid**: `P = 0` → shrinks. Example: `H=W=28, K=3, S=1` → `H_out=W_out=26`.
  - **same (S=1)**: choose `P = floor(K/2)` (for odd `K`) to keep size: `H_out=W_out=H=W`. Example: `28, K=3, P=1, S=1` → `28`.
  - **same (S>1)**: libs pick `P` so `H_out ≈ ceil(H/S)`. Expect downsampling while roughly centering features.

**Tiny examples (padding):**
- `5×5×1`, `K=3`, `S=1`  
  - valid (`P=0`) → `3×3`  
  - same (`P=1`) → `5×5`
- `64×64×3`, `K=5`, `S=1`  
  - valid → `60×60`  
  - same (`P=2`) → `64×64`

**Why “same” early on?** You keep resolution for a few layers so small patterns aren’t lost too soon.

---

## 3) Stride (downsampling while convolving)
- **Stride `S`** = how far the filter jumps each move (right or down).
  - `S=1`: check every position.
  - `S=2`: skip every other position → output **shrinks by ~½** per axis.
- **Formula with stride:**  
  `H_out = floor((H + 2P − K)/S) + 1`, same for `W_out`.
- **Effect:** larger `S` → fewer spatial locations, less compute, fewer activations, but also less fine detail (you’re skipping pixels).

**Tiny examples (stride):**
- `H=W=28, K=3, P=0, S=2` → `H_out = floor((28−3)/2)+1 = floor(25/2)+1 = 12+1 = 13` → `13×13`.
- `H=W=28, K=3, P=1, S=2` (same-style) → `H_out = floor((28+2−3)/2)+1 = floor(27/2)+1 = 13+1 = 14` → `14×14`.

---

## 4) When/why to use non-unit stride (S>1)
Use `S>1` when you want **built-in downsampling** and cheaper compute:
- **Early reduction:** big images → use `S=2` (with `same` padding) to shrink maps and speed up.
- **Replace pooling:** a **strided conv** can downsample while learning filters (often used instead of max-pool).
- **High-level focus:** bigger strides ignore fine detail and keep coarse structure (useful when small textures are not needed).

**Caution:**
- Too large a stride can **drop important details** and cause **aliasing**. Prefer small `K` (e.g., `3×3`), `S=1` in most convs; downsample only at planned stages (stride 2 or pooling).

---

## 5) Quick tables

### 5.1 Valid vs Same (S=1)
| Setting | Padding `P`           | Output size         | Use case |
|---|---|---|---|
| valid  | `0`                    | shrinks: `(H−K+1)`  | Fast shrink, cut borders |
| same   | `floor(K/2)` (odd `K`) | keeps `H, W` equal  | Preserve resolution early |

### 5.2 Stride cheat-sheet
| Stride `S` | What happens | Typical use |
|---|---|---|
| 1 | full detail, bigger outputs | default for most convs |
| 2 | halves `H, W` (≈) | planned downsampling blocks |
| ≥3 | strong shrink, detail loss | rare; special architectures |

---

## 6) Design defaults (keep it simple)
- Start blocks with **`3×3` conv, `S=1`, `same` padding**. Stack 2–3 such convs.
- Downsample with **`S=2` conv** (or max-pool) every few blocks.
- Keep shapes in check with the formula `floor((H + 2P − K)/S) + 1`.
- Prefer **odd K** (3, 5) so `same` padding is symmetric.
- Verify shapes per layer to avoid silent shrink too early.

---

## 7) One-minute shape workout
1) Input `32×32×3`, `K=3`, `P=1`, `S=1`, `F=32` → Output `32×32×32`.  
2) Then `K=3`, `P=1`, `S=2`, `F=64` → `16×16×64`.  
3) Then `K=3`, `P=1`, `S=1`, `F=64` → `16×16×64`.  
You kept detail first, then downsampled once, then refined again.

---

## 8) Key takeaways
- **Padding** protects borders and controls size.  
- **Stride** controls how much you downsample during the conv.  
- Combine **same+S=1** for detail, use **S=2** (sparingly) to shrink maps and save compute.