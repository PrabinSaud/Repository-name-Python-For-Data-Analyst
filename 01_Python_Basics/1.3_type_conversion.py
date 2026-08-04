"""
====================================================
Module      : 01 - Python Basics
Lesson      : 03
Topic       : Type Conversion
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is Type Conversion?
# ==================================================

# Type conversion means changing one data type into another.


# ==================================================
# Example 1 : String to Integer
# ==================================================

age = "21"

print("Before:", age, type(age))

age = int(age)

print("After :", age, type(age))


# ==================================================
# Example 2 : Integer to Float
# ==================================================

salary = 55000

print("\nBefore:", salary, type(salary))

salary = float(salary)

print("After :", salary, type(salary))


# ==================================================
# Example 3 : Float to Integer
# ==================================================

cgpa = 8.75

print("\nBefore:", cgpa, type(cgpa))

cgpa = int(cgpa)

print("After :", cgpa, type(cgpa))


# ==================================================
# Example 4 : Integer to String
# ==================================================

roll_number = 101

print("\nBefore:", roll_number, type(roll_number))

roll_number = str(roll_number)

print("After :", roll_number, type(roll_number))


# ==================================================
# Example 5 : Boolean Conversion
# ==================================================

number = 1

print("\nBefore:", number, type(number))

result = bool(number)

print("After :", result, type(result))