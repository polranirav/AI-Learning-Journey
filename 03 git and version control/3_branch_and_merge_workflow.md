# 🌿 Git Branch & Merge – Experiment Like a Pro

This guide explains how to use Git branching to isolate experiments, switch features, and combine results — just like model versioning in AI projects.

---

## 🌱 1. Create and Switch Branches

```bash
# Create a new branch
git branch feature-cnn

# Switch to that branch
git checkout feature-cnn

# Shortcut: create and switch in one step
git checkout -b exp-batch-size-128
```

---

## ✅ 2. See All Branches

```bash
git branch
```

Shows:

```
* feature-cnn
  main
```

The `*` shows your current active branch.

---

## 🔁 3. Merge Branch into Main

```bash
# Step 1: Switch back to main
git checkout main

# Step 2: Merge the experiment branch
git merge feature-cnn
```

This combines changes from `feature-cnn` into `main`.

---

## ⚠️ 4. Resolve Merge Conflicts

Git will show:

```
CONFLICT (content): Merge conflict in model.py
```

Steps to fix:
1. Open the conflicting file and manually resolve the `<<<< HEAD` and `=====` markers
2. After editing, run:

```bash
git add model.py
git commit -m "Resolve merge conflict from feature-cnn"
```

---

## 🤖 AI Engineer Use Case: Branch for Every Experiment

| Branch Name              | Use Case |
|--------------------------|----------|
| `exp-cnn-dropout`        | Try CNN + Dropout |
| `opt-batch-size-128`     | Try different batch size |
| `fix-preprocessing`      | Bug fix on dataset pipeline |
| `langchain-integration`  | Add GenAI model to chatbot |

This helps track which experiment helped or hurt model accuracy.

---

## 🧠 Why Branching Matters in ML

| Action       | ML Impact |
|--------------|-----------|
| `git branch` | Test multiple ideas without breaking working code |
| `git merge`  | Combine good experiments into production |
| Conflicts    | Helps you think clearly about what to keep/change |

---

## 🧪 Example Workflow

```bash
# Create experiment
git checkout -b exp-cnn-relu

# Add new model logic
nano model.py

# Save it
git add model.py
git commit -m "CNN with ReLU instead of Sigmoid"

# Merge back if successful
git checkout main
git merge exp-cnn-relu
```

---

## 🌍 Visual Map

```
main
│
├── exp-cnn-relu (✓ merged)
│
└── exp-dropout       (ongoing...)
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Why use branches? | Safely test features or models without touching main |
| How to switch branches? | `git checkout branch-name` |
| Merge conflict? | Happens when two branches edit the same line differently |
| Best practice? | One branch = one experiment/feature |

---

✅ Branching keeps your AI project organized and fearless — experiment boldly without breaking your base code.

Next → `4 git with ML projects` to track notebooks, experiments, models efficiently.