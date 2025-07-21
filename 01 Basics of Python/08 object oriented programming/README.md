# 🧠 Basics of Python: Object-Oriented Programming (OOP)

This folder introduces **Object-Oriented Programming (OOP)** — a powerful way to organize code using classes and objects. OOP is heavily used in AI/ML frameworks to create reusable, scalable, and modular code (e.g., models, datasets, training pipelines).

---

## 📌 Programs in This Folder

### 1. `1_class_and_object.py`

Covers:
- Creating a class
- Instantiating an object

Example:
```python
class Dog:
    pass

my_dog = Dog()
```

💡 A class is a blueprint; an object is an actual instance of that blueprint.

---

### 2. `2_init_and_self.py`

Covers:
- `__init__()` constructor
- `self` for instance-level data

Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name
```

💡 `__init__` runs automatically when you create an object.

---

### 3. `3_instance_vs_class_variable.py`

Covers:
- Class variables (shared)
- Instance variables (object-specific)

Example:
```python
class Robot:
    category = "AI Machine"
```

---

### 4. `4_class_methods.py`

Covers:
- Adding custom methods

Example:
```python
def square(self):
    return self.value ** 2
```

💡 Methods define what objects can do — like `.train()`, `.predict()` in ML models.

---

### 5. `5_inheritance_basics.py`

Covers:
- Inheriting methods from a parent class

Example:
```python
class Dog(Animal):
    def bark(self):
        ...
```

💡 Reuse code from base classes (just like in PyTorch: `nn.Module`)

---

### 6. `6_method_overriding.py`

Covers:
- Redefining a parent method in a child class

Example:
```python
def train(self):
    print("Custom model training...")
```

---

### 7. `7_str_and_repr_methods.py`

Covers:
- Human-readable and debug-friendly object printing

Example:
```python
def __str__(self):
    return "Readable version"
```

---

### 8. `8_encapsulation.py`

Covers:
- Restricting access to variables/methods
- `_protected` and `__private` convention

Example:
```python
self.__pin = "1234"
```

---

### 9. `9_abstraction_basics.py`

Covers:
- Abstract classes with `ABC` and `@abstractmethod`
- Hiding internal logic, enforcing structure

Example:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        ...
```

💡 Common in frameworks where a base class requires child classes to implement specific methods.

---

### 10. `10_custom_dataset_class.py`

Covers:
- Simulating a real dataset class like in PyTorch

Example:
```python
def __getitem__(self, index):
    return self.data[index]
```

💡 AI/ML frameworks use classes to load and process datasets.

---

### 11. `11_ai_model_class_example.py`

Covers:
- Simulated ML model with `.train()` and `.predict()` methods

Example:
```python
class SimpleModel:
    def train(self):
        ...
```

💡 All AI models are created using OOP structure.

---

## 🎯 Real-World Relevance in AI/ML

| OOP Concept      | Use Case in AI/ML                    |
|------------------|--------------------------------------|
| Class/Object     | Models, Datasets, Trainers           |
| Inheritance      | Reuse base model or trainer logic    |
| Encapsulation    | Hide internal logic or parameters    |
| Abstraction      | Define required structure (like `fit`) |
| `__str__`, `__repr__` | Logging, debugging, readable output |

---

## 🧠 Interview Questions to Practice

1. What is the difference between a class and an object?
2. How does `__init__()` work?
3. What is the difference between class and instance variables?
4. What is abstraction, and how is it implemented in Python?
5. Why do we use `self` inside methods?

---

## ✅ Tip

> OOP becomes powerful when combined with AI.  
> Your model, data pipeline, loss function — all can be cleanly separated using classes.

---

📁 **Next Topic:** [9 file handling and modules →](../09%20file%20handling%20and%20modules/)