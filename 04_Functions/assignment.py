"""
====================================================
Module      : 04 - Functions
Final Assignment
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# Question 1 : Basic Function
# ==================================================

# Create a function:
#
# show_message()
#
# Print:
#
# "Welcome to Python Data Analysis"
#
# Call the function.


# Write your code below 👇
def show_message():
    print("Welcome to Python Data Analysis")

show_message()


# ==================================================
# Question 2 : Parameters
# ==================================================

# Create a function:
#
# student_info(name, course, age)
#
# Print:
#
# Name   : <name>
# Course : <course>
# Age    : <age>
#
# Call the function using the three parameters.


# Write your code below 👇
def student_info(name, course, age):
    print("Name   :", name)
    print("Course :", course)
    print("Age    :", age)

student_info("Prabin", "BCA", 22)


# ==================================================
# Question 3 : Return
# ==================================================

# Create a function:
#
# calculate_total(price, quantity)
#
# Return the total purchase amount.
#
# Formula:
#
# total = price * quantity
#
# Store the returned value in a variable
# and print it.
#
# Example:
#
# calculate_total(500, 4)
#
# Expected:
# 2000


# Write your code below 👇
def calculate_total(price, quantity):
    total = price * quantity
    return total

calculated_total = calculate_total(500, 4)
print("Total Purchase Amount:", calculated_total)


# ==================================================
# Question 4 : Default Argument
# ==================================================

# Create a function:
#
# calculate_salary(basic_salary, bonus=5000)
#
# Return the total salary.
#
# Test the function:
#
# 1. Using the default bonus.
# 2. Using a custom bonus.
#
# Example:
#
# calculate_salary(30000)
# calculate_salary(30000, 10000)


# Write your code below 👇
def calculate_salary(basic_salary, bonus=5000):
    total_salary = basic_salary + bonus
    return total_salary
calculated_salary_default = calculate_salary(30000)
calculated_salary_custom = calculate_salary(30000, 10000)
print("Salary with Default Bonus:", calculated_salary_default)
print("Salary with Custom Bonus:", calculated_salary_custom)    


# ==================================================
# Question 5 : Parameters + Return + If
# ==================================================

# Create a function:
#
# check_result(marks)
#
# Return:
#
# "Pass" if marks >= 40
# "Fail" otherwise.
#
# Example:
#
# check_result(75)
#
# Expected:
# Pass


# Write your code below 👇
def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"
check_result_result = check_result(75)
print("Result:", check_result_result)


# ==================================================
# Question 6 : Functions with List
# ==================================================

# Create a function:
#
# calculate_average(marks)
#
# Accept a list of marks.
#
# Calculate and return the average.
#
# Example:
#
# marks = [80, 75, 90, 85, 70]
#
# Expected:
# 80.0


# Write your code below 👇
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

marks = [80, 75, 90, 85, 70]
print("Average Marks:", calculate_average(marks))


# ==================================================
# Question 7 : List + Function + Condition
# ==================================================

# Create a function:
#
# get_passing_marks(marks)
#
# Accept a list of marks.
#
# Create a new list containing only marks >= 40.
#
# Return the new list.
#
# Example:
#
# marks = [35, 80, 55, 28, 92, 65]
#
# Expected:
# [80, 55, 92, 65]


# Write your code below 👇
def get_passing_marks(marks):
    passing = []
    for mark in marks:
        if mark >= 40:
            passing.append(mark)
    return passing

marks = [35, 80, 55, 28, 92, 65]
passing_marks = get_passing_marks(marks)
print("Passing Marks:", passing_marks)


# ==================================================
# Question 8 : Dictionary + Function
# ==================================================

# Create a function:
#
# employee_salary(employee)
#
# The dictionary contains:
#
# name
# basic_salary
# bonus
#
# Calculate and return the total salary.
#
# Example:
#
# employee = {
#     "name": "Prabin",
#     "basic_salary": 30000,
#     "bonus": 5000
# }
#
# Expected:
# 35000


# Write your code below 👇
def employee_salary(employee):
    basic_salary = employee["basic_salary"]
    bonus = employee["bonus"]
    total_salary = basic_salary + bonus
    return total_salary

employee = {
    "name": "Prabin",
    "basic_salary": 30000,
    "bonus": 5000
}
print("Total Salary:", employee_salary(employee))


# ==================================================
# Question 9 : Global Scope
# ==================================================

# Create a global variable:
#
# tax_rate = 10
#
# Create a function:
#
# calculate_tax(salary)
#
# Use the global tax_rate.
#
# Calculate:
#
# tax = salary * tax_rate / 100
#
# Return the tax amount.
#
# Example:
#
# calculate_tax(50000)
#
# Expected:
# 5000.0


# Write your code below 👇
tax_rate = 10
def calculate_tax(salary):
    tax = salary * tax_rate / 100
    return tax

calculated_tax = calculate_tax(50000)
print("Tax Amount:", calculated_tax)

# ==================================================
# Question 10 : Default Argument + List
# ==================================================

# Create a function:
#
# sales_summary(sales, target=50000)
#
# Accept a list of sales.
#
# Calculate:
#
# 1. Total sales
# 2. Average sales
# 3. Highest sales
# 4. Lowest sales
# 5. Number of sales that reached the target
#
# Return all five values.
#
# Example:
#
# sales = [42000, 55000, 48000, 62000, 70000]
#
# Target = 50000
#
# Expected:
#
# Total Sales       : 277000
# Average Sales     : 55400.0
# Highest Sales     : 70000
# Lowest Sales      : 42000
# Target Achieved   : 3
#
# Test the function with:
#
# 1. Default target.
# 2. Custom target.


# Write your code below 👇
def sales_summary(sales, target=50000):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    highest_sales = max(sales)
    lowest_sales = min(sales)
    target_achieved_count = sum(1 for sale in sales if sale >= target)

    return total_sales, average_sales, highest_sales, lowest_sales, target_achieved_count
sales = [42000, 55000, 48000, 62000, 70000]
total, average, highest, lowest, target_count = sales_summary(sales)
default_target = 50000
print("Total Sales       :", total)
print("Average Sales     :", average)
print("Highest Sales     :", highest)
print("Lowest Sales      :", lowest)
print("Target Achieved   :", target_count)

# ==================================================
# Question 11 : Multiple Return Values
# ==================================================

# Create a function:
#
# analyze_marks(marks)
#
# Accept a list of marks.
#
# Return:
#
# 1. Total marks
# 2. Average marks
# 3. Highest mark
# 4. Lowest mark
#
# Example:
#
# marks = [80, 75, 90, 65, 85]
#
# Store all returned values in separate variables.
#
# Print each result.


# Write your code below 👇
def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return total, average, highest, lowest

marks = [80, 75, 90, 65, 85]
total, average, highest, lowest = analyze_marks(marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)


# ==================================================
# Question 12 : Mini Data Analysis Project
# ==================================================

# Monthly sales data:
#
# sales = [45000, 52000, 48000, 65000, 72000, 39000]
#
# Create a function:
#
# analyze_sales(sales, target=50000)
#
# Requirements:
#
# 1. Calculate total sales.
#
# 2. Calculate average sales.
#
# 3. Find highest sales.
#
# 4. Find lowest sales.
#
# 5. Count how many months achieved the target.
#
# 6. Create a list containing only sales
#    greater than or equal to the target.
#
# 7. Return all required results.
#
# Use the default target of 50000.
#
# Then call the function and print:
#
# Total Sales
# Average Sales
# Highest Sales
# Lowest Sales
# Target Achieved Count
# Target Achieved Sales
#
# Finally, call the same function again
# with a custom target of 60000.


# Write your code below 👇
def analyze_sales(sales, target=50000):
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    highest_sales = max(sales)
    lowest_sales = min(sales)
    target_achieved_count = sum(1 for sale in sales if sale >= target)
    target_achieved_sales = [sale for sale in sales if sale >= target]

    return (total_sales, average_sales, highest_sales, lowest_sales,
            target_achieved_count, target_achieved_sales)

sales = [45000, 52000, 48000, 65000, 72000, 39000]
results = analyze_sales(sales)