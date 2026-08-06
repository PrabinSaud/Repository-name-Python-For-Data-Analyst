"""
====================================================
Module      : 01 - Python Basics
Lesson      : 05
Topic       : Input & Output
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is Output?
# ==================================================

print("Welcome to Python!")

# ==================================================
# Example 1 : Print Variables
# ==================================================

student_name = "Rahul"
age = 21

print("Student Name :", student_name)
print("Age          :", age)

# ==================================================
# Example 2 : User Input
# ==================================================

name = input("Enter your name: ")

print("Hello,", name)

# ==================================================
# Example 3 : Integer Input
# ==================================================

age = int(input("Enter your age: "))

print("Your age is:", age)

# ==================================================
# Example 4 : Float Input
# ==================================================

cgpa = float(input("Enter your CGPA: "))

print("Your CGPA is:", cgpa)

# ==================================================
# Example 5 : Mini Student Profile
# ==================================================

student_name = input("Student Name: ")
course = input("Course: ")
semester = int(input("Semester: "))
cgpa = float(input("CGPA: "))

print("\n========== Student Profile ==========")
print("Name      :", student_name)
print("Course    :", course)
print("Semester  :", semester)
print("CGPA      :", cgpa)