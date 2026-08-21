"""
====================================================
Module      : 04 - Functions
Lesson      : 05
Topic       : Scope
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is Scope?
# ==================================================

# Scope determines where a variable can be accessed
# in a Python program.
#
# The two basic types of scope we will learn are:
#
# 1. Local Scope
# 2. Global Scope


# ==================================================
# Example 1 : Local Variable
# ==================================================

def student_info():

    name = "Prabin"

    print("Name :", name)


student_info()


# ==================================================
# Example 2 : Local Variable Cannot Be Accessed
# Outside the Function
# ==================================================

def calculate_salary():

    salary = 30000

    print("Salary :", salary)


calculate_salary()

# The following would cause an error:
#
# print(salary)
#
# Because salary exists only inside the function.


# ==================================================
# Example 3 : Global Variable
# ==================================================

name = "Prabin"


def greet():

    print("Hello", name)


greet()

print("Name :", name)


# ==================================================
# Example 4 : Global Variable Inside a Function
# ==================================================

target = 50000


def check_sales(sales):

    print("Sales :", sales)
    print("Target :", target)


check_sales(75000)


# ==================================================
# Example 5 : Same Variable Name
# ==================================================

name = "Prabin"


def student():

    name = "Rahul"

    print("Inside Function :", name)


student()

print("Outside Function :", name)


# ==================================================
# Example 6 : Local Variable Has Priority
# ==================================================

salary = 50000


def employee():

    salary = 30000

    print("Inside Function :", salary)


employee()

print("Outside Function :", salary)


# ==================================================
# Example 7 : Reading a Global Variable
# ==================================================

tax_rate = 10


def calculate_tax(salary):

    tax = salary * tax_rate / 100

    return tax


tax = calculate_tax(50000)

print("Tax :", tax)


# ==================================================
# Example 8 : Changing a Global Variable
# ==================================================

counter = 0


def increase_counter():

    global counter

    counter = counter + 1


increase_counter()
increase_counter()

print("Counter :", counter)


# ==================================================
# Example 9 : Local Scope in Data Analysis
# ==================================================

total_sales = 100000


def calculate_profit(cost):

    profit = total_sales - cost

    return profit


profit = calculate_profit(65000)

print("Profit :", profit)

# profit is created outside the function as well,
# because we stored the returned value.


# ==================================================
# Example 10 : Global vs Local Scope
# ==================================================

department = "Data Analytics"


def employee_info():

    employee_name = "Prabin"

    print("Name       :", employee_name)
    print("Department :", department)


employee_info()

print("Department :", department)

# employee_name is local.
# department is global.