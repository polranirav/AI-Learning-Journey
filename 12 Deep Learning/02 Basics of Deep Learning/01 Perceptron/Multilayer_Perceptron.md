# 02 — Multilayer Perceptron (MLP)

 **Multilayer Perceptron (MLP)** stacks simple neurons in layers (input → hidden → output). With **nonlinear activations** and **backpropagation**, it learns **curved** decision boundaries and handles problems a single perceptron can’t.

---

## 1) Why do we need an MLP?
- A single perceptron draws only a **straight line** (linear boundary). Many real datasets need **non-linear** boundaries (e.g., XOR, digits, text sentiment).
- **Fix:** add **hidden layers** and **nonlinear activations** (ReLU, Tanh, Sigmoid). Each layer builds slightly better features than the previous one.
- Result: the network can represent complex patterns and generalize better.

---

## 2) Architecture & notation (super simple)
- **Input layer:** holds your features (pixels, tokens, numbers).
- **Hidden layers:** fully connected; each neuron sees all outputs from the previous layer.
- **Output layer:** shape depends on task  
  - Regression: 1 unit (linear)  
  - Binary class: 1 unit (sigmoid)  
  - Multi-class: K units (softmax)
- **Quick shape notation example:** `784 → 128 → 64 → 10` (MNIST image to 10 classes).

---

## 3) Forward pass (how a prediction is made)
For each layer:
1. **Linear mix:** `z = W·a_prev + b`
2. **Nonlinear squish:** `a = activation(z)` (ReLU/Tanh/Sigmoid)
3. Final layer converts to the right form (number, probability, probability vector).

This left-to-right computation is **forward propagation**.

---

## 4) Loss functions (what “wrong” means)
Pick the loss for your task:
- **Regression:** Mean Squared Error (MSE)
- **Binary classification:** Binary Cross-Entropy (with sigmoid)
- **Multi-class classification:** Cross-Entropy (with softmax)

Loss tells the model how far predictions are from truth.

---

## 5) Backpropagation + Gradient Descent (how learning happens)
- **Backpropagation:** efficiently computes **gradients** of the loss w.r.t. all weights by chaining derivatives from output → input.
- **Gradient Descent:** update weights a tiny step **downhill** using those gradients.
- Repeat over many passes (epochs). The network gradually improves.

---

## 6) Tiny training loop (checklist)
1. **Prepare data:** split train/val/test; scale features if needed.  
2. **Choose architecture:** e.g., `input → 128 → 64 → out`.  
3. **Pick activations:** ReLU in hidden layers is a solid default.  
4. **Set loss + optimizer:** BCE/CE/MSE + SGD/Adam.  
5. **Forward pass → compute loss.**  
6. **Backprop → compute gradients.**  
7. **Update weights.**  
8. **Evaluate on validation; tune hyperparameters.**

---

## 7) Practical tips that actually help
- **Initialization:** use sensible weight init (e.g., Xavier/He) to keep signals stable.
- **Regularization:** add **dropout** or **weight decay (L2)** to fight overfitting.
- **Learning rate:** too high explodes, too low crawls; try schedulers and warmup.
- **Batch size:** moderate sizes are often stable; try a few options.
- **Early stopping:** stop when validation stops improving.

---

## 8) Classic starter project
- **MNIST with an MLP:** `784 → 256 → 128 → 10`, ReLU in hidden layers, softmax output, cross-entropy loss, Adam optimizer. It’s the “hello world” of deep learning.

---

## 9) When to use (and not use) an MLP
- **Use MLPs** when inputs are already meaningful vectors (tabular data, simple tasks) or as the **classifier head** on top of features from other models.
- **Prefer CNNs** for images (spatial structure) and **RNNs/Transformers** for sequences (order/time), because they have built-in inductive biases that fit those data types.

---

## Quick recap
- Perceptron too simple → add hidden layers + nonlinearities = **MLP**.  
- **Forward** to predict, **loss** to measure error, **backprop + gradient descent** to learn.  
- Start small, regularize, tune learning rate, and iterate.