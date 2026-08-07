"""
====================================================
Module      : 03 - Control Flow
Final Assignment
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# Question 1 : If Statement
# ==================================================

# Create:
#
# temperature = 32
#
# Print "Hot" if temperature is greater than 30.


# Write your code below 👇
temperature = 32
if temperature > 30:
    print("Hot")
    

# ==================================================
# Question 2 : If Else
# ==================================================

# Create:
#
# marks = 78
#
# Print:
# "Pass" if marks are 40 or above.
# Otherwise print "Fail".


# Write your code below 👇
marks = 78
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# ==================================================
# Question 3 : Elif
# ==================================================

# Create:
#
# marks = 86
#
# Print:
#
# Grade A : marks >= 90
# Grade B : marks >= 75
# Grade C : marks >= 60
# Fail     : otherwise


# Write your code below 👇
marks = 86
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# ==================================================
# Question 4 : For Loop
# ==================================================

# Create:
#
# fruits = ["Apple", "Banana", "Mango", "Orange"]
#
# Print every fruit.


# Write your code below 👇
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
    print(fruit)

# ==================================================
# Question 5 : For Loop + If
# ==================================================

# Create:
#
# marks = [35, 82, 65, 28, 90, 41]
#
# Print only passing marks (>=40).


# Write your code below 👇
marks = [35, 82, 65, 28, 90, 41]
for mark in marks:
    if mark >= 40:
        print(mark)

# ==================================================
# Question 6 : While Loop
# ==================================================

# Print numbers from 1 to 10 using a while loop.


# Write your code below 👇
count = 1
while count <= 10:
    print(count)
    count += 1



# ==================================================
# Question 7 : Break
# ==================================================

# Create:
#
# numbers = [5, 10, 15, 20, 25]
#
# Stop the loop when 20 is found.


# Write your code below 👇
numbers = [5, 10, 15, 20, 25]
for number in numbers:
    if number == 20:
        break
    print(number)


# ==================================================
# Question 8 : Continue
# ==================================================

# Create:
#
# numbers = [5, 10, 15, 20, 25]
#
# Skip printing 15.


# Write your code below 👇
numbers = [5, 10, 15, 20, 25]
for number in numbers:
    if number == 15:
        continue
    print(number)


# ==================================================
# Question 9 : Real Data Analyst Task
# ==================================================

# Monthly sales:
#
# sales = [42000, 55000, 48000, 62000, 39000]
#
# Print:
#
# Target Achieved : <sale>
#
# only for sales greater than or equal to 50000.


# Write your code below 👇
sales = [42000, 55000, 48000, 62000, 39000]
for sale in sales:
    if sale >= 50000:
        print("Target Achieved :", sale)


# ==================================================
# Question 10 : Mini Project
# ==================================================

# Student marks:
#
# marks = [78, 35, 92, 65, 28, 81, 49]
#
# Requirements:
#
# 1. Print every mark.
#
# 2. Print only passing marks.
#
# 3. Print Grade A for marks >=90
#    Grade B for marks >=75
#    Grade C for marks >=60
#    Fail otherwise.


# Write your code below 👇
marks = [78, 35, 92, 65, 28, 81, 49]
for mark in marks:
    if mark >= 90:
        print("Grade A")
    elif mark >= 75:
        print("Grade B")
    elif mark >= 60:
        print("Grade C")
    else:
        print("Fail")

