"""
====================================================
Module      : 04 - Functions
Lesson      : 04
Topic       : Default Arguments
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What are Default Arguments?
# ==================================================

# A default argument is a parameter that already
# has a default value.
#
# If no value is provided when the function is called,
# Python uses the default value.


# ==================================================
# Example 1 : Basic Default Argument
# ==================================================

def greet(name="Prabin"):
    print("Hello", name)


greet()
greet("Rahul")


# ==================================================
# Example 2 : Default Age
# ==================================================

def student_info(name, age=18):
    print("Name :", name)
    print("Age  :", age)


student_info("Prabin")
student_info("Rahul", 22)


# ==================================================
# Example 3 : Default Department
# ==================================================

def employee_info(name, department="IT"):
    print("Name       :", name)
    print("Department :", department)


employee_info("Prabin")
employee_info("Rahul", "Finance")


# ==================================================
# Example 4 : Default Quantity
# ==================================================

def calculate_total(price, quantity=1):

    total = price * quantity

    print("Total :", total)


calculate_total(500)
calculate_total(500, 3)


# ==================================================
# Example 5 : Multiple Default Arguments
# ==================================================

def student_result(name, python=0, sql=0, excel=0):

    total = python + sql + excel

    print("Name  :", name)
    print("Total :", total)


student_result("Prabin")
student_result("Rahul", 80, 75, 90)


# ==================================================
# Example 6 : Default Target
# ==================================================

def check_target(sales, target=50000):

    if sales >= target:
        return "Target Achieved"

    return "Target Missed"


result1 = check_target(60000)
result2 = check_target(45000)
result3 = check_target(60000, 70000)

print(result1)
print(result2)
print(result3)


# ==================================================
# Example 7 : Default Discount
# ==================================================

def calculate_discount(price, discount=10):

    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price


price1 = calculate_discount(1000)
price2 = calculate_discount(1000, 20)

print("Final Price 1 :", price1)
print("Final Price 2 :", price2)


# ==================================================
# Example 8 : Data Analyst Example
# ==================================================

def calculate_salary(basic_salary, bonus=5000):

    total_salary = basic_salary + bonus

    return total_salary


salary1 = calculate_salary(30000)
salary2 = calculate_salary(30000, 10000)

print("Salary 1 :", salary1)
print("Salary 2 :", salary2)


# ==================================================
# Example 9 : Default Value with Keyword Argument
# ==================================================

def sales_report(sales, target=50000):

    if sales >= target:
        return "Target Achieved"

    return "Target Missed"


result = sales_report(sales=75000)

print("Sales Report :", result)


# ==================================================
# Important Rule
# ==================================================

# Required parameters must come before
# default parameters.
#
# Correct:
#
# def employee(name, department="IT"):
#     print(name, department)
#
#
# Incorrect:
#
# def employee(department="IT", name):
#     print(name, department)