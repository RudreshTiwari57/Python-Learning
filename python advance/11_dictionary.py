# A dictionary in Python is an unordered collection of key-value pairs. It is mutable, meaning it can be changed after creation, and it is optimized for fast lookups.
#
# ---------------------------------1. Creating a Dictionary-------------------------------------------------

    # Dictionaries are defined using {} or the dict() constructor.
    #
    # Example: Creating a Dictionary

# Using curly braces
student = {
    "name": "Rudresh",
    "age": 25,
    "course": "Computer Science"
}

# Using dict() function
person = dict(name="Alice", age=30, city="New York")

print(student)
print(person)



# ------------------------------------------------------------2. Accessing Dictionary Values-----------------------------------------------
#
#
# You can access values using keys.


print(student["name"])  # Output: Rudresh
print(student.get("age"))  # Output: 25


# If a key doesn’t exist:
print(student.get("grade", "Not Available"))  # Output: Not Available


# --------------------------------------------------3. Adding and Updating Elements---------------------------------------------------------

student["grade"] = "A"  # Adding a new key-value pair
student["age"] = 26  # Updating an existing value

print(student)


# --------------------------------------------------------4. Removing Elements------------------------------------------------------

del student["age"]  # Removes a specific key
print(student)

grade = student.pop("grade")  # Removes and returns the value
print(grade)

student.clear()  # Removes all elements
print(student)  # Output: {}


# ------------------------------------------------------5. Dictionary Methods-----------------------------------------------
#                            ------------------------------------------------------------------------------------------
#                            | Method	        |       Description	            |   Example                           |
#                            ------------------------------------------------------------------------------------------
#                            | dict.keys()	    |     Returns all keys	        |   student.keys()                    |
#                            | dict.values()	|   Returns all values	        |   student.values()                  |
#                            | dict.items()	    |   Returns all key-value pairs	|   student.items()                   |
#                            | dict.update()	|   Merges another dictionary	|   student.update({"grade": "B"})    |
#                            | dict.copy()	    |   Creates a shallow copy	    |   new_dict = student.copy()         |
#                            ------------------------------------------------------------------------------------------



# Example: Iterating Over a Dictionary

for key, value in student.items():
    print(key, ":", value)


# -----------------------------------------------------------------6. Checking for Key Existence-----------------------------------------

if "name" in student:
    print("Name exists in dictionary")


# ------------------------------------------------------------7. Dictionary Comprehension-----------------------------------------------------


squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# --------------------------------------------------8. Nested Dictionaries---------------------------------------------------------------------
# Dictionaries can contain other dictionaries.

company = {
    "CEO": {"name": "Alice", "age": 45},
    "CTO": {"name": "Bob", "age": 40}
}

print(company["CEO"]["name"])  # Output: Alice

# ------------------------------------------------------------------# 10. Merging Two Dictionaries----------------------------------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Method 1: Using update()
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

# Method 2: Using dictionary unpacking (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(merged_dict)


# ------------------------------------------------------------------11. Sorting a Dictionary-------------------------------------------------

data = {"banana": 3, "apple": 5, "orange": 2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)  # Output: {'orange': 2, 'banana': 3, 'apple': 5}


# ---------------------------------------------------12. Default Dictionary (collections.defaultdict)-----------------------------------------
#
# If a key does not exist, defaultdict provides a default value.

from collections import defaultdict

dd = defaultdict(int)
dd["a"] += 1
print(dd["a"])  # Output: 1
print(dd["b"])  # Output: 0 (default int is 0)


# -----------------------------------------------------------13. Ordered Dictionary (collections.OrderedDict)-----------------------------------
#
# Maintains the order of insertion (Python 3.7+ maintains order by default).

from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# ---------------------------------------------------------------14. Dictionary Performance-----------------------------------------------
#
#
# Dictionaries in Python are implemented as hash tables, providing average O(1) time complexity for lookups, insertions, and deletions.