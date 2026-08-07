"""
====================================================
Module      : 03 - Control Flow
Lesson      : 03
Topic       : Elif Statement
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is Elif?
# ==================================================

# elif allows Python to check multiple conditions.


# ==================================================
# Example 1 : Student Grades
# ==================================================

marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")


# ==================================================
# Example 2 : Age Category
# ==================================================

age = 15

if age >= 60:
    print("Senior Citizen")

elif age >= 18:
    print("Adult")

elif age >= 13:
    print("Teenager")

else:
    print("Child")


# ==================================================
# Example 3 : Salary Category
# ==================================================

salary = 42000

if salary >= 100000:
    print("High Salary")

elif salary >= 50000:
    print("Medium Salary")

else:
    print("Low Salary")


# ==================================================
# Example 4 : Discount
# ==================================================

purchase = 7500

if purchase >= 10000:
    print("20% Discount")

elif purchase >= 5000:
    print("10% Discount")

else:
    print("No Discount")


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

sales = 72000

if sales >= 100000:
    print("Excellent Performance")

elif sales >= 70000:
    print("Good Performance")

elif sales >= 50000:
    print("Average Performance")

else:
    print("Needs Improvement")