"""
====================================================
Module      : 03 - Control Flow
Lesson      : 04
Topic       : For Loop
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a For Loop?
# ==================================================

# A for loop repeats a block of code for each item
# in a collection.


# ==================================================
# Example 1 : Print Numbers
# ==================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# ==================================================
# Example 2 : Student Names
# ==================================================

students = ["Rahul", "Amit", "Neha", "Prawin"]

for student in students:
    print(student)


# ==================================================
# Example 3 : Sales
# ==================================================

sales = [25000, 28000, 31000, 35000]

for sale in sales:
    print("Monthly Sale :", sale)


# ==================================================
# Example 4 : Multiply by 2
# ==================================================

numbers = [5, 10, 15, 20]

for number in numbers:
    print(number * 2)


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

monthly_sales = [45000, 52000, 38000, 61000]

for sale in monthly_sales:
    if sale >= 50000:
        print("Target Achieved :", sale)