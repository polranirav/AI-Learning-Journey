# 🤖 Git for AI/ML Projects – Practical Setup

Git isn’t just for developers — AI engineers use it to:
- Version training scripts
- Track hyperparameter changes
- Avoid uploading large models/datasets

---

## 🧠 Recommended Folder Structure

```
my-ml-project/
├── data/               # Raw or preprocessed datasets
├── models/             # Saved model files (.h5, .pt)
├── notebooks/          # Jupyter notebooks
├── src/                # Python scripts
├── outputs/            # Logs, metrics, charts
├── .gitignore          # Prevents tracking large/binary files
└── README.md
```

---

## 🚫 Use `.gitignore` to Exclude Heavy Stuff

```bash
touch .gitignore
```

Inside `.gitignore`, add:

```
# Data and model artifacts
data/
models/
*.csv
*.h5
*.pt

# Jupyter outputs and caches
.ipynb_checkpoints/
__pycache__/
*.log
```

Then commit:

```bash
git add .gitignore
git commit -m "Ignore data, models, and notebook outputs"
```

---

## 📜 Versioning Experiments (Tips)

| Tip | What to Do |
|-----|-------------|
| Each experiment | Use `git commit -m "Try lr=0.01, batch=64"` |
| Save metrics | Log accuracy/loss in a `.txt` or `.json` |
| Tag best runs | `git tag v1.0-best-model` |
| Compare runs | Use `git diff HEAD~1 HEAD` on scripts |

---

## 🧪 Example: Commit Only What's Needed

```bash
git add src/train_model.py
git commit -m "v3: Added dropout and changed activation to ReLU"
```

Don’t add model weights or datasets unless small and reproducible.

---

## ✅ Best Practices for AI Teams

| Practice | Benefit |
|----------|---------|
| Ignore raw data and weights | Save repo space |
| Commit scripts & configs only | Reproduce runs easily |
| Tag best versions | Easy rollback and deployment |
| Use `README.md` | Describe model goals and metrics |

---

## 🔥 Bonus: Use Branches for Experiments

- `exp-transformer-finetune`
- `test-batch-size-128`
- `langchain-pipeline`

Each branch = 1 model idea. Merge if it works.

---

## 📁 Real Git History (AI Dev Example)

```
✔️ v1: Base logistic regression
✔️ v2: Add preprocessing + normalize
✔️ v3: Change to Random Forest
✔️ v4: Reduce overfitting, add dropout
✔️ v5: Fine-tuned hyperparameters
🏷  v5.1-best: Achieved 91% accuracy
```

---

## 💬 Interview Q&A

| Question | Answer |
|----------|--------|
| Should you push datasets to Git? | No — use `.gitignore` or data versioning tools (like DVC) |
| How to track model evolution? | Commit scripts, tag best versions |
| Where to store weights/models? | Outside Git, or use cloud storage (e.g., Hugging Face Hub, S3) |
| Why ignore `.ipynb_checkpoints`? | They clutter your repo with auto-saves |

---

✅ Git + ML = clean, trackable, reproducible experiments.  
Your repo becomes a living portfolio of your model journey.

Next → Final topic: `5 git interview tips & commands review`