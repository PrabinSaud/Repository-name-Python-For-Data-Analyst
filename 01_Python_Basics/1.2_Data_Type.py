"""
====================================================
Module      : 01 - Python Basics
Lesson      : 02
Topic       : Data Types
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What are Data Types?
# ==================================================

# Data types tell Python what kind of value a variable stores.


# ==================================================
# Example 1 : Integer (int)
# ==================================================

age = 21

print("Age:", age)
print("Data Type:", type(age))


# ==================================================
# Example 2 : Float (float)
# ==================================================

cgpa = 8.45

print("\nCGPA:", cgpa)
print("Data Type:", type(cgpa))


# ==================================================
# Example 3 : String (str)
# ==================================================

student_name = "Rahul"

print("\nStudent Name:", student_name)
print("Data Type:", type(student_name))


# ==================================================
# Example 4 : Boolean (bool)
# ==================================================

is_placed = True

print("\nPlaced:", is_placed)
print("Data Type:", type(is_placed))


# ==================================================
# Example 5 : Multiple Data Types
# ==================================================

employee_name = "Amit"
salary = 55000
rating = 4.8
is_permanent = True

print("\n========== Employee Details ==========")
print("Employee Name :", employee_name)
print("Salary        :", salary)
print("Rating        :", rating)
print("Permanent     :", is_permanent)

print("\n========== Data Types ==========")
print(type(employee_name))
print(type(salary))
print(type(rating))
print(type(is_permanent))