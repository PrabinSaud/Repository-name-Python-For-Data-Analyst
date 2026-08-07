"""
Module 03 - Control Flow
Practice
"""

# ==========================================
# Topic 1 : If Statement
# ==========================================

# Practice 1
#
# Create:
# age = 25
#
# Print "Adult" if age is 18 or above.
age = 25
if age >= 18:
    print("Adult")


# Practice 2
#
# Create:
# marks = 35
#
# Print "Pass" if marks are 40 or above.
marks = 35
if marks >= 40:
    print("Pass")



# Practice 3
#
# Create:
# salary = 75000
#
# Print "Bonus Eligible" if salary is greater than 60000.
salary = 75000
if salary > 60000:
    print("Bonus Eligible")



# Practice 4
#
# Create:
# skills = ["Python", "SQL", "Excel"]
#
# Print "SQL Found" if SQL exists in the list.
skills = ["Python", "SQL", "Excel"]
if "SQL" in skills:
    print("SQL Found")  

    # ==========================================
# Topic 2 : If Else
# ==========================================

# Practice 5
#
# Create:
# marks = 82
#
# Print:
# "Pass" if marks are 40 or above,
# otherwise print "Fail".
marks = 82
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Practice 6
#
# Create:
# age = 15
#
# Print:
# "Adult" if age is 18 or above,
# otherwise print "Minor".
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")


# Practice 7
#
# Create:
# number = 28
#
# Print:
# "Even" if the number is even,
# otherwise print "Odd".
number = 28
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Practice 8
#
# Create:
# salary = 55000
# target = 50000
#
# Print:
# "Target Achieved" or "Target Missed".
salary = 55000
target = 50000
if salary >= target:
    print("Target Achieved")    
else:
    print("Target Missed")

# ==========================================
# Topic 3 : Elif
# ==========================================

# Practice 9
#
# Create:
# marks = 92
#
# Print:
# A if marks >= 90
# B if marks >= 75
# C if marks >= 60
# Otherwise Fail
marks = 92
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

# Practice 10
#
# Create:
# age = 35
#
# Print:
# Child
# Teenager
# Adult
# Senior Citizen
age = 35
if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Practice 11
#
# Create:
# salary = 65000
#
# Print:
# High
# Medium
# Low
salary = 65000
if salary >= 100000:
    print("High")
elif salary >= 50000:
    print("Medium")
else:
    print("Low")

# Practice 12
#
# Create:
# purchase = 12000
#
# Print:
# 20% Discount
# 10% Discount
# No Discount
purchase = 12000
if purchase >= 10000:
    print("20% Discount")
elif purchase >= 5000:
    print("10% Discount")
else:
    print("No Discount")

# ==========================================
# Topic 4 : For Loop
# ==========================================

# Practice 13
#
# Create:
# fruits = ["Apple", "Banana", "Mango"]
#
# Print every fruit.
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)    

# Practice 14
#
# Create:
# numbers = [5, 10, 15, 20]
#
# Print each number multiplied by 3.
numbers = [5, 10, 15, 20]
for number in numbers:
    print(number * 3)

# Practice 15
#
# Create:
# marks = [35, 80, 55, 92, 28]
#
# Print only marks that are greater than or equal to 40.
marks = [35, 80, 55, 92, 28]
for mark in marks:
    if mark >= 40:
        print(mark)

# Practice 16
#
# Create:
# sales = [25000, 45000, 60000, 38000]
#
# Print "Target Achieved" only for sales greater than or equal to 50000.
sales = [25000, 45000, 60000, 38000]
for sale in sales:
    if sale >= 50000:
        print("Target Achieved")