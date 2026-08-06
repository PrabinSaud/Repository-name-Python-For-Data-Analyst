"""
Practice - Lists
"""

# ==================================================
# Practice 1
# ==================================================

# Create a list of five cities.
# Print the first city.
# Print the last city.


# Write your code below 👇
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print("First City :", cities[0])
print("Last City  :", cities[-1])


# ==================================================
# Practice 2
# ==================================================

# Create a list:
# [100, 200, 300]
#
# Add 400.
# Print the updated list.


# Write your code below 👇
list = [100, 200, 300]
list.append(400)
print(list)


# ==================================================
# Practice 3
# ==================================================

# Create a list:
# ["Python", "SQL", "Excel"]
#
# Remove "SQL".
# Print the updated list.


# Write your code below 👇
languages = ["Python", "SQL", "Excel"]
languages.remove("SQL")
print(languages)

# ==========================================
# Topic 1 : Lists (Part 2)
# ==========================================

# Practice 6
#
# Create:
# fruits = ["Apple", "Banana"]
#
# Insert "Orange" at index 1.
fruits = ["Apple", "Banana"]
fruits.insert(1, "Orange")  
print(fruits)


# Practice 7
#
# Create:
# list1 = [10,20]
# list2 = [30,40]
#
# Combine both lists.
list1 = [10, 20]
list2 = [30, 40]
list1.extend(list2)
print(list1)



# Practice 8
#
# Create:
# numbers = [100,200,300]
#
# Remove the last number using pop().
# Print the removed value.
# Print the updated list.
numbers = [100, 200, 300]
removed_value = numbers.pop()
print("Removed Value :", removed_value)
print("Updated List :", numbers)

# Practice 9
#
# Sort:
#
# [45,12,89,32,56]

marks = [45, 12, 89, 32, 56]
marks.sort()
print("Sorted :", marks)

# Practice 10
#
# Reverse:
#
# [10,20,30,40,50]
numbers = [10, 20, 30, 40, 50]  
numbers.reverse()
print("Reversed :", numbers)    


# ==========================================
# Topic 2 : Tuples
# ==========================================

# Practice 11
#
# Create a tuple of five colors.
# Print the first and last color.
colors = ("Red", "Green", "Blue", "Yellow", "Purple")
print("First Color :", colors[0])
print("Last Color  :", colors[-1])

# Practice 12
#
# Create:
# numbers = (10, 20, 30, 10, 40, 10)
#
# Count how many times 10 appears.
numbers = (10, 20, 30, 10, 40, 10)
print("Count of 10 :", numbers.count(10))


# Practice 13
#
# Create:
# employee = ("Rahul", "HR", 45000)
#
# Unpack the tuple and print each value.

employee = ("Rahul", "HR", 45000)
name, department, salary = employee
print("Name       :", name)
print("Department :", department)
print("Salary     :", salary)

# Practice 14
#
# Create a tuple of four cities.
# Print the length of the tuple.

cities = ("New York", "Los Angeles", "Chicago", "Houston")
print("Length of Tuple :", len(cities))

# Practice 15
#
# Create:
# skills = ("Python", "SQL", "Excel")
#
# Print the index of "SQL".
skills = ("Python", "SQL", "Excel")
print("Index of SQL :", skills.index("SQL"))

# ==========================================
# Topic 3 : Sets
# ==========================================

# Practice 16
#
# Create a set of five fruits.
# Print the set.
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
print(fruits)

# Practice 17
#
# Create:
# numbers = {10, 20, 30}
#
# Add 40.
# Print the updated set.
numbers = {10, 20, 30}
numbers.add(40)
print("Updated Set :", numbers)


# Practice 18
#
# Remove "Python" from:
#
# {"Python", "SQL", "Excel"}
skills = {"Python", "SQL", "Excel"}
skills.remove("Python")
print("Updated Set :", skills)


# Practice 19
#
# Find the common values between:
#
# {1,2,3,4}
#
# and
#
# {3,4,5,6}
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common_values = set1.intersection(set2)
print("Common Values :", common_values)

# Practice 20
#
# Find all unique values from:
#
# {"Python","SQL"}
#
# and
#
# {"SQL","Power BI"}
set1 = {"Python", "SQL"}
set2 = {"SQL", "Power BI"}
unique_values = set1.union(set2)
print("Unique Values :", unique_values)


# ==========================================
# Topic 4 : Dictionaries
# ==========================================

# Practice 21
#
# Create a dictionary with:
# name, age, city
# Print the dictionary.
dict = {
    "name": "Rahul",
    "age": 21,
    "city": "New York"
}
print("Dictionary :", dict)


# Practice 22
#
# Print only the student's name.
print("Name :", dict["name"])


# Practice 23
#
# Add a new key:
# "course": "BCA"
dict["course"] = "BCA"
print("Updated Dictionary :", dict) 

# Practice 24
#
# Update the age.
dict["age"] = 22
print("Updated Age :", dict["age"]) 

# Practice 25
#
# Print:
# keys()
# values()
# items()
print("Keys :", dict.keys())
print("Values :", dict.values())
print("Items :", dict.items())
