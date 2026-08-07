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