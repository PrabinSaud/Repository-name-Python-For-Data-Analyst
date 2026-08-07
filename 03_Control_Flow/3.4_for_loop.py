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


# ==========================================
# Topic 5 : While Loop
# ==========================================

# Practice 17
#
# Print numbers from 1 to 10 using a while loop.
count = 1
while count <= 10:
    print(count)
    count += 1

# Practice 18
#
# Print even numbers from 2 to 20 using a while loop.
number = 2
while number <= 20:
    print(number)
    number += 2


# Practice 19
#
# Print numbers from 10 down to 1.
count = 10
while count >= 1:
    print(count)
    count -= 1


# Practice 20
#
# Print the multiplication table of 7.
table = 7
i = 1
while i <= 10:
    print(table, "x", i, "=", table * i)
    i += 1