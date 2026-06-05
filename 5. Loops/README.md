# 🔄 Python Loops

Loops are used to execute a block of code repeatedly until a specified condition is met. They help reduce code duplication and make programs more efficient.

## 📚 Topics Covered

- For Loop
- While Loop
- Nested Loops
- Break Statement
- Continue Statement
- Pass Statement
- Range Function
- Pattern Programs

---

## 🔹 For Loop

A `for` loop is used to iterate over a sequence such as a list, tuple, string, or range.

### Example

```python
for i in range(5):
    print(i)
```

### Output

```
0
1
2
3
4
```

---

## 🔹 While Loop

A `while` loop executes as long as a condition remains true.

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### Output

```
1
2
3
4
5
```

---

## 🔹 Break Statement

The `break` statement terminates the loop immediately.

### Example

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

### Output

```
1
2
3
4
```

---

## 🔹 Continue Statement

The `continue` statement skips the current iteration and moves to the next one.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```
1
2
4
5
```

---

## 🔹 Pass Statement

The `pass` statement acts as a placeholder and does nothing.

### Example

```python
for i in range(5):
    pass
```

---

## 🔹 Nested Loops

A loop inside another loop is called a nested loop.

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

### Output

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

## 🔹 Pattern Example

```python
for i in range(5):
    print("*" * (i + 1))
```

### Output

```
*
**
***
****
*****
```

---

## 📂 Files in this Folder

| File Name | Description |
|------------|-------------|
| `for_loop.py` | Demonstrates for loops |
| `while_loop.py` | Demonstrates while loops |
| `break_continue_pass.py` | Examples of break, continue, and pass |
| `nested_loops.py` | Nested loop examples |
| `patterns.py` | Pattern printing programs |

---

## 🎯 Learning Outcomes

After completing this section, you will be able to:

- Use `for` and `while` loops effectively.
- Control loop execution using `break`, `continue`, and `pass`.
- Implement nested loops.
- Solve pattern-based programming problems.
- Write efficient repetitive tasks using loops.

---

⭐ If you found this repository helpful, consider giving it a star!
