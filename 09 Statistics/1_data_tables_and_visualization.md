# 📊 1_data_tables_and_visualization.md

This file introduces foundational concepts in **statistical data representation** and **visualization** — essential for interpreting datasets before applying AI/ML techniques. From one-way tables to pie charts and histograms, these tools help you understand **distribution**, **categories**, and **trends** in your data.

---

## 📌 Topics Covered

- One-Way Tables
- Bar Graphs
- Pie Charts
- Line Graphs
- Two-Way Tables
- Dot Plots
- Frequency Tables

---

## 📋 One-Way Table

A **one-way table** organizes data by counting individuals that fall into specific categories of a single variable.

| Name    | Age |
|---------|-----|
| Akarsh  | 22  |
| Sarthak | 23  |
| Harsh   | 24  |

- "Name" = Individual
- "Age" = Variable

> If there are multiple variables (e.g., Age, Salary, Gender), it's still a one-way table if we ask only **one counter question**: *“What is the [value] of [person]?”*

---

## 📊 Bar Graph

Used for categorical data (like fruits, genders, etc.).

| Person | Fruit  |
|--------|--------|
| A      | Apple  |
| B      | Banana |
| C      | Apple  |

First, build a frequency table:

| Fruit  | Count |
|--------|-------|
| Apple  | 2     |
| Banana | 1     |

Then, plot using bars. Useful for:
- Survey data
- Comparing class counts
- Categorical target distribution

---

## 🥧 Pie Chart

Used to represent **percentage breakdown** of categories.

Example frequency:

| Fruit  | Count | %
|--------|-------|------|
| Apple  | 6     | 42.9 |
| Banana | 4     | 28.6 |
| Kiwi   | 2     | 14.3 |
| Mango  | 2     | 14.3 |

Good for:
- Visualizing proportions
- Comparing categorical labels in ML datasets

---

## 📈 Line Graph

Used for **trends over time** or **continuous variables**.

Example: Monthly expense

| Month | Expense |
|-------|---------|
| Jan   | 10k     |
| Feb   | 12k     |
| Mar   | 18k     |

> More suitable than bar graphs when **order or sequence** matters (e.g., time-series forecasting).

---

## 📑 Two-Way Table

Used when two variables interact.

| Month | Revenue |
|-------|---------|
| Jan   | 50k     |
| Mar   | 80k     |

Expanded for multiple years:

| Month | 2020 | 2021 | 2022 | Total |
|-------|------|------|------|-------|
| Jan   | 5k   | 10k  | 15k  | 30k   |
| Mar   | 10k  | 20k  | 50k  | 80k   |

> Helps explore **relationships between two variables**, such as class vs gender, model vs time, etc.

---

## 📌 Dot Plot

Simplified version of bar graph — stacks dots instead of bars.

| Age Group | Members |
|-----------|---------|
| 10–20     | 5       |
| 20–30     | 8       |
| 30–40     | 12      |

Useful for:
- Educational stats
- Quick visual of spread
- Intro to histograms

---

## 📦 In ML/AI Context:

| Visualization Tool | Use Case in AI |
|--------------------|----------------|
| One-Way Table       | Analyze individual features |
| Bar Graph           | Categorical label distribution |
| Pie Chart           | Class imbalance visualization |
| Line Graph          | Time-series data trends |
| Two-Way Table       | Feature interactions (e.g. feature vs class) |
| Dot Plot            | Understand small-sample feature frequencies |

---

## 💬 Interview Questions

1. When do you use a one-way vs two-way table?
2. What's the advantage of a line graph over a bar graph?
3. How is a dot plot different from a histogram?

---

📁 **Next File:** `2_range_and_iqr.md`