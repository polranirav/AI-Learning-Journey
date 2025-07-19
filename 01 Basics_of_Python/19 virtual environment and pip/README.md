# 🧠 Python: Virtual Environment and pip

This folder covers how to manage **isolated Python environments** and install project-specific libraries using `pip`.

Virtual environments are **essential** for AI/ML workflows to:
- Avoid dependency conflicts between projects
- Freeze & share environments (`requirements.txt`)
- Run the same code reliably across devices (macOS, Windows, Linux)

---

## 📌 Files in This Folder

### 1. 🌐 Virtual Environment Setup

#### ✅ macOS/Linux:
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

#### ✅ Windows:
```bat
:: Create virtual environment
python -m venv venv

:: Activate it
venv\Scripts\activate
```

💡 Activating the virtual environment is required before installing or running any libraries.

---

### 2. `3_install_and_upgrade_pip.py`

Covers:
- How to install and upgrade pip packages

```python
pip install --upgrade pip
pip install numpy pandas matplotlib
```

💡 Install only the packages you need — this avoids cluttering the project.

---

### 3. `4_freeze_requirements.sh`

```bash
pip freeze > requirements.txt
```

💡 Save your full environment so others (or future-you) can recreate it exactly.

---

### 4. `5_install_from_requirements.sh`

```bash
pip install -r requirements.txt
```

💡 Rebuild the same environment on any system with one command.

---

### 5. `6_check_installed_packages.py`

```python
# View installed packages
import pkg_resources

for dist in pkg_resources.working_set:
    print(f"{dist.project_name}=={dist.version}")
```

💡 Useful to double-check what’s really installed — especially before deployment.

---

### 6. `7_delete_virtualenv_instructions.txt`

#### ✅ macOS/Linux:
```bash
deactivate
rm -rf venv/
```

#### ✅ Windows:
```bat
deactivate
rmdir /S /Q venv
```

💡 This removes the isolated environment without touching your system Python.

---

## 🎯 Real-World Relevance in AI/ML

| Tool     | Use Case |
|----------|----------|
| `venv`   | Keeps each ML project isolated |
| `pip`    | Install training libs like `scikit-learn`, `xgboost`, `torch` |
| `requirements.txt` | Share & deploy same setup to cloud or colleagues |
| `deactivate` | Exit project safely without affecting system packages |

---

## 🧠 Interview Questions to Practice

1. Why use virtual environments in ML workflows?
2. How do you freeze and share your Python dependencies?
3. How do you activate and deactivate environments on both OS types?

---

## ✅ Tip

> Every new project = new virtual environment. This keeps dependencies clean, reproducible, and safe to deploy or share.

---

📁 **Next Topic:** [20 working with JSON and XML →](../20 working with JSON and XML/)