"""
====================================================
Module      : 04 - Functions
Lesson      : 03
Topic       : Return
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is return?
# ==================================================

# The return statement sends a value back from a function.
# The returned value can be stored in a variable and reused.


# ==================================================
# Example 1 : Basic Return
# ==================================================

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)

print("Result :", result)


# ==================================================
# Example 2 : Return vs Print
# ==================================================

def add_with_print(a, b):
    print(a + b)


def add_with_return(a, b):
    return a + b


add_with_print(10, 20)

result = add_with_return(10, 20)

print("Returned Result :", result)


# ==================================================
# Example 3 : Storing Returned Value
# ==================================================

def multiply_numbers(a, b):
    return a * b


result = multiply_numbers(10, 5)

print("Multiplication :", result)


# ==================================================
# Example 4 : Return with a Variable
# ==================================================

def calculate_average(mark1, mark2, mark3):

    total = mark1 + mark2 + mark3
    average = total / 3

    return average


result = calculate_average(80, 75, 90)

print("Average :", result)


# ==================================================
# Example 5 : Return Final Price
# ==================================================

def calculate_discount(price, discount):

    discount_amount = price * discount / 100
    final_price = price - discount_amount

    return final_price


result = calculate_discount(2000, 10)

print("Final Price :", result)


# ==================================================
# Example 6 : Return with If Statement
# ==================================================

def check_pass(marks):

    if marks >= 40:
        return "Pass"

    return "Fail"


result = check_pass(75)

print("Result :", result)


# ==================================================
# Example 7 : Returning Multiple Values
# ==================================================

def calculate_numbers(a, b):

    addition = a + b
    multiplication = a * b

    return addition, multiplication


sum_result, multiply_result = calculate_numbers(10, 5)

print("Sum :", sum_result)
print("Multiplication :", multiply_result)


# ==================================================
# Example 8 : Data Analyst Example
# ==================================================

def calculate_profit(revenue, cost):

    profit = revenue - cost

    return profit


profit = calculate_profit(100000, 65000)

print("Profit :", profit)


# ==================================================
# Example 9 : Profit Margin
# ==================================================

def calculate_profit_margin(revenue, cost):

    profit = revenue - cost
    profit_margin = (profit / revenue) * 100

    return profit_margin


margin = calculate_profit_margin(100000, 70000)

print("Profit Margin :", margin)