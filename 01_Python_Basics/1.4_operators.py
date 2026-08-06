"""
====================================================
Module      : 01 - Python Basics
Lesson      : 04
Topic       : Operators
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# Arithmetic Operators
# ==================================================

num1 = 20
num2 = 5

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)
print("Floor Division :", num1 // num2)
print("Modulus        :", num1 % num2)
print("Exponent       :", num1 ** num2)


# ==================================================
# Comparison Operators
# ==================================================

print("\n========== Comparison Operators ==========")

print("20 == 5 :", num1 == num2)
print("20 != 5 :", num1 != num2)
print("20 > 5  :", num1 > num2)
print("20 < 5  :", num1 < num2)
print("20 >= 5 :", num1 >= num2)
print("20 <= 5 :", num1 <= num2)


# ==================================================
# Logical Operators
# ==================================================

print("\n========== Logical Operators ==========")

age = 22
salary = 50000

print(age > 18 and salary > 30000)
print(age > 25 or salary > 30000)
print(not age > 25)


# ==================================================
# Assignment Operators
# ==================================================

print("\n========== Assignment Operators ==========")

score = 10

score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)


# ==================================================
# Membership Operators
# ==================================================

print("\n========== Membership Operators ==========")

skills = ["Python", "SQL", "Excel"]

print("Python" in skills)
print("Tableau" in skills)
print("Power BI" not in skills)