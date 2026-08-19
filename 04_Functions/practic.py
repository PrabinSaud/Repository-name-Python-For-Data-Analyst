# ==========================================
# Module 04 - Functions
# Lesson 01 Practice
# ==========================================


# Question 1
#
# Create a function named show_name().
# Print your name.
# Call the function.
def show_name():
    print("Your Name")

show_name()

# Question 2
#
# Create a function named show_course().
# Print:
# BCA - Data Analytics
# Call the function two times.
def show_course():
    print("BCA - Data Analytics")
show_course()
show_course()

# Question 3
#
# Create a function named show_skills().
#
# Print:
# Python
# SQL
# Excel
# Tableau
#
# Call the function.


def show_skills():
    print("Python")
    print("SQL")
    print("Excel")
    print("Tableau")

show_skills()

# Question 4
#
# Create a function named show_message().
#
# Print:
# I am learning Python for Data Analysis
#
# Call the function three times.
def show_message():
    print("I am learning Python for Data Analysis")

show_message()
show_message()
show_message()

"""
====================================================
Module      : 04 - Functions
Practice    : Lesson 02 - Parameters
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""


# ==================================================
# Practice 1 : One Parameter
# ==================================================

# Create a function:
#
# greet(name)
#
# Print:
# Hello <name>
#
# Example:
# greet("Prabin")


# Write your code below 👇
def greet(name):
    print("Hello", name)

greet("Prabin")


# ==================================================
# Practice 2 : Addition
# ==================================================

# Create a function:
#
# add_numbers(a, b)
#
# Print the sum of two numbers.
#
# Example:
# add_numbers(15, 25)
#
# Expected:
# 40


# Write your code below 👇
def add_numbers(a, b):
    print(a + b)
add_numbers(15, 25)



# ==================================================
# Practice 3 : Multiplication
# ==================================================

# Create a function:
#
# multiply_numbers(a, b)
#
# Print the multiplication of two numbers.
#
# Example:
# multiply_numbers(10, 5)
#
# Expected:
# 50


# Write your code below 👇
def multiply_numbers(a, b):
    print(a * b)
multiply_numbers(10, 5)


# ==================================================
# Practice 4 : Rectangle Area
# ==================================================

# Create a function:
#
# rectangle_area(length, width)
#
# Calculate and print the area.
#
# Example:
# rectangle_area(10, 5)
#
# Expected:
# 50


# Write your code below 👇
def rectangle_area(length, width):
    area = length * width
    print(area)
rectangle_area(10, 5)


# ==================================================
# Practice 5 : Student Information
# ==================================================

# Create a function:
#
# student_info(name, age, course)
#
# Print:
#
# Name   : <name>
# Age    : <age>
# Course : <course>
#
# Call the function using positional arguments.


# Write your code below 👇
def student_info(name, age, course):
    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)
student_info("Prabin", 22, "BCA")


# ==================================================
# Practice 6 : Keyword Arguments
# ==================================================

# Create a function:
#
# employee_info(name, department, salary)
#
# Print all employee information.
#
# Call the function using keyword arguments.


# Write your code below 👇
def employee_info(name, department, salary):
    print("Name       :", name)
    print("Department :", department)
    print("Salary     :", salary)
employee_info( name="Prabin",department="Data Analytics", salary=50000)


# ==================================================
# Practice 7 : Salary Calculation
# ==================================================

# Create a function:
#
# calculate_salary(basic_salary, bonus)
#
# Calculate:
#
# total_salary = basic_salary + bonus
#
# Example:
# calculate_salary(30000, 5000)
#
# Expected:
# Total Salary : 35000


# Write your code below 👇
def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    print("Total Salary :", total_salary)
calculate_salary(30000, 5000)


# ==================================================
# Practice 8 : Average Marks
# ==================================================

# Create a function:
#
# calculate_average(mark1, mark2, mark3)
#
# Calculate and print the average.
#
# Example:
# calculate_average(80, 75, 90)


# Write your code below 👇
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    print("Average :", average)
calculate_average(80, 75, 90)


# ==================================================
# Practice 9 : Discount Calculation
# ==================================================

# Create a function:
#
# calculate_discount(price, discount)
#
# Calculate the discount amount:
#
# discount_amount = price * discount / 100
#
# Then calculate:
#
# final_price = price - discount_amount
#
# Example:
# calculate_discount(1000, 10)
#
# Expected:
# Final Price : 900


# Write your code below 👇
def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    print("Final Price :", final_price)
calculate_discount(1000, 10)


# ==================================================
# Practice 10 : Data Analyst Task
# ==================================================

# Create a function:
#
# sales_target(sales, target)
#
# If sales are greater than or equal to target:
#
# Target Achieved
#
# Otherwise:
#
# Target Missed
#
# Example:
# sales_target(75000, 50000)


# Write your code below 👇
def sales_target(sales, target):
    if sales >= target:
        print("Target Achieved")
    else:
        print("Target Missed")
sales_target(75000, 50000)
