"""
====================================================
Module      : 02 - Collections
Final Assignment
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# Question 1 : Lists
# ==================================================

# Create a list of five programming languages.
#
# Print:
# - The complete list
# - First language
# - Last language
#
# Add "Git" to the list.
# Insert "HTML" at index 1.
# Remove "SQL".
# Print the updated list.
# Print the total number of items.


# Write your code below 👇
languages = ["Python", "SQL", "Excel", "Java", "C++"]
print("Complete List :", languages)
print("First Language :", languages[0])
print("Last Language :", languages[-1])

languages.append("Git")
languages.insert(1, "HTML")
languages.remove("SQL")

print("Updated List :", languages)
print("Total Items :", len(languages))


# ==================================================
# Question 2 : Lists
# ==================================================

# Create:
#
# sales = [25000, 18000, 32000, 27000, 30000]
#
# Print:
# - First three months
# - Last two months
# - Every second month
# - Reverse the list
#
# Sort the list in ascending order.
# Print the sorted list.


# Write your code below 👇
sales = [25000, 18000, 32000, 27000, 30000]
print("First Three Months :", sales[:3])    
print("Last Two Months :", sales[-2:])    
print("Every Second Month :", sales[::2])    
sales.reverse()
print("Reversed List :", sales)
sales.sort()
print("Sorted List :", sales)


# ==================================================
# Question 3 : Tuples
# ==================================================

# Create a tuple:
#
# employee = ("Rahul", "Finance", 55000, 4.5)
#
# Print:
# - Employee Name
# - Department
#
# Unpack the tuple into four variables.
# Print all four variables.
# Print the total number of values.


# Write your code below 👇
employee = ("Rahul", "Finance", 55000, 4.5)
print("Employee Name :", employee[0])
print("Department :", employee[1])

name, department, salary, rating = employee
print("Name :", name)
print("Department :", department)
print("Salary :", salary)
print("Rating :", rating)
print("Total Values :", len(employee))


# ==================================================
# Question 4 : Sets
# ==================================================

# Create:
#
# skills_1 = {"Python", "SQL", "Excel"}
#
# skills_2 = {"SQL", "Power BI", "Tableau"}
#
# Print:
# - Union
# - Intersection
# - Difference
#
# Add "Git" to skills_1.
# Remove "Excel" from skills_1.
# Print the updated set.


# Write your code below 👇
skills_1 = {"Python", "SQL", "Excel"}
skills_2 = {"SQL", "Power BI", "Tableau"}

print("Union :", skills_1.union(skills_2))
print("Intersection :", skills_1.intersection(skills_2))
print("Difference :", skills_1.difference(skills_2))

skills_1.add("Git")
skills_1.remove("Excel")
print("Updated Set :", skills_1)


# ==================================================
# Question 5 : Dictionaries
# ==================================================

# Create a dictionary:
#
# student = {
#     "name": "Prawin",
#     "age": 21,
#     "course": "BCA",
#     "cgpa": 8.7
# }
#
# Print:
# - Student Name
# - CGPA
#
# Update age to 22.
# Add:
# "city": "Bangalore"
#
# Delete "course".
#
# Print:
# - Dictionary
# - Keys
# - Values
# - Items


# Write your code below 👇
student = {
    "name": "Prawin",
    "age": 21,
    "course": "BCA",
    "cgpa": 8.7
}

print("Student Name :", student["name"])
print("CGPA :", student["cgpa"])

student["age"] = 22
student["city"] = "Bangalore"
del student["course"]

print("Updated Dictionary :", student)
print("Keys :", student.keys())
print("Values :", student.values())
print("Items :", student.items())


# ==================================================
# Question 6 : Real Data Analyst Scenario
# ==================================================

# Create:
#
# employees = ["Rahul", "Amit", "Rahul", "Neha", "Amit", "Prawin"]
#
# Convert the list into a set.
#
# Print:
# - Original list
# - Unique employee names
# - Total unique employees


# Write your code below 👇
employees = ["Rahul", "Amit", "Rahul", "Neha", "Amit", "Prawin"]
unique_employees = set(employees)

print("Original List :", employees)
print("Unique Employee Names :", unique_employees)
print("Total Unique Employees :", len(unique_employees))


# ==================================================
# Question 7 : Mini Project
# ==================================================

# Create a dictionary for one product:
#
# Product Name
# Price
# Quantity
#
# Calculate:
#
# Total Price = Price × Quantity
#
# Print:
#
# ========== Product Summary ==========
# Product :
# Price :
# Quantity :
# Total Price :


# Write your code below 👇
product = {
    "name": "Laptop",
    "price": 50000,
    "quantity": 5
}

total_price = product["price"] * product["quantity"]

print("========== Product Summary ==========")
print("Product :", product["name"])
print("Price :", product["price"])
print("Quantity :", product["quantity"])
print("Total Price :", total_price)