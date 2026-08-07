"""
====================================================
Module      : 03 - Control Flow
Lesson      : 06
Topic       : Break and Continue
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is break?
# ==================================================

# break immediately stops the loop.


# ==================================================
# Example 1 : break
# ==================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        break
    print(number)


# ==================================================
# Example 2 : continue
# ==================================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        continue
    print(number)


# ==================================================
# Example 3 : break with while
# ==================================================

count = 1

while True:
    print(count)

    if count == 5:
        break

    count += 1


# ==================================================
# Example 4 : continue with while
# ==================================================

count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)


# ==================================================
# Example 5 : Real Data Analyst Example
# ==================================================

sales = [25000, 45000, -1, 50000, 60000]

for sale in sales:

    if sale == -1:
        break

    print("Valid Sale :", sale)