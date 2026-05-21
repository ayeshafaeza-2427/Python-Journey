# Variables in Python

## Introduction

Variables are one of the most important concepts in Python.  
A variable is used to store data or information that can be used later in a program.

Think of a variable like a container that stores values.

Example:
```python
name = "AYESHA"
```

Here:
- `name` → variable name
- `"AYESHA"` → value stored inside the variable

---

# Why Do We Use Variables?

Variables help us:
- store information
- reuse values
- make programs dynamic
- avoid writing the same data again and again

Example:
```python
name = "AYESHA"

print(name)
print("Welcome", name)
```

Output:
```python
AYESHA
Welcome AYESHA
```

---

# Creating Variables in Python

Python automatically creates a variable when you assign a value using `=`.

Syntax:
```python
variable_name = value
```

Example:
```python
student_name = "AYESHA"
age = 18
height = 5.4
is_student = True
```

---

# Types of Variables

## 1. String (Text)

Strings are used to store text.

Example:
```python
name = "AYESHA"
city = "Hyderabad"
```

---

## 2. Integer (Whole Numbers)

Integers are numbers without decimal points.

Example:
```python
age = 18
year = 2026
```

---

## 3. Float (Decimal Numbers)

Floats contain decimal values.

Example:
```python
height = 5.4
temperature = 36.7
```

---

## 4. Boolean (True or False)

Boolean values represent only:
- True
- False

Example:
```python
is_student = True
is_logged_in = False
```

---

# Rules for Naming Variables

## ✅ Allowed
- letters
- numbers
- underscore (_)

Examples:
```python
user_name = "AYESHA"
age1 = 18
student_city = "Hyderabad"
```

---

## ❌ Not Allowed

### Cannot start with a number
```python
1name = "AYESHA"
```

### Cannot contain spaces
```python
student name = "AYESHA"
```

### Cannot use special symbols
```python
name@ = "AYESHA"
```

---

# Python is Case Sensitive

Python treats uppercase and lowercase letters differently.

Example:
```python
name = "AYESHA"
Name = "Python"
```

These are considered two different variables.

---

# Printing Variables

We use `print()` to display variables.

Example:
```python
name = "AYESHA"
age = 18

print(name)
print(age)
```

Output:
```python
AYESHA
18
```

---

# Printing Multiple Variables

Example:
```python
name = "AYESHA"
city = "Hyderabad"

print(name, city)
```

Output:
```python
AYESHA Hyderabad
```

---

# Checking Variable Type

We use `type()` to check the datatype of a variable.

Example:
```python
name = "AYESHA"
age = 18

print(type(name))
print(type(age))
```

Output:
```python
<class 'str'>
<class 'int'>
```

---

# Taking User Input

Python can take input from users using `input()`.

Example:
```python
name = input("Enter your name: ")

print("Welcome", name)
```

---

# Mini Practice Program

```python
name = "AYESHA"
age = 18
college = "Engineering College"

print("Student Name:", name)
print("Age:", age)
print("College:", college)
```

Output:
```python
Student Name: AYESHA
Age: 18
College: Engineering College
```

---

# Summary

In this file, we learned:
- what variables are
- why variables are used
- types of variables
- rules for naming variables
- printing variables
- taking user input

Variables are the foundation of programming and are used in almost every Python project.
