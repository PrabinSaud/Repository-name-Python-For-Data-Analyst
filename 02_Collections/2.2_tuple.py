"""
====================================================
Module      : 02 - Collections
Lesson      : 02
Topic       : Tuples
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a Tuple?
# ==================================================

# A tuple stores multiple values in a single variable.
# Tuples are ordered, immutable, and allow duplicate values.


# ==================================================
# Example 1 : Creating a Tuple
# ==================================================

fruits = ("Apple", "Banana", "Mango")

print("Fruits :", fruits)


# ==================================================
# Example 2 : Different Data Types
# ==================================================

student = ("Rahul", 21, 8.45, True)

print("Student :", student)


# ==================================================
# Example 3 : Accessing Elements
# ==================================================

print("First Fruit :", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit  :", fruits[-1])


# ==================================================
# Example 4 : Tuple Length
# ==================================================

print("Total Fruits :", len(fruits))


# ==================================================
# Example 5 : count()
# ==================================================

numbers = (10, 20, 10, 30, 10)

print("Count of 10 :", numbers.count(10))


# ==================================================
# Example 6 : index()
# ==================================================

print("Index of 30 :", numbers.index(30))


# ==================================================
# Example 7 : Packing
# ==================================================

employee = ("Amit", "Finance", 55000)

print("Employee :", employee)


# ==================================================
# Example 8 : Unpacking
# ==================================================

name, department, salary = employee

print("Name       :", name)
print("Department :", department)
print("Salary     :", salary)