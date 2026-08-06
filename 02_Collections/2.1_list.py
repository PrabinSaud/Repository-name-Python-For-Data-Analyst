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

# ==================================================
# Example 9 : insert()
# ==================================================

fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print("After Insert :", fruits)


# ==================================================
# Example 10 : extend()
# ==================================================

frontend = ["HTML", "CSS"]
backend = ["Python", "SQL"]

frontend.extend(backend)

print("After Extend :", frontend)


# ==================================================
# Example 11 : pop()
# ==================================================

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed :", removed)
print("Updated :", numbers)


# ==================================================
# Example 12 : clear()
# ==================================================

cities = ["Delhi", "Mumbai", "Chennai"]

cities.clear()

print("After Clear :", cities)


# ==================================================
# Example 13 : sort()
# ==================================================

marks = [85, 60, 95, 72, 90]

marks.sort()

print("Sorted :", marks)


# ==================================================
# Example 14 : reverse()
# ==================================================

marks.reverse()

print("Reverse :", marks)


# ==================================================
# Example 15 : copy()
# ==================================================

original = ["Python", "SQL"]

copied = original.copy()

print("Original :", original)
print("Copied   :", copied)