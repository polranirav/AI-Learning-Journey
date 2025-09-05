# 07_backprop_in_cnn — How Training Flows in CNNs

## 1) What is backprop in CNNs?
Backpropagation is the method used to **update weights** in a convolutional neural network (CNN). It tells each parameter (filter weight, bias, dense weight) how much it contributed to the error, and how it should be adjusted. CNN backprop is the same principle as in ANNs, but with special handling for **convolution, pooling, flatten/global average pooling, and softmax heads**.

---

## 2) Forward pass recap (the pipeline)
1. **Input image** → goes into **convolution layer** (filters slide and produce feature maps).  
2. Apply **non-linearity** (ReLU or similar).  
3. Sometimes apply **pooling** (max or average) or stride to shrink maps.  
4. Stack multiple conv+activation+pooling blocks.  
5. Flatten or GlobalAveragePooling the feature maps.  
6. Dense (fully connected) layers → output logits.  
7. Softmax/Sigmoid head → predicted class probabilities.  
8. Loss function (cross entropy, etc.) compares predicted vs true label.

---

## 3) Where gradients flow
During backprop, the loss gradient flows **backward step by step**:

- **Softmax + Loss**: compute error at output. For softmax with cross-entropy, derivative is simple:  
  `dL/dz = y_pred − y_true`.
- **Dense layer**: gradients go into weights (`W_dense`), biases, and inputs (which were flatten/GAP outputs).
- **Flatten or GAP**: reshapes don’t add parameters; gradients are just reshaped back.
- **Pooling layers**:  
  - Max pooling → gradient flows only to the position that was maximum in the forward pass.  
  - Average pooling → gradient is equally divided to all inputs in the window.
- **ReLU (or other activation)**: derivative is 1 if input > 0, else 0 (ReLU). For others, use their simple formulas.
- **Convolution layers**: trickiest part — each filter weight is updated by convolving the input patch with the gradient coming from above. Gradients are also passed back to earlier feature maps.

---

## 4) Shapes and intuition
- In conv backprop, the **incoming gradient** has the same shape as the feature map.  
- To update filter weights, you slide over the input with the gradient just like a conv.  
- To update biases, just sum up gradients across the feature map.  
- Gradient wrt input is like “full” convolution of the flipped filter with the gradient.  

**Key memory hook:** forward = input * filter → output.  
Backward = output_grad * filter (to update weights) and output_grad * input (to send back).

---

## 5) Pooling backprop (simple rules)
- **Max pooling**: only the winning pixel in each region gets the gradient; others get 0.  
- **Average pooling**: gradient is spread evenly across all pixels in the pooling window.  

---

## 6) Worked toy flow (tiny CNN)
Input `6×6` → Conv(3×3, 1 filter) → ReLU → MaxPool(2×2) → Flatten → Dense(1).  
- Forward shapes:  
  - Conv → `4×4`  
  - ReLU → `4×4`  
  - MaxPool → `2×2`  
  - Flatten → `4`  
  - Dense → `1` output.  
- Parameters: 3×3 filter + 1 bias = 10, Dense weights = 4, Dense bias = 1 → total 15 trainable.  
- Backprop: error at output → Dense → back to flatten → expand into pooled map → unpool into 4×4 → pass through ReLU mask → update conv filter weights with input patches.  

---

## 7) Gradient intuition without heavy math
- Gradient is just “how much changing this weight will change the loss.”  
- Convolution makes this shared across positions: the same filter is nudged consistently by all its receptive fields.  
- Pooling just routes gradients: max-pool chooses winners, average pool splits evenly.  
- Activations gate gradients: ReLU kills negatives, Sigmoid shrinks large magnitudes, etc.  
- Dense layers behave like classic ANN backprop.  

---

## 8) Why this matters
- Understanding backprop in CNNs helps you debug vanishing gradients, exploding updates, or dead ReLUs.  
- Frameworks (TensorFlow, PyTorch) handle math, but knowing the flow lets you design better architectures and tune training.

---

## 9) Quick checklist (memory hook)
- Error starts at **loss** → flows backward.  
- Softmax + cross-entropy → simple derivative.  
- Dense → weight update = input × gradient.  
- Flatten/GAP → reshaping only, gradients reshaped back.  
- Pooling → max = route to winner, avg = split evenly.  
- ReLU → pass grad if input > 0, else block.  
- Conv → weight grad = input patch × grad; bias grad = sum of grad; input grad = conv of grad with flipped filter.  
- Repeat until input.

---

## 10) Key takeaway
Backprop in CNNs = the same chain rule as in ANNs, but adapted for conv and pooling. Think of it as **errors flowing backward through the same pipeline**: dense, flatten, pooling, activation, convolution, until the input image.