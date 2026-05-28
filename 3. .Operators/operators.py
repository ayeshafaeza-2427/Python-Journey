# ==========================================
# Operators in Python
# ==========================================


# ------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------

a = 15
b = 4

print("===== Arithmetic Operators =====")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)

print("\n")


# ------------------------------------------
# 2. Comparison Operators
# ------------------------------------------

print("===== Comparison Operators =====")

print("Equal to:", a == b)
print("Not Equal to:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or Equal to:", a >= b)
print("Less than or Equal to:", a <= b)

print("\n")


# ------------------------------------------
# 3. Logical Operators
# ------------------------------------------

x = True
y = False

print("===== Logical Operators =====")

print("AND Operator:", x and y)
print("OR Operator:", x or y)
print("NOT Operator:", not x)

print("\n")


# ------------------------------------------
# 4. Assignment Operators
# ------------------------------------------

num = 10

print("===== Assignment Operators =====")

print("Initial Value:", num)

num += 5
print("After += :", num)

num -= 3
print("After -= :", num)

num *= 2
print("After *= :", num)

num /= 4
print("After /= :", num)

print("\n")


# ------------------------------------------
# 5. Membership Operators
# ------------------------------------------

language = "Python"

print("===== Membership Operators =====")

print("'P' in language:", "P" in language)
print("'z' not in language:", "z" not in language)

print("\n")


# ------------------------------------------
# 6. Identity Operators
# ------------------------------------------

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("===== Identity Operators =====")

print("list1 is list3:", list1 is list3)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)

print("\n")


# ==========================================
# End of Program
# ==========================================
