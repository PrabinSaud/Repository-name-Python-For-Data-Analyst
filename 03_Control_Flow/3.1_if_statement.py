"""
====================================================
Module      : 03 - Control Flow
Lesson      : 01
Topic       : If Statement
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is an If Statement?
# ==================================================

# An if statement executes code only when a condition is True.


# ==================================================
# Example 1 : Simple If
# ==================================================

age = 20

if age >= 18:
    print("Eligible to Vote")


# ==================================================
# Example 2 : Marks
# ==================================================

marks = 78

if marks >= 40:
    print("Pass")


# ==================================================
# Example 3 : Salary
# ==================================================

salary = 55000

if salary > 50000:
    print("High Salary")


# ==================================================
# Example 4 : Membership
# ==================================================

skills = ["Python", "SQL", "Excel"]

if "Python" in skills:
    print("Python Found")


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

sales = 65000
target = 50000

if sales >= target:
    print("Target Achieved")