# 08_pretrained_models — Using Ready Models

---

## 1) Why Use Pretrained Models (Simple Reasons)
- **You save data**: Big CNNs need lots of labeled images. Pretrained models were already trained on millions, so you don’t start from zero.
- **You save compute & time**: Training from scratch can take days on GPUs. Loading a ready model starts in seconds and often reaches strong accuracy fast.
- **You stand on proven designs**: Battle-tested backbones (ResNet, VGG, EfficientNet, etc.) are well-understood and documented; you reuse their strengths.
- **You reduce overfitting**: When your dataset is small, starting from a model that already “knows” general visual patterns (edges → parts → objects) helps the model generalize.

---

## 2) ImageNet & ILSVRC (The Base Everyone Shares)
- **ImageNet**: A very large visual database (~1.2M training images) across 1,000 classes; diverse, daily objects. Models trained here learn broadly useful features.
- **ILSVRC (ImageNet Challenge)**: Annual benchmark (2010–2017) using that 1K-class subset. It popularized CNN progress: *AlexNet (2012) → ZFNet → VGG → GoogLeNet/Inception → ResNet → DenseNet → EfficientNet*. Error rates dropped below human-level on the task.
- **Why it matters**: “ImageNet-pretrained” means the backbone weights already encode general vision features; you fine-tune them for your task (cats vs. dogs, x-ray scans, products, etc.).

---

## 3) Famous Backbone Families (Quick Memory Hook)
- **Early**: AlexNet, ZFNet, VGG-16/19
- **Inception line**: GoogLeNet, Inception-v1/-v3/-v4, Xception
- **Residual & dense**: ResNet-18/34/50/101, ResNeXt, DenseNet
- **Mobile/efficient**: MobileNet-V1/V2/V3, EfficientNet-B0…B7, EfficientNetV2
- **Modern CNN tweaks**: RegNet, ConvNeXt

---

## 4) How to Use a Pretrained Model (Plain Steps)
1. **Pick a backbone** that fits your budget:
   - Tiny device → *MobileNet, EfficientNet-B0*
   - Balanced → *ResNet-50*
   - Highest accuracy (bigger) → *EfficientNet-B4…B7*
2. Load weights pretrained on **ImageNet**.
3. Cut off the **top classifier** (keep the feature extractor).
4. Add your **custom head** (GlobalAveragePooling → small Dense → output).
5. **Freeze then unfreeze**:
   - Start frozen → train only your head.
   - Then unfreeze top *N* layers of the backbone and fine-tune with a **low LR**.
6. Mind **input rules**: Most backbones expect ~224×224 (some 299×299) and specific preprocessing.
7. **Regularize & monitor**: Use augmentation, dropout, early stopping; track validation loss/accuracy or F1 score.

---

## 5) Quick Keras “Load a Backbone” Demo (no code box, just lines)
- `from tensorflow.keras.applications import ResNet50, resnet50`
- `from tensorflow.keras import layers, models`
- `backbone = ResNet50(weights="imagenet", include_top=False, input_shape=(224,224,3))`
- `backbone.trainable = False  # freeze for a warm start`
- `inp = layers.Input((224,224,3))`
- `x = resnet50.preprocess_input(inp)`
- `x = backbone(x)`
- `x = layers.GlobalAveragePooling2D()(x)`
- `x = layers.Dropout(0.2)(x)`
- `out = layers.Dense(num_classes, activation="softmax")(x)`
- `model = models.Model(inp, out)`
- `model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["acc"])`
- `# Fine-tune later`
- `backbone.trainable = True  # then recompile with a smaller LR (e.g., 1e-5) and train a few more epochs`

---

## 6) Tiny FAQ (Beginner Traps)
- **Do I always need to unfreeze?** Not always. If your task is close to ImageNet, a frozen backbone + trained head may be enough. If the domain is different (e.g., medical scans), fine-tune.
- **Which input size?** Most CNN backbones: **224×224**. Inception/Xception: **299×299**. EfficientNet varies (B0=224, B3=300, etc.).
- **Which preprocessing?** Use the matching helper (e.g., `resnet50.preprocess_input`). It matters for performance.
- **Can I change the last activation/loss?** Yes — sigmoid + binary_crossentropy for multi-label; softmax + categorical/sparse_categorical_crossentropy for single-label multi-class.
- **What about speed?** Prefer MobileNet/EfficientNet-B0 for phones/edge; keep batch size modest; consider mixed precision on GPUs.

---

## 7) One-Minute Recipe (Memorize)
- Load pretrained backbone (**no top**) → GAP → Dropout → Dense(out).
- Freeze → train head (fast).
- Unfreeze top blocks → low-LR fine-tune (careful).
- Use correct preprocessing and right input size.
- Pick backbone by your device & accuracy needs.

---

## 8) Key Takeaways
- **Pretrained = free knowledge** learned on huge data.
- You get faster training, better generalization, and fewer labels needed.
- Start frozen, then fine-tune gently; always match input size & preprocessing.
- Choose the backbone that matches your constraints (**size/speed/accuracy**).

---