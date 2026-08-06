"""
====================================================
Module      : 02 - Collections
Lesson      : 01
Topic       : Lists
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a List?
# ==================================================

# A list stores multiple values in a single variable.
# Lists are ordered, mutable, and allow duplicate values.


# ==================================================
# Example 1 : Creating a List
# ==================================================

fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# ==================================================
# Example 2 : Accessing Elements
# ==================================================

print("First Fruit :", fruits[0])
print("Last Fruit  :", fruits[-1])


# ==================================================
# Example 3 : Updating a List
# ==================================================

fruits[1] = "Orange"

print(fruits)


# ==================================================
# Example 4 : Adding Elements
# ==================================================

fruits.append("Grapes")

print(fruits)


# ==================================================
# Example 5 : Removing Elements
# ==================================================

fruits.remove("Apple")

print(fruits)


# ==================================================
# Example 6 : List Length
# ==================================================

print("Total Fruits :", len(fruits))


# ==================================================
# Example 7 : Real Data Analyst Example
# ==================================================

monthly_sales = [25000, 28000, 31000, 29500]

print("Monthly Sales :", monthly_sales)