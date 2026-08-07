"""
====================================================
Module      : 03 - Control Flow
Lesson      : 05
Topic       : While Loop
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a While Loop?
# ==================================================

# A while loop repeats a block of code
# as long as the condition is True.


# ==================================================
# Example 1 : Print Numbers
# ==================================================

count = 1

while count <= 5:
    print(count)
    count += 1


# ==================================================
# Example 2 : Print Even Numbers
# ==================================================

number = 2

while number <= 10:
    print(number)
    number += 2


# ==================================================
# Example 3 : Countdown
# ==================================================

count = 5

while count >= 1:
    print(count)
    count -= 1


# ==================================================
# Example 4 : Multiplication Table
# ==================================================

table = 5
i = 1

while i <= 10:
    print(table, "x", i, "=", table * i)
    i += 1


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

sales = [25000, 35000, 42000, 50000]

index = 0

while index < len(sales):
    print(sales[index])
    index += 1