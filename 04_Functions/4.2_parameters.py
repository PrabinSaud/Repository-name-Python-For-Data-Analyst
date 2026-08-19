"""
====================================================
Module      : 04 - Functions
Lesson      : 02
Topic       : Parameters
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What are Parameters?
# ==================================================

# Parameters are variables used to receive values
# when a function is called.


# ==================================================
# Example 1 : One Parameter
# ==================================================

def greet(name):
    print("Hello", name)


greet("Prabin")


# ==================================================
# Example 2 : Two Parameters
# ==================================================

def add_numbers(a, b):
    print("Sum :", a + b)


add_numbers(10, 20)


# ==================================================
# Example 3 : Multiple Parameters
# ==================================================

def student_info(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)


student_info("Prabin", 22, "BCA")


# ==================================================
# Example 4 : Positional Arguments
# ==================================================

def employee_info(name, department):
    print("Name       :", name)
    print("Department :", department)


employee_info("Rahul", "Finance")


# ==================================================
# Example 5 : Keyword Arguments
# ==================================================

employee_info(
    department="Data Analytics",
    name="Prabin"
)


# ==================================================
# Example 6 : Salary Calculation
# ==================================================

def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus

    print("Basic Salary :", basic_salary)
    print("Bonus        :", bonus)
    print("Total Salary :", total_salary)


calculate_salary(30000, 5000)


# ==================================================
# Example 7 : Rectangle Area
# ==================================================

def calculate_area(length, width):
    area = length * width

    print("Area :", area)


calculate_area(10, 5)


# ==================================================
# Example 8 : Average Marks
# ==================================================

def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3

    print("Average :", average)


calculate_average(80, 75, 90)