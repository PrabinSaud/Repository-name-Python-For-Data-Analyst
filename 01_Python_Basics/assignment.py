"""
====================================================
Module      : 01 - Python Basics
Final Assignment
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# Question 1 : Variables
# ==================================================

# Create variables for:
# - Company Name
# - Employee Name
# - Department
# - Salary
# - Permanent Employee (True/False)
#
# Print all the values.

# Write your code below 👇
print("Company Name : ","ABC Pvt. Ltd.")
print("Employee Name : ","Prabin Saud")
print("Department : ","IT")
print("Salary : ",50000)
print("Permanent Employee : ",True)

# ==================================================
# Question 2 : Data Types
# ==================================================

# Create variables for:
# - Movie Name
# - Release Year
# - IMDb Rating
# - Is Available on Netflix
#
# Print:
# - Value
# - Data Type

# Write your code below 👇
movie_name = "Inception"
release_year = 2010
imdb_rating = 8.8
is_available_on_netflix = True

print("Movie Name : ",movie_name, type(movie_name))
print("Release Year : ",release_year, type(release_year))
print("IMDb Rating : ",imdb_rating, type(imdb_rating))
print("Available on Netflix : ",is_available_on_netflix, type(is_available_on_netflix))


# ==================================================
# Question 3 : Type Conversion
# ==================================================

# A product price is stored as:
#
# price = "1499"
#
# Convert it to an integer.
# Add 500.
# Print the final price.

# Write your code below 👇
price = "1499"
price = int(price)
price += 500
print("Final Price : ",price)


# ==================================================
# Question 4 : Type Conversion
# ==================================================

# Convert:
#
# "100" -> int
# 250 -> float
# 8.95 -> int
#
# Print the converted values and their data types.

# Write your code below 👇
price1 = "100"  
price1 = int(price1)
print("Converted Value : ",price1, type(price1))

price2 = 250
price2 = float(price2)
print("Converted Value : ",price2, type(price2))

price3 = 8.95
price3 = int(price3)
print("Converted Value : ",price3, type(price3))


# ==================================================
# Question 5 : Arithmetic Operators
# ==================================================

# Create:
#
# num1 = 25
# num2 = 8
#
# Print:
# Addition
# Subtraction
# Multiplication
# Division
# Floor Division
# Modulus
# Exponent

# Write your code below 👇
num1 = 25
num2 = 8
print("Addition : ", num1 + num2)
print("Subtraction : ", num1 - num2)        
print("Multiplication : ", num1 * num2)
print("Division : ", num1 / num2)   
print("Floor Division : ", num1 // num2)
print("Modulus : ", num1 % num2)
print("Exponent : ", num1 ** num2)


# ==================================================
# Question 6 : Comparison Operators
# ==================================================

# Compare:
#
# 100 and 75
#
# Print:
# >
# <
# ==
# !=
# >=
# <=

# Write your code below 👇
num1 = 100
num2 = 75
print("Greater than : ", num1 > num2)
print("Less than : ", num1 < num2)
print("Equal to : ", num1 == num2)
print("Not equal to : ", num1 != num2)
print("Greater than or equal to : ", num1 >= num2)
print("Less than or equal to : ", num1 <= num2)


# ==================================================
# Question 7 : Logical Operators
# ==================================================

# age = 22
# salary = 50000
#
# Check:
#
# age > 18 and salary > 30000
#
# age > 25 or salary > 30000
#
# not age > 25

# Write your code below 👇
age = 22
salary = 50000
print("Age > 18 and Salary > 30000 : ", age > 18 and salary > 30000)
print("Age > 25 or Salary > 30000 : ", age > 25 or salary > 30000)
print("Not Age > 25 : ",  not age > 25)  
    


# ==================================================
# Question 8 : Membership Operators
# ==================================================

# Create:
#
# skills = ["Python", "SQL", "Excel", "Git"]
#
# Check:
#
# "Python" in skills
# "Tableau" in skills
# "Git" not in skills

# Write your code below 👇
skills = ["Python", "SQL", "Excel", "Git"]
print("Python in skills :","Python" in skills)
print("Tableau in skills :","Tableau" in skills)
print("Git not in skills :","Git" not in skills)


# ==================================================
# Question 9 : Input & Output
# ==================================================

# Ask the user to enter:
#
# - Student Name
# - Course
# - Semester
# - CGPA
#
# Print the student profile.

# Write your code below 👇
student_name = input("Enter Student Name: ")
course = input("Enter Course: ")
semester = input("Enter Semester: ")
cgpa = float(input("Enter CGPA: "))

print("\n========== Student Profile ==========")
print("Name       : ", student_name)
print("Course     : ", course)
print("Semester   : ", semester)
print("CGPA       : ", cgpa)

# ==================================================
# Question 10 : Mini Project
# ==================================================

# Create a simple Employee Information Program.
#
# Ask the user to enter:
#
# Employee Name
# Department
# Salary
# Experience
#
# Print:
#
# ========== Employee Details ==========
# Name       :
# Department :
# Salary     :
# Experience :

# Write your code below 👇
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = float(input("Enter Salary: "))
experience = int(input("Enter Experience (in years): "))

print("\n========== Employee Details ==========")
print("Name       : ", employee_name)
print("Department : ", department)
print("Salary     : ", salary)
print("Experience : ", experience)