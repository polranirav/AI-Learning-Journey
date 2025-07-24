# 🧱 Git Basics for AI Engineers (Full Cheat Sheet)

This guide covers everything you need to manage your ML/AI project with Git — from initialization to experiment tracking.

---

## 🗂️ 1. Initialize Git in Your Project

```bash
# Step 1: Create a new folder
mkdir my-ai-project
cd my-ai-project

# Step 2: Initialize Git
git init

# Step 3: Create a script
echo "print('Hello AI')" > hello.py

# Step 4: Track the file
git add hello.py

# Step 5: Make your first commit
git commit -m "Initial commit: Hello AI program"
```

---

## 🔍 2. Check What’s Going On

```bash
# See which files changed or are untracked
git status

# View commit history
git log

# Cleaner view of history (one line per commit)
git log --oneline
```

🧠 Example Output:

```
c2198e3 Add dropout to improve accuracy
b0a81dd Fix feature scaling bug
a1b4d90 Initial commit
```

---

## 🔁 3. See and Undo Changes

### 🔸 See what’s changed before committing:

```bash
git diff              # Unstaged changes
git diff --staged     # Changes staged with git add
```

### 🔸 Undo changes safely:

```bash
git restore filename.py              # Undo file changes
git reset HEAD filename.py           # Unstage a file
git reset --soft HEAD~1              # Undo last commit (keep changes)
git reset --hard HEAD~1              # Undo and discard changes ❗ (careful)
```

---

## 🚫 4. Ignore Files (e.g., models, datasets, notebooks)

```bash
# Create .gitignore
touch .gitignore
```

Inside `.gitignore`, add:

```
__pycache__/
*.csv
*.h5
*.pt
dataset/
.ipynb_checkpoints/
secrets.env
```

Then run:

```bash
git add .gitignore
git commit -m "Add .gitignore to exclude data/models"
```

---

## 🤖 AI/ML-Specific Use Cases

| Git Command         | AI/ML Project Use |
|---------------------|------------------|
| `git init`          | Begin tracking your ML repo |
| `git add`           | Stage only your model/code (not dataset) |
| `git commit`        | Save checkpoints after major model updates |
| `git log`           | Review what change improved accuracy |
| `git diff`          | Debug why accuracy dropped (code diff) |
| `.gitignore`        | Exclude raw datasets or logs |
| `reset --soft`      | Undo bad experiments without losing code |

---

## 🧠 Real Workflow Example

```bash
# 1. You added a CNN layer
nano model.py

# 2. Check changes
git status

# 3. Stage and commit
git add model.py
git commit -m "v2: Add CNN with ReLU"

# 4. Later, compare with previous version
git diff HEAD~1 HEAD
```

---

## 💡 Pro Tips

- Use `git log --oneline` to track your experiment history
- Keep `.gitignore` clean — don’t upload huge files or secrets
- Use meaningful commit messages:  
  ✅ "Fix scaler bug in preprocessing"  
  ✅ "Try batch size 64 — accuracy +3%"  
- Use `git reset --soft HEAD~1` if you committed too early

---

## 📁 Folder Recap After Setup

```
my-ai-project/
├── .git/                  # Git metadata
├── hello.py               # Tracked code
├── model.py               # Your model file
├── .gitignore             # Prevents accidental big file tracking
```

---

## 🧪 Interview-Ready One-Liners

| Question | Answer |
|----------|--------|
| What does `git init` do? | Creates a .git folder to start version control |
| Difference between `add` and `commit`? | `add` stages, `commit` saves |
| Undo last commit but keep code? | `git reset --soft HEAD~1` |
| See commit history? | `git log` or `git log --oneline` |
| Ignore files from Git? | Add rules in `.gitignore` |

---

✅ This file gives you 100% control over your project — version your models, experiments, and scripts like a pro.

Next up → `2 working with remote` to push to GitHub and work in teams.