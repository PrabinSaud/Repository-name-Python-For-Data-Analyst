"""
====================================================
Module      : 03 - Control Flow
Lesson      : 02
Topic       : If Else Statement
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is an If Else Statement?
# ==================================================

# If the condition is True, the if block executes.
# Otherwise, the else block executes.


# ==================================================
# Example 1 : Pass or Fail
# ==================================================

marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# ==================================================
# Example 2 : Adult or Minor
# ==================================================

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ==================================================
# Example 3 : Even or Odd
# ==================================================

number = 15

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==================================================
# Example 4 : Positive or Negative
# ==================================================

temperature = -5

if temperature >= 0:
    print("Positive")
else:
    print("Negative")


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

sales = 45000
target = 50000

if sales >= target:
    print("Target Achieved")
else:
    print("Target Missed")