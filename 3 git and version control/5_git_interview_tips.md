# 🎯 Git Interview Tips & Command Review (For AI/ML Engineers)

This cheat sheet helps you **revise Git quickly before interviews** — especially when asked about collaboration, versioning, or ML workflow management.

---

## 💬 Top Git Interview Questions (With Answers)

### 1. What's the difference between `git clone` and `git init`?

**Answer:**
- `git init` → Initializes a new local repo from scratch.
- `git clone` → Copies an existing repo (from GitHub, GitLab, etc.).

---

### 2. What is a commit?

**Answer:**
A snapshot of your code at a point in time. You can go back to it later.

---

### 3. How does `git add` differ from `git commit`?

**Answer:**
- `git add` → Stages changes (prepares them).
- `git commit` → Saves the staged changes to your history.

---

### 4. How to undo your last commit?

```bash
git reset --soft HEAD~1    # Undo commit but keep code
git reset --hard HEAD~1    # Undo & delete changes (⚠️ permanent)
```

---

### 5. What is a branch?

**Answer:**
A branch is a copy of your code used to test features or experiments **without breaking the main version**.

---

### 6. How do you merge branches?

```bash
git checkout main
git merge feature-branch
```

---

### 7. What’s a merge conflict?

**Answer:**
When two branches edit the same line differently. Git can’t decide which version to keep — you resolve it manually.

---

### 8. How do you track only specific files?

```bash
git add script.py         # Only adds one file
git commit -m "Track model script changes"
```

---

### 9. What is `.gitignore` and why is it important?

**Answer:**
A file listing paths Git should ignore — useful to exclude `models/`, `data/`, and auto-saved notebooks in ML.

---

### 10. Can you use Git for Jupyter Notebooks?

**Answer:**
Yes, but output cells can clutter diffs. Use:
- `.gitignore` to skip checkpoints
- `nbstripout` to clean outputs before commits

---

## 🔑 Most Used Git Commands (Quick Recap)

```bash
# Start and connect
git init
git clone <url>
git remote add origin <url>

# Track changes
git status
git add .
git commit -m "Message"

# Undo or inspect
git diff
git reset --soft HEAD~1
git log --oneline

# Remote
git push origin main
git pull origin main

# Branching
git branch new-exp
git checkout new-exp
git merge new-exp
```

---

## 🧠 AI/ML Use Case Table

| Git Concept  | ML/AI Project Example |
|--------------|------------------------|
| Commit       | Log model version w/ accuracy |
| Branch       | Try new model architecture (CNN, transformer) |
| Tag          | Save best-performing version |
| Diff         | Compare feature engineering strategies |
| Ignore       | Exclude `data/` and `models/` |
| Merge        | Combine team contributions into `main` |

---

## 🧪 Real Interview Tips

- ✅ Show how you use Git **per experiment**
- ✅ Mention `.gitignore` to avoid uploading weights/data
- ✅ Say you commit: code, configs, hyperparameters — **not models**
- ✅ Talk about tags (`v1.0-best`) and branches (`exp-transformer`)
- ✅ Add GitHub repo to your resume/portfolio

---

🎉 You’re now 100% interview-ready with Git + ML!

Next Step → Head into **SQL, Pandas, Numpy**, or **ML training pipelines**