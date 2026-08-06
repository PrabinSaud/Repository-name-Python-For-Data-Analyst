"""
====================================================
Module      : 02 - Collections
Lesson      : 04
Topic       : Dictionaries
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a Dictionary?
# ==================================================

# A dictionary stores data in key-value pairs.
# Dictionaries are ordered, mutable, and do not allow duplicate keys.


# ==================================================
# Example 1 : Creating a Dictionary
# ==================================================

student = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA"
}

print(student)


# ==================================================
# Example 2 : Accessing Values
# ==================================================

print("Name   :", student["name"])
print("Age    :", student["age"])


# ==================================================
# Example 3 : Adding a New Key
# ==================================================

student["cgpa"] = 8.5

print(student)


# ==================================================
# Example 4 : Updating a Value
# ==================================================

student["age"] = 22

print(student)


# ==================================================
# Example 5 : Removing a Key
# ==================================================

del student["course"]

print(student)


# ==================================================
# Example 6 : Dictionary Length
# ==================================================

print("Total Keys :", len(student))


# ==================================================
# Example 7 : keys()
# ==================================================

print(student.keys())


# ==================================================
# Example 8 : values()
# ==================================================

print(student.values())


# ==================================================
# Example 9 : items()
# ==================================================

print(student.items())