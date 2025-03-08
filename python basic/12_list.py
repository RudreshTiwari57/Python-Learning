# List
    # Lists are used to store multiple items in a single variable.
    #
    # Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
    #
    # Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items
#     List items are ordered, changeable, and allow duplicate values.
#
#     List items are indexed, the first item has index [0], the second item has index [1] etc.
#
# Ordered
#     When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#
#     If you add new items to a list, the new items will be placed at the end of the list.
#
#
# Changeable
#     The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#
# Allow Duplicates
#     Since lists are indexed, lists can have items with the same value:
#
#     Example
#         Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Items - Data Types
#     List items can be of any data type:
#
#     Example
#     String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
    #
    # Example
    # A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

# ----------------------------------------- Access Items --------------------------------------------------------------------

# Access Items
    # List items are indexed and you can access them by referring to the index number:
    # Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
#     Negative indexing means start from the end
#
#     -1 refers to the last item, -2 refers to the second last item etc.
#
#     Example
#     Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# ----------------------------------------- Change Item Value --------------------------------------------------------------------

# Change Item Value
    # To change the value of a specific item, refer to the index number:
    #
    # Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change a Range of Item Values
    # To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
    #
    # Example
    # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
    # To insert a new list item, without replacing any of the existing values, we can use the insert() method.
    #
    # The insert() method inserts an item at the specified index:
    #
    # Example
    # Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# ----------------------------------------- adding another list --------------------------------------------------------------------

# Append Items
    # To add an item to the end of the list, use the append() method:
    #
    # ExampleGet your own Python Server
    # Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
#     To append elements from another list to the current list, use the extend() method.
#
#     Example
#     Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable
#     The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
#
#     Example
#     Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# ----------------------------------------- removing --------------------------------------------------------------------

# Remove Specified Item
    # The remove() method removes the specified item.
    #
    # ExampleGet your own Python Server
    # Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
    # The pop() method removes the specified index.
    # Example
    # Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# Example
# Remove the last item:
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


# The del keyword also removes the specified index:
    #
    # Example
    # Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
#
# Example
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
#     The clear() method empties the list.
#
#     The list still remains, but it has no content.
#
#     Example
#     Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# ----------------------------------------- sorting --------------------------------------------------------------------
# Sort List Alphanumerically
    # List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
    #
    # ExampleGet your own Python Server
    # Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending
    # To sort descending, use the keyword argument reverse = True:
    #
    # Example
    # Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Case Insensitive Sort
    # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
    #
    # Example
    # Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# Reverse Order
    # What if you want to reverse the order of a list, regardless of the alphabet?
    #
    # The reverse() method reverses the current sorting order of the elements.
    #
    # Example
    # Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)