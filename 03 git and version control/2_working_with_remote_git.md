# 🌍 Git Remote & GitHub – Push, Pull, Clone, SSH

This guide shows how to connect your local Git repo to **GitHub** and work with remotes — ideal for ML engineers who need to:
- Push model updates to GitHub
- Collaborate with teammates
- Showcase public projects or portfolios

---

## ✅ 1. Create a GitHub Repo (Online)

1. Go to: [https://github.com](https://github.com)
2. Click **"New Repository"**
3. Name it (e.g., `my-ml-project`)
4. Do NOT initialize with README (you already have code locally)
5. Click **Create repository**

---

## 🌐 2. Link Local Git to GitHub (Remote)

```bash
# Check you're inside your local project folder
cd my-ml-project

# Add GitHub as remote (replace with your repo URL)
git remote add origin https://github.com/username/my-ml-project.git

# Push local code to GitHub (main branch)
git push -u origin main
```

💡 If your branch is `master`, replace `main` with `master`.

---

## 🔑 3. Set Up SSH for GitHub (Recommended)

### ✅ Step-by-step (One time only):

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### ✅ Copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

1. Copy the full string
2. Go to GitHub → Settings → **SSH and GPG Keys**
3. Click "New SSH Key" → Paste → Save

Now, instead of HTTPS, use:

```bash
git remote set-url origin git@github.com:username/my-ml-project.git
```

---

## 🔁 4. Common Remote Git Commands

| Command | Use |
|---------|-----|
| `git clone [repo_url]` | Download a repo from GitHub |
| `git push origin main` | Upload local commits to GitHub |
| `git pull origin main` | Download latest code from GitHub |
| `git remote -v`        | Check linked remote repo |

---

## 🧠 Real Workflow Example (ML Project)

```bash
# Train new model and save script
python train.py

# Stage & commit
git add train.py
git commit -m "v2: New model with early stopping"

# Push to GitHub
git push origin main
```

✅ Now your team or recruiter can see your latest experiment on GitHub instantly.

---

## 🤖 AI-Specific Use Case: Model Versioning

| Task | Git Usage |
|------|-----------|
| New model architecture | Commit changes with version tags |
| Share results with team | Push to GitHub repo |
| Log performance per commit | Use commit messages with accuracy/loss info |

---

## 💬 Pro Tips

- Use `git clone` to copy someone else’s project
- Use SSH over HTTPS to avoid entering password every time
- Always `git pull` before starting new changes in a team project
- Use `.gitignore` to avoid pushing `models/`, `data/`, or `*.csv`

---

## 📁 Final Project Structure (After Push)

```
my-ml-project/
├── train.py
├── model.py
├── README.md
├── .gitignore
└── .git/           ← Local repo history
```

✅ Online copy lives at:
> https://github.com/username/my-ml-project

---

## 🧪 Interview Q&A

| Question | Answer |
|----------|--------|
| What is `origin`? | A nickname for your GitHub repo (remote) |
| What's `git push`? | Sends your local commits to GitHub |
| Why use SSH instead of HTTPS? | It’s secure and doesn’t ask for your password every time |
| How do you clone a repo? | `git clone <URL>` |

---

🎯 You’ve now mastered Git local + remote setup.

Next → Branching and merging for experiment control. 