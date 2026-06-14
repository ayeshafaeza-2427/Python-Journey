# Data Types in Python
 
## Introduction

Data types define the type of value a variable can store in Python.

Python provides different built-in data types to store numbers, text, and logical values.

Understanding data types is important because they help us perform operations correctly in a program.

---

# Main Data Types in Python

## 1. Integer (int)

Integers are whole numbers without decimal points.

### Examples

```python
age = 19
marks = 95
year = 2025
```

### Output

```python
18
95
2025
```

---

## 2. Float (float)

Float data types are numbers with decimal points.

### Examples

```python
height = 5.7
price = 99.99
temperature = 36.5
```

### Output

```python
5.7
99.99
36.5
```

---

## 3. String (str)

Strings are used to store text data.

Strings are written inside single quotes (' ') or double quotes (" ").

### Examples

```python
name = "Ayesha"
city = "Hyderabad"
course = "Python"
```

### Output

```python
Ayesha
Hyderabad
Python
```

---

## 4. Boolean (bool)

Boolean values represent either True or False.

They are mainly used in conditions and decision making.

### Examples

```python
is_student = True
is_logged_in = False
```

### Output

```python
True
False
```

---

# Type Checking in Python

Python provides the `type()` function to check the data type of a variable.

### Example

```python
name = "Ayesha"
age = 18

print(type(name))
print(type(age))
```

### Output

```python
<class 'str'>
<class 'int'>
```

---

# Type Conversion

Type conversion means changing one data type into another.

Python provides built-in functions for conversion.

## Integer Conversion

```python
age = "18"
converted_age = int(age)

print(converted_age)
```

---

## String Conversion

```python
number = 100
converted_number = str(number)

print(converted_number)
```

---

## Float Conversion

```python
value = "5.5"
converted_value = float(value)

print(converted_value)
```

---

# Complete Example

```python
name = "Ayesha"
age = 18
height = 5.7
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

---

# Conclusion

Data types are one of the most important concepts in Python programming.

They help Python understand:
- what kind of data is stored
- how the data should behave
- what operations can be performed on it

Learning data types is the foundation for writing Python programs.
