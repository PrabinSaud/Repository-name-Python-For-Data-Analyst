"""
====================================================
Module      : 04 - Functions
Lesson      : 06
Topic       : Functions with Collections
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What are Functions with Collections?
# ==================================================

# Functions can accept collections such as:
#
# Lists
# Tuples
# Sets
# Dictionaries
#
# They can also return collections.


# ==================================================
# Example 1 : Function with a List
# ==================================================

def print_fruits(fruits):

    for fruit in fruits:
        print(fruit)


fruits = ["Apple", "Banana", "Mango"]

print_fruits(fruits)


# ==================================================
# Example 2 : Function with a List of Numbers
# ==================================================

def print_numbers(numbers):

    for number in numbers:
        print(number)


numbers = [10, 20, 30, 40, 50]

print_numbers(numbers)


# ==================================================
# Example 3 : Calculate Total from a List
# ==================================================

def calculate_total(sales):

    total = sum(sales)

    return total


monthly_sales = [25000, 30000, 28000, 35000]

total_sales = calculate_total(monthly_sales)

print("Total Sales :", total_sales)


# ==================================================
# Example 4 : Calculate Average from a List
# ==================================================

def calculate_average(numbers):

    total = sum(numbers)
    average = total / len(numbers)

    return average


marks = [80, 75, 90, 85, 70]

average = calculate_average(marks)

print("Average :", average)


# ==================================================
# Example 5 : Find Maximum Value
# ==================================================

def find_maximum(numbers):

    return max(numbers)


sales = [42000, 55000, 48000, 62000]

maximum_sales = find_maximum(sales)

print("Highest Sales :", maximum_sales)


# ==================================================
# Example 6 : Find Minimum Value
# ==================================================

def find_minimum(numbers):

    return min(numbers)


sales = [42000, 55000, 48000, 62000]

minimum_sales = find_minimum(sales)

print("Lowest Sales :", minimum_sales)


# ==================================================
# Example 7 : Filter Passing Marks
# ==================================================

def passing_marks(marks):

    passed = []

    for mark in marks:

        if mark >= 40:
            passed.append(mark)

    return passed


marks = [35, 80, 55, 28, 92, 65]

result = passing_marks(marks)

print("Passing Marks :", result)


# ==================================================
# Example 8 : Function with a Tuple
# ==================================================

def calculate_total(numbers):

    return sum(numbers)


numbers = (10, 20, 30, 40)

total = calculate_total(numbers)

print("Total :", total)


# ==================================================
# Example 9 : Function with a Set
# ==================================================

def count_unique_values(values):

    return len(values)


numbers = {10, 20, 20, 30, 30, 40}

unique_count = count_unique_values(numbers)

print("Unique Values :", unique_count)


# ==================================================
# Example 10 : Function with a Dictionary
# ==================================================

def print_student(student):

    print("Name   :", student["name"])
    print("Age    :", student["age"])
    print("Course :", student["course"])


student = {
    "name": "Prabin",
    "age": 22,
    "course": "BCA"
}

print_student(student)


# ==================================================
# Example 11 : Calculate Salary from Dictionary
# ==================================================

def calculate_salary(employee):

    basic_salary = employee["basic_salary"]
    bonus = employee["bonus"]

    total_salary = basic_salary + bonus

    return total_salary


employee = {
    "name": "Rahul",
    "basic_salary": 30000,
    "bonus": 5000
}

salary = calculate_salary(employee)

print("Total Salary :", salary)


# ==================================================
# Example 12 : Data Analyst Example
# ==================================================

def calculate_sales_summary(sales):

    total = sum(sales)
    average = total / len(sales)
    highest = max(sales)
    lowest = min(sales)

    return total, average, highest, lowest


monthly_sales = [25000, 30000, 45000, 38000, 50000]

total, average, highest, lowest = calculate_sales_summary(monthly_sales)

print("Total Sales   :", total)
print("Average Sales :", average)
print("Highest Sales :", highest)
print("Lowest Sales  :", lowest)