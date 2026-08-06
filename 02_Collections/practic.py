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
