# ==========================================
# Module 04 - Functions
# Lesson 01 Practice
# ==========================================


# Question 1
#
# Create a function named show_name().
# Print your name.
# Call the function.
from csv import excel


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



# ==================================================
# Topic 2 : Return
# ==================================================

# Practice 11
#
# Create a function:
#
# add_numbers(a, b)
#
# Return the sum of two numbers.
#
# Store the result in a variable and print it.
#
# Example:
# result = add_numbers(10, 20)
# print(result)


# Write your code below 👇
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(result)

# ==================================================
# Practice 12
#
# Create a function:
#
# multiply_numbers(a, b)
#
# Return the multiplication of two numbers.
#
# Example:
# multiply_numbers(10, 5)
#
# Expected:
# 50


# Write your code below 👇
def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(10, 5)
print(result)


# ==================================================
# Practice 13
#
# Create a function:
#
# calculate_square(number)
#
# Return the square of the number.
#
# Example:
# calculate_square(8)
#
# Expected:
# 64


# Write your code below 👇
def calculate_square(number):
    return number ** 2
result = calculate_square(8)
print(result)


# ==================================================
# Practice 14
#
# Create a function:
#
# calculate_average(mark1, mark2, mark3)
#
# Return the average of three marks.
#
# Example:
# calculate_average(80, 70, 90)


# Write your code below 👇
def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average
result = calculate_average(80, 70, 90)
print(result)


# ==================================================
# Practice 15
#
# Create a function:
#
# calculate_total(price, quantity)
#
# Return:
#
# price * quantity
#
# Store the returned value in:
#
# total
#
# Then print total.


# Write your code below 👇
def calculate_total(price, quantity):
    return price * quantity
result = calculate_total(100, 5)
print(result)


# ==================================================
# Practice 16
#
# Create a function:
#
# calculate_profit(revenue, cost)
#
# Return the profit.
#
# Formula:
#
# profit = revenue - cost
#
# Example:
# calculate_profit(100000, 65000)
#
# Expected:
# 35000


# Write your code below 👇
def calculate_profit(revenue, cost):
    return revenue - cost
result = calculate_profit(100000, 65000)
print(result)

# ==================================================
# Practice 17
#
# Create a function:
#
# calculate_discount(price, discount)
#
# Return the final price after discount.
#
# Formula:
#
# discount_amount = price * discount / 100
# final_price = price - discount_amount
#
# Example:
# calculate_discount(2000, 10)
#
# Expected:
# 1800


# Write your code below 👇
def calculate_discount(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

result = calculate_discount(2000, 10)
print(result)


# ==================================================
# Practice 18
#
# Create a function:
#
# check_pass(marks)
#
# Return:
#
# "Pass" if marks >= 40
# "Fail" otherwise.
#
# Example:
# check_pass(75)
#
# Expected:
# Pass


# Write your code below 👇
def check_pass(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"

result = check_pass(75)
print(result)


# ==================================================
# Practice 19
#
# Create a function:
#
# calculate_salary(basic_salary, bonus)
#
# Return the total salary.
#
# Example:
# calculate_salary(30000, 5000)
#
# Expected:
# 35000


# Write your code below 👇
def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    return total_salary

result = calculate_salary(30000, 5000)
print(result)


# ==================================================
# Practice 20 : Data Analyst Task
#
# Create a function:
#
# calculate_profit_margin(revenue, cost)
#
# Calculate:
#
# profit = revenue - cost
# profit_margin = (profit / revenue) * 100
#
# Return the profit margin.
#
# Example:
# calculate_profit_margin(100000, 70000)
#
# Expected:
# 30.0


# Write your code below 👇
def calculate_profit_margin(revenue, cost):
    profit = revenue - cost
    profit_margin = (profit / revenue) * 100
    return profit_margin
result = calculate_profit_margin(100000, 70000)
print(result)

# ==================================================
# Topic 3 : Default Arguments
# ==================================================

# Practice 21
#
# Create a function:
#
# greet(name="Prabin")
#
# Print:
# Hello <name>
#
# Call the function once without an argument
# and once with an argument.


# Write your code below 👇
def greet(name="Prabin"):
    print("Hello", name)

greet()
greet("Rahul")


# ==================================================
# Practice 22
#
# Create a function:
#
# student_info(name, age=18)
#
# Print the student's name and age.
#
# Test the function with and without age.


# Write your code below 👇
def student_info(name, age=18):
    print("Name :", name)
    print("Age  :", age)

student_info("Prabin")
student_info("Rahul", 22)


# ==================================================
# Practice 23
#
# Create a function:
#
# employee_info(name, department="IT")
#
# Print employee name and department.
#
# Test both default and custom department.


# Write your code below 👇
def employee_info(name, department="IT"):
    print("Name       :", name)
    print("Department :", department)

employee_info("Prabin")
employee_info("Rahul", "Finance")


# ==================================================
# Practice 24
#
# Create a function:
#
# calculate_total(price, quantity=1)
#
# Calculate:
#
# total = price * quantity
#
# Test:
#
# calculate_total(500)
# calculate_total(500, 3)


# Write your code below 👇
def calculate_total(price, quantity=1):
    total = price * quantity
    print("Total :", total)

calculate_total(500)
calculate_total(500, 3)


# ==================================================
# Practice 25
#
# Create a function:
#
# calculate_discount(price, discount=10)
#
# Calculate the final price after discount.
#
# Test:
#
# calculate_discount(1000)
# calculate_discount(1000, 20)


# Write your code below 👇
def calculate_discount(price, discount=10):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    print("Final Price :", final_price)

calculate_discount(1000)
calculate_discount(1000, 20)


# ==================================================
# Practice 26
#
# Create a function:
#
# check_target(sales, target=50000)
#
# Return:
#
# "Target Achieved"
# "Target Missed"
#
# Test with default and custom targets.


# Write your code below 👇
def check_target(sales, target=50000):
    if sales >= target:
        return "Target Achieved"
    return "Target Missed"

result1 = check_target(60000)
result2 = check_target(45000)


# ==================================================
# Practice 27
#
# Create a function:
#
# calculate_salary(basic_salary, bonus=5000)
#
# Return the total salary.
#
# Test:
#
# calculate_salary(30000)
# calculate_salary(30000, 10000)


# Write your code below 👇
def calculate_salary(basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    return total_salary

salary1 = calculate_salary(30000)
salary2 = calculate_salary(30000, 10000)


# ==================================================
# Practice 28
#
# Create a function:
#
# student_result(name, python=0, sql=0, excel=0)
#
# Calculate and return total marks.
#
# Example:
#
# student_result("Prabin", 80, 75, 90)
#
# Expected:
# 245


# Write your code below 👇
def student_result(name, python=0, sql=0, excel=0):
    total = python + sql + excel
    return total
student1_total = student_result("Prabin", 80, 75, 90)
print(f"Total marks for {student1_total}")


# ==================================================
# Practice 29
#
# Create a function:
#
# calculate_profit(revenue, cost=50000)
#
# Return:
#
# revenue - cost
#
# Test the function with the default cost
# and a custom cost.


# Write your code below 👇
def calculate_profit(revenue, cost=50000):
    profit = revenue - cost
    return profit
custom_profit = calculate_profit(100000, 60000)
default_profit = calculate_profit(100000)


# ==================================================
# Practice 30 : Data Analyst Task
#
# Create a function:
#
# sales_report(sales, target=50000)
#
# Return:
#
# "Target Achieved" if sales >= target
# "Target Missed" otherwise
#
# Test the function using:
#
# 1. Default target
# 2. Custom target
#
# Example:
#
# sales_report(75000)
# sales_report(75000, 80000)


# Write your code below 👇
def sales_report(sales, target=50000):
    if sales >= target:
        return "Target Achieved"
    return "Target Missed"
sales1 = sales_report(75000)
sales2 = sales_report(75000, 80000)



# ==================================================
# Topic 4 : Scope
# ==================================================

# Practice 31
#
# Create a function:
#
# student_info()
#
# Create a local variable:
#
# name = "Prabin"
#
# Print the name inside the function.


# Write your code below 👇
def student_info():
    name = "Prabin"
    print("Name :", name)

student_info()


# ==================================================
# Practice 32
#
# Create a local variable inside a function:
#
# salary = 30000
#
# Print it inside the function.
#
# Then try printing salary outside the function.
#
# Observe what happens.


# Write your code below 👇
def calculate_salary():
    salary = 30000
    print("Salary :", salary)

calculate_salary() 
print(salary)  # This would cause an error because salary is not defined outside the function


# ==================================================
# Practice 33
#
# Create a global variable:
#
# company = "ABC Ltd"
#
# Create a function that prints the company name.
#
# Call the function.


# Write your code below 👇
company = "ABC Ltd"
def print_company():
    print("Company :", company)

print_company()


# ==================================================
# Practice 34
#
# Create:
#
# target = 50000
#
# Create a function:
#
# check_sales(sales)
#
# Print both sales and target.


# Write your code below 👇
def check_sales(sales):
    target = 50000
    print("Sales :", sales)
    print("Target :", target)

check_sales(75000)


# ==================================================
# Practice 35
#
# Create:
#
# name = "Prabin"
#
# Inside a function create another variable:
#
# name = "Rahul"
#
# Print name inside and outside the function.
#
# Observe the difference.


# Write your code below 👇
    
name = "Prabin"
def student():
    name = "Rahul"
    print("Inside Function :", name)

student()
print("Outside Function :", name)


# ==================================================
# Practice 36
#
# Create:
#
# tax_rate = 10
#
# Create:
#
# calculate_tax(salary)
#
# Use the global tax_rate to calculate tax.
#
# Return the tax amount.


# Write your code below 👇
tax_rate = 10
def calculate_tax(salary):
    tax = salary * tax_rate / 100
    return tax
print(calculate_tax(50000))


# ==================================================
# Practice 37
#
# Create:
#
# counter = 0
#
# Create a function:
#
# increase_counter()
#
# Use the global keyword to increase counter by 1.
#
# Call the function three times.
#
# Expected:
# 3


# Write your code below 👇
counter = 0
def increase_counter():
    global counter
    counter = counter + 1
increase_counter()
increase_counter()
increase_counter()


# ==================================================
# Practice 38
#
# Create:
#
# total_sales = 100000
#
# Create:
#
# calculate_profit(cost)
#
# Calculate:
#
# profit = total_sales - cost
#
# Return the profit.


# Write your code below 👇



# ==================================================
# Practice 39
#
# Create a global variable:
#
# department = "Data Analytics"
#
# Create a function:
#
# employee_info(name)
#
# Print:
#
# Employee Name
# Department
#
# Use the global department variable.


# Write your code below 👇
department = "Data Analytics"
def employee_info(name):
    print("Employee Name :", name)
    print("Department    :", department)

employee_info("Prabin")


# ==================================================
# Practice 40 : Data Analyst Task
#
# Create:
#
# tax_rate = 10
#
# Create a function:
#
# calculate_net_salary(salary)
#
# Requirements:
#
# 1. Use the global tax_rate.
# 2. Calculate tax.
# 3. Calculate net salary.
# 4. Return net salary.
#
# Formula:
#
# tax = salary * tax_rate / 100
# net_salary = salary - tax
#
# Example:
#
# calculate_net_salary(50000)
#
# Expected:
# 45000.0


# Write your code below 👇
tax_rate = 10
def calculate_net_salary(salary):
    tax = salary * tax_rate / 100
    net_salary = salary - tax
    return net_salary
print(calculate_net_salary(50000))


# ==================================================
# Topic 5 : Functions with Collections
# ==================================================

# Practice 41
#
# Create a function:
#
# print_fruits(fruits)
#
# Print every fruit from the list.
#
# Example:
# ["Apple", "Banana", "Mango"]


# Write your code below 👇
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["Apple", "Banana", "Mango"]
print_fruits(fruits)


# ==================================================
# Practice 42
#
# Create a function:
#
# calculate_total(numbers)
#
# Return the sum of all numbers in a list.
#
# Example:
# [10, 20, 30, 40]
#
# Expected:
# 100


# Write your code below 👇
def calculate_total(numbers):
    total = sum(numbers)
    return total
numbers = [10, 20, 30, 40]
print(calculate_total(numbers))


# ==================================================
# Practice 43
#
# Create a function:
#
# calculate_average(numbers)
#
# Return the average of numbers in a list.
#
# Example:
# [80, 70, 90]
#
# Expected:
# 80.0


# Write your code below 👇
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers = [80, 70, 90]
print(calculate_average(numbers))


# ==================================================
# Practice 44
#
# Create a function:
#
# find_highest(numbers)
#
# Return the highest number from the list.
#
# Example:
# [25, 80, 45, 90, 60]
#
# Expected:
# 90


# Write your code below 👇
def find_highest(numbers):
    highest = max(numbers)
    return highest
numbers = [25, 80, 45, 90, 60]
print(find_highest(numbers))


# ==================================================
# Practice 45
#
# Create a function:
#
# find_lowest(numbers)
#
# Return the lowest number from the list.
#
# Example:
# [25, 80, 45, 90, 60]
#
# Expected:
# 25


# Write your code below 👇
def find_lowest(numbers):
    lowest = min(numbers)
    return lowest
numbers = [25, 80, 45, 90, 60]
print(find_lowest(numbers))


# ==================================================
# Practice 46
#
# Create a function:
#
# passing_marks(marks)
#
# Create a new list containing only marks >= 40.
#
# Return the new list.
#
# Example:
# [35, 80, 55, 28, 92]
#
# Expected:
# [80, 55, 92]


# Write your code below 👇
def passing_marks(marks):
    passed = []
    for mark in marks:
        if mark >= 40:
            passed.append(mark)
    return passed
marks = [35, 80, 55, 28, 92]
print(passing_marks(marks))


# ==================================================
# Practice 47
#
# Create a function:
#
# count_unique(numbers)
#
# Accept a set and return the number of unique values.
#
# Example:
# {10, 20, 20, 30, 30}
#
# Expected:
# 3


# Write your code below 👇
def count_unique(numbers):
    return len(numbers)
numbers = {10, 20, 20, 30, 30}
print(count_unique(numbers))


# ==================================================
# Practice 48
#
# Create a function:
#
# student_info(student)
#
# Accept a dictionary containing:
#
# name
# age
# course
#
# Print all student information.


# Write your code below 👇
def student_info(student):
    print("Name   :", student["name"])
    print("Age    :", student["age"])
    print("Course :", student["course"])
student = {"name": "Prabin", "age": 22, "course": "BCA"}
student_info(student)


# ==================================================
# Practice 49
#
# Create a function:
#
# calculate_salary(employee)
#
# Accept a dictionary containing:
#
# basic_salary
# bonus
#
# Return the total salary.


# Write your code below 👇
def calculate_salary(employee):
    basic_salary = employee["basic_salary"]
    bonus = employee["bonus"]
    total_salary = basic_salary + bonus
    return total_salary
employee = {"basic_salary":     30000, "bonus": 5000}
print(calculate_salary(employee))


# ==================================================
# Practice 50 : Data Analyst Task
#
# Create a function:
#
# sales_summary(sales)
#
# The function should calculate:
#
# 1. Total sales
# 2. Average sales
# 3. Highest sales
# 4. Lowest sales
#
# Return all four values.
#
# Example:
#
# sales = [25000, 30000, 45000, 38000, 50000]
#
# Expected:
#
# Total    : 188000
# Average  : 37600.0
# Highest  : 50000
# Lowest   : 25000


# Write your code below 👇
def sales_summary(sales):
    total = sum(sales)
    average = total / len(sales)
    highest = max(sales)
    lowest = min(sales)
    return total, average, highest, lowest

sales = [25000, 30000, 45000, 38000, 50000]
total, average, highest, lowest = sales_summary(sales)
print("Total    :", total)
print("Average  :", average)
print("Highest  :", highest)
print("Lowest   :", lowest)