# Basic CNN stacks, LeNet, and CNN vs ANN

## A) Typical CNN Block
- Pattern: [Conv → (BN) → ReLU] × N → Downsample (MaxPool 2×2 or Conv stride 2)  
- Why: Conv learns local parts, BN makes training steady, ReLU adds nonlinearity, pooling/stride reduces size and cost  
- Shapes: with “same” padding and stride 1, H and W stay the same; stride 2 or pooling halves them  
- Channel tip: when size halves, double the filters (32 → 64 → 128)  

---

## B) LeNet-5 (1998) — Classic Example
- Task: digit recognition (MNIST)  
- Input: 32×32×1 (gray)  
- Layers:  
  - Conv (6 filters, 5×5, valid) → 28×28×6  
  - AvgPool (2×2, stride 2) → 14×14×6  
  - Conv (16 filters, 5×5, valid) → 10×10×16  
  - AvgPool (2×2, stride 2) → 5×5×16  
  - Flatten → 400 → Dense 120 → Dense 84 → Dense 10 (softmax)  
- Key points: local receptive fields, shared weights, early downsampling, small fully connected head  

---

## C) Simple Design Guidelines
- Start small: 32 or 64 filters, kernel 3×3, padding “same”  
- Use 2 convs per level, then downsample (MaxPool or stride 2)  
- Double filters each time you downsample  
- Use GlobalAveragePooling instead of huge Flatten  
- Add Dropout, light weight decay, and data augmentation  
- Train with Adam, monitor validation loss, apply early stop  
- Don’t over-pool: keep detail if tiny features matter  

---

## D) Minimal Keras Model
```python
import tensorflow as tf
from tensorflow.keras import layers, models

def tiny_cnn(num_classes=10, input_shape=(32,32,3)):
    x = inputs = layers.Input(shape=input_shape)
    # Block 1
    x = layers.Conv2D(32, 3, padding='same', use_bias=False)(x)
    x = layers.BatchNormalization()(x); x = layers.ReLU()(x)
    x = layers.Conv2D(32, 3, padding='same', use_bias=False)(x)
    x = layers.BatchNormalization()(x); x = layers.ReLU()(x)
    x = layers.MaxPooling2D(2)(x)  # 32→16
    # Block 2
    x = layers.Conv2D(64, 3, padding='same', use_bias=False)(x)
    x = layers.BatchNormalization()(x); x = layers.ReLU()(x)
    x = layers.Conv2D(64, 3, padding='same', use_bias=False)(x)
    x = layers.BatchNormalization()(x); x = layers.ReLU()(x)
    x = layers.MaxPooling2D(2)(x)  # 16→8
    # Head
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)
    return models.Model(inputs, outputs)

model = tiny_cnn()
model.summary()
```

## 5 ANN Vs CNN


| Aspect              | CNN (Convolutional NN)                                | ANN (Fully Connected NN)                           |
|---------------------|-------------------------------------------------------|---------------------------------------------------|
| Connection pattern  | Local patches only (small receptive fields)           | Every input connects to every neuron              |
| Weight handling     | Shared kernel weights reused across whole image       | Separate weight per input–neuron pair             |
| Parameters          | Small: ~kernel × in_ch × out_ch                       | Huge: input_dim × hidden_dim, grows very fast     |
| Spatial structure   | Keeps 2D/3D grid (spatial info preserved)             | Flattens input, spatial layout lost               |
| Compute scaling     | Few weights → efficient                               | Millions of weights if input is large             |
| When it wins        | Images, videos, spectrograms, any grid-like data      | Tabular data, tiny heads after CNN, small inputs  |
| Translation handling| Naturally tolerant to shifts (conv + pooling)         | No tolerance unless engineered                    |




## 6 Quick checklist (memory hook)
- Stack Conv → BN → ReLU; keep “same” early, stride 1
- Downsample on purpose (MaxPool or stride-2 conv)
- Double channels when H,W halve
- Finish with GlobalAveragePooling + a small Dense
- Goal: fewer weights, keep spatial structure, train steady

