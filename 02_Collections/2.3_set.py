"""
====================================================
Module      : 02 - Collections
Lesson      : 03
Topic       : Sets
Author      : Prabin Saud
Repository  : Python-For-Data-Analyst
====================================================
"""

# ==================================================
# What is a Set?
# ==================================================

# A set stores multiple unique values.
# Sets are unordered, mutable, and do not allow duplicates.


# ==================================================
# Example 1 : Creating a Set
# ==================================================

fruits = {"Apple", "Banana", "Mango"}

print("Fruits :", fruits)


# ==================================================
# Example 2 : Duplicate Values
# ==================================================

numbers = {10, 20, 10, 30, 20}

print("Numbers :", numbers)


# ==================================================
# Example 3 : add()
# ==================================================

fruits.add("Orange")

print("After Add :", fruits)


# ==================================================
# Example 4 : remove()
# ==================================================

fruits.remove("Banana")

print("After Remove :", fruits)


# ==================================================
# Example 5 : discard()
# ==================================================

fruits.discard("Apple")

print("After Discard :", fruits)


# ==================================================
# Example 6 : Length
# ==================================================

print("Total Items :", len(fruits))


# ==================================================
# Example 7 : Union
# ==================================================

python_skills = {"Python", "SQL", "Excel"}

tools = {"Excel", "Power BI", "Tableau"}

print("Union :", python_skills.union(tools))


# ==================================================
# Example 8 : Intersection
# ==================================================

print("Intersection :", python_skills.intersection(tools))


# ==================================================
# Example 9 : Difference
# ==================================================

print("Difference :", python_skills.difference(tools))