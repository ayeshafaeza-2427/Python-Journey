# Operators in Python

Operators are special symbols used to perform operations on variables and values.

They are used in calculations, comparisons, logical decisions, and many other programming tasks.

Python provides different types of operators.

---

# Types of Operators in Python

1. Arithmetic Operators  
2. Comparison Operators  
3. Logical Operators  
4. Assignment Operators  
5. Membership Operators  
6. Identity Operators  

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning | Example |
|----------|----------|----------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| % | Modulus | 10 % 3 |
| // | Floor Division | 10 // 3 |
| ** | Exponent | 2 ** 3 |

## Example

```python
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
```

---

# 2. Comparison Operators

Comparison operators are used to compare two values.

The result will always be either `True` or `False`.

| Operator | Meaning |
|----------|----------|
| == | Equal to |
| != | Not Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal to |
| <= | Less than or Equal to |

## Example

```python
x = 10
y = 20

print(x == y)
print(x < y)
print(x > y)
```

---

# 3. Logical Operators

Logical operators are used to combine conditions.

| Operator | Meaning |
|----------|----------|
| and | Returns True if both conditions are true |
| or | Returns True if at least one condition is true |
| not | Reverses the result |

## Example

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

---

# 4. Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example |
|----------|----------|
| = | x = 5 |
| += | x += 2 |
| -= | x -= 2 |
| *= | x *= 2 |
| /= | x /= 2 |

## Example

```python
num = 10

num += 5

print(num)
```

---

# 5. Membership Operators

Membership operators are used to check whether a value exists inside a sequence.

| Operator | Meaning |
|----------|----------|
| in | Returns True if value exists |
| not in | Returns True if value does not exist |

## Example

```python
language = "Python"

print("P" in language)
print("z" not in language)
```

---

# 6. Identity Operators

Identity operators are used to compare memory locations of two objects.

| Operator | Meaning |
|----------|----------|
| is | Returns True if both objects are same |
| is not | Returns True if both objects are different |

## Example

```python
x = [1, 2]
y = x

print(x is y)
print(x is not y)
```

---

# Conclusion

Operators are one of the most important concepts in Python.

They help programmers perform calculations, compare values, check conditions, and control program logic efficiently.
