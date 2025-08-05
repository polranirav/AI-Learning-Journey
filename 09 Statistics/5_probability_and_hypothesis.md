# 🎲 5. Probability & Hypothesis – Statistical Thinking for AI Decisions

This folder introduces you to **probability theory and hypothesis testing** — essential tools for reasoning under uncertainty in AI. These concepts are used in algorithms like Naive Bayes, decision trees, AB testing, and model evaluation.

---

## 📁 Files in This Folder

### `1_probability_basics.py`

Covers:
- Simple probability formula: `P(A) = favorable / total`
- Coin toss, dice, card deck examples
- Experimental vs theoretical probability

Used in:
- Estimating likelihood of events in ML
- Sampling strategies and noise modeling

---

### `2_union_vs_intersection.py`

Covers:
- Probability of A or B: `P(A ∪ B)`
- Probability of A and B: `P(A ∩ B)`
- Venn diagram logic and `p(A) + p(B) - p(A and B)`

Used in:
- Handling multiple features
- Probabilistic modeling (e.g. Naive Bayes)

---

### `3_conditional_independent_events.py`

Covers:
- Conditional probability: `P(A|B)`
- Independence rule: `P(A ∩ B) = P(A) * P(B)`
- Event dependence in real-world examples

Used in:
- Naive Bayes assumptions
- Causal inference and event modeling

---

### `4_hypothesis_testing.py`

Covers:
- Null vs Alternate Hypothesis
- p-value, confidence interval
- Type I/II errors, statistical significance

Used in:
- A/B testing for ML product decisions
- Evaluating fairness and performance claims

---

### `5_bayes_theorem.py`

Covers:
- `P(A|B) = P(B|A) * P(A) / P(B)`
- Real-world inference scenarios
- Prior, likelihood, posterior intuition

Used in:
- Naive Bayes classifier
- Updating belief systems in AI agents

---

## 🧠 Real-World AI/ML Relevance

| Concept                | Use Case in AI/ML                      |
|------------------------|----------------------------------------|
| Conditional Probability | Bayes classifier, sequence modeling   |
| Hypothesis Testing     | A/B tests for model & UI experiments   |
| Bayes Theorem          | Updating predictions, prior knowledge |
| Event Independence     | Naive Bayes, probabilistic assumptions |

---

## 💬 Interview Questions

1. What’s the difference between conditional probability and joint probability?
2. Explain Bayes’ theorem and its use in ML.
3. How do you interpret a p-value?
4. What are Type I and Type II errors?

---

## ✅ Tip

> Always define your **null hypothesis clearly** before running an experiment — it frames how you interpret results and p-values.