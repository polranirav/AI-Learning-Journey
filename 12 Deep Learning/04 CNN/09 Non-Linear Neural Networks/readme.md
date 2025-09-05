# Keras Functional Model | How to Build Non-Linear Neural Networks

---

## 1) Why Functional API (in one line)
When your model is not just a straight stack—you need branches, merges, multiple inputs, or multiple outputs—use the Functional API. Sequential is great for single-input → single chain → single-output. Functional lets you draw a graph.

---

## 2) When to use it (typical cases)
- Multi-output: one input, two predictions (e.g., from a face image predict age + emotion).
- Multi-input: combine image + text + tabular to predict a product’s price.
- Shared layers: same subnetwork applied to two inputs (e.g., Siamese/metric learning).
- Skip/merge paths: residual/add/concat connections.
- Any non-linear topology your idea needs.

---

## 3) Core idea (3 building blocks)
- Inputs are explicit tensors: `inp = layers.Input(shape=(...))`
- Layers are callables: `x = layers.Dense(64, activation='relu')(inp)`
- Model ties graph ends: `model = Model(inputs=..., outputs=...)`  
That’s it: you wire tensors through layers, then declare which tensors are inputs and which are outputs.

---

## 4) Tiny multi-output example (tabular → age + city)
- `from tensorflow.keras import layers, Model, optimizers`
- `inp = layers.Input(shape=(3,), name='tabular')              # [salary, height, marital_status]`
- `h   = layers.Dense(64, activation='relu', name='h1')(inp)`
- `h   = layers.Dense(32, activation='relu', name='h2')(h)`
- `age = layers.Dense(1,  activation='linear',  name='age')(h)       # regression`
- `city= layers.Dense(2,  activation='softmax', name='city')(h)      # 2 classes (e.g., Delhi/Mumbai)`
- `model = Model(inputs=inp, outputs=[age, city], name='multi_output')`
- `model.compile(optimizer=optimizers.Adam(1e-3),`
- `              loss={'age':'mse','city':'sparse_categorical_crossentropy'},`
- `              metrics={'age':['mae'],'city':['accuracy']},`
- `              loss_weights={'age':0.5,'city':1.0})`
- `# Training data: X shape (N,3); y_age shape (N,1); y_city shape (N,)`
- `model.fit(X, {'age': y_age, 'city': y_city}, batch_size=32, epochs=..., validation_data=...)`  
**Why this works:** one shared “trunk” learns common features; two “heads” specialize (regression + classification).

---

## 5) Multi-input + concat example (two streams → one prediction)
- `from tensorflow.keras import layers, Model`
- `inp_a = layers.Input(shape=(32,),  name='meta')            # tabular`
- `inp_b = layers.Input(shape=(128,), name='text_embed')      # text embedding (already encoded)`
- `a = layers.Dense(64, activation='relu')(inp_a)`
- `b = layers.Dense(64, activation='relu')(inp_b)`
- `z = layers.Concatenate(name='join')([a, b])                # merge features`
- `z = layers.Dense(64, activation='relu')(z)`
- `out = layers.Dense(1, activation='linear', name='price')(z)  # regression`
- `model = Model([inp_a, inp_b], out)`
- `# Fit with dicts or lists: model.fit({'meta': Xa, 'text_embed': Xb}, y, ...)`  
**Tip:** Concat grows features; Add/Average keeps size (good for residual paths).

---

## 6) Shared layers (same weights on different inputs)
- `shared = layers.Dense(64, activation='relu', name='shared_dense')`
- `a = shared(inp_a)`
- `b = shared(inp_b)`  
Now `a` and `b` came through the same layer = **shared weights**. Use this for Siamese/similarity models or whenever two branches should learn the same transformation.

---

## 7) Compile & train with multiple outputs (rules of thumb)
- Provide loss for every output (dict or list).
- Use `loss_weights` to balance tasks (larger weight = task matters more).
- Name your layers/outputs; feed/collect by those names (clean & debuggable).
- Datasets/Generators: emit dicts that match input/output names.

---

## 8) Merges you’ll use (quick cheat)
- `Concatenate([x, y])` → stacks features; channel increases.
- `Add([x, y])` / `Average([x, y])` → elementwise; shapes must match.
- `Multiply([x, y])` → gating/attention-like effects.
- `GlobalAveragePooling2D` before Dense head (keeps params low).

---

## 9) Debugging & best practices
- Name everything (`name='...'`) so `model.summary()` is readable.
- Check shapes often; merges need compatible shapes.
- Start simple (one branch), then add branches/outputs.
- BatchNorm & tiny batches can wobble—freeze BN or use bigger batches.
- Regularize heads (Dropout/weight decay) to avoid overfitting.
- Plot the graph (optional): `tf.keras.utils.plot_model(model, show_shapes=True)`.

---

## 10) Pattern library (mix & match)
- One input → two heads (regression + classification): shared trunk → two Dense heads.
- Two inputs → concat → one head (meta + text/image).
- Image + tabular: CNN branch (Conv → GAP) + tabular MLP → Concat → Dense head.
- Shared tower: same subnetwork applied to two inputs, then distance/contrastive loss.
- Residual: `y = layers.Add()([y, shortcut])` to ease optimization.

---

## 11) Quick memory hook
- Think in graphs: `Input → layer(x) → branch/merge → Model(inputs, outputs)`.
- Sequential for lines, Functional for graphs.
- Name layers, check shapes, balance losses.
- Concat grows width; Add keeps shape.
- Shared layers = shared knowledge across branches.

---