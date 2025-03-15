# A set in Python is an unordered collection of unique elements. It is mutable but only stores immutable data types
# (numbers, strings, tuples). Sets are useful for removing duplicates, performing mathematical operations like union and
# intersection, and fast lookups.


# -----------------------------------------------------------1. Creating a Set-----------------------------------------------------------------
# Sets can be created using {} or the set() constructor.
#
# Example: Creating a Set

# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() function
colors = set(["red", "green", "blue"])

print(fruits)
print(colors)


# -------------------------------------------------------------------2. Properties of Sets----------------------------------------------------

               # a.  Unordered - Elements have no specific order.
               # b.  Unique Elements - Duplicates are automatically removed.
               # c.  Mutable - You can add or remove elements.



#--------------------------------------------------------------- 3. Adding and Removing Elements --------------------------------------------------

numbers = {1, 2, 3}

# Adding a single element
numbers.add(4)

# Adding multiple elements
numbers.update([5, 6, 7])

# Removing an element
numbers.remove(3)  # Raises an error if the element is not found

# Removing an element safely
numbers.discard(8)  # Does not raise an error if the element is not found

# Removing and returning a random element
removed_item = numbers.pop()

# Clearing all elements
numbers.clear()

print(numbers)


# -------------------------------------------------------4. Set Operations (Mathematical Operations)---------------------------------------------
#
# Python sets support mathematical operations like union, intersection, and difference.
#
# ------------------------------------------ a) Union (| or union())
#
# Returns all unique elements from both sets.

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Output: {1, 2, 3, 4, 5}
print(A.union(B))


# ------------------------------------------ b) Intersection (& or intersection())

# Returns elements present in both sets.
print(A & B)  # Output: {3}
print(A.intersection(B))


# ------------------------------------------c) Difference (- or difference())


# Returns elements in one set but not in the other.

print(A - B)  # Output: {1, 2}
print(A.difference(B))

# ------------------------------------- d) Symmetric Difference (^ or symmetric_difference())
#
# Returns elements in either set but not both.

print(A ^ B)  # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))


# ------------------------------------------------------------5. Checking Subsets and Supersets-----------------------------------------------

X = {1, 2, 3}
Y = {1, 2}

print(Y.issubset(X))  # True (Y ⊆ X)
print(X.issuperset(Y))  # True (X ⊇ Y)

# -------------------------------------------------------------------6. Checking for Element Existence-----------------------------------------

fruits = {"apple", "banana", "cherry"}

print("banana" in fruits)  # True
print("grape" not in fruits)  # True


# ----------------------------------------------------------7. Converting Lists to Sets (Removing Duplicates)-----------------------------------------


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)

print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# --------------------------------------------------------8. Frozen Sets (Immutable Sets)-------------------------------------------------------
#
# A frozenset is an immutable version of a set. You cannot add or remove elements.

fs = frozenset([1, 2, 3, 4])

# fs.add(5)  # Error: Frozen set does not support modification
print(fs)


# ----------------------------------------------------9. Set Comprehension------------------------------------------------------------------
#
# Similar to list comprehension but for sets.

squares = {x**2 for x in range(1, 6)}
print(squares)  # Output: {1, 4, 9, 16, 25}


# -----------------------------------------------10. Real-World Use Case: Finding Unique Words in a Sentence------------------------------------

text = "Python is great and Python is easy"
unique_words = set(text.split())

print(unique_words)  # Output: {'great', 'is', 'Python', 'and', 'easy'}

# --------------------------------------------------------------11. Performance of Sets vs Lists----------------------------


        # Faster lookups – Checking for an item in a set is O(1), while in a list it’s O(n).
        # Faster removal – Removing an item is faster in a set compared to a list.