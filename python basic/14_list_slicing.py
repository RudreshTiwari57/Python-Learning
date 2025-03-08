# Python List Slicing
    # Last Updated : 08 Mar, 2025
    # Python list slicing is fundamental concept that let us easily access specific elements in a list. In this article, we’ll learn the syntax and how to use both positive and negative indexing for slicing with examples.
    #
    # Example: Get the items from a list starting at position 1 and ending at position 4 (exclusive).


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4])

# ------------------------------------------------Python List Slicing Syntax-------------------------------------
# list_name[start : end : step]
#
#
# Parameters:
#
# start (optional): Index to begin the slice (inclusive). Defaults to 0 if omitted.
# end (optional): Index to end the slice (exclusive). Defaults to the length of list if omitted.
# step (optional): Step size, specifying the interval between elements. Defaults to 1 if omitted

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get all elements in the list
print(a[::])
print(a[:])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index 2
# to the end of the list
b = a[2:]
print(b)

# Get elements starting from index 0
# to index 3 (excluding 3th index)
c = a[:3]
print(c)
#
#----------------------------- Get all items between two positions--------------------------------------
# To extract elements between two specific positions, specify both the start and end indices

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 1
# to index 4 (excluding index 4)
b = a[1:4]
print(b)

# ----------------------------Get items at specified intervals------------------------------------------
# To extract elements at specific intervals, use the step parameter.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every second element from the list
# starting from the beginning
b = a[::2]
print(b)

# Get every third element from the list
# starting from index 1 to 8(exclusive)
c = a[1:8:3]
print(c)


# ------------------------------Reverse a list using slicing----------------------------------------
# In this example, we’ll reverse the entire list using a slicing trick. By using a negative step value, we can move through the list in reverse order.




a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get the entire list using negative step
b = a[::-1]
print(b)

# Output
[9, 8, 7, 6, 5, 4, 3, 2, 1]
# Explanation:
# The negative step (-1) indicates that Python should traverse the list in reverse order, starting from the end. The slice a[::-1] starts from the end of the list and moves to the beginning which result in reversing list.
# It’s a quick and easy way to get the list in reverse without changing the original list.



# --------------------------------------Negative Indexing------------------------------------------
# Negative indexing is useful for accessing elements from the end of the list. The last element has an index of -1, the second last element -2, and so on.
#
# Extract elements using negative indices
# This example shows how to use negative numbers to access elements from the list starting from the end. Negative indexing makes it easy to get items without needing to know the exact length of the list.




a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index -2
# to end of list
b = a[-2:]
print(b)

# Get elements starting from index 0
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)

# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)

# Get every 2nd elements from index -8
# to -1 (excluding index -1)
e = a[-8:-1:2]
print(e)
#
# Output
[8, 9]
[1, 2, 3, 4, 5, 6]
[6, 7, 8]
[2, 4, 6, 8]