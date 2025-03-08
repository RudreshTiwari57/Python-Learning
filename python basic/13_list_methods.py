# List Methods
    # Python has a set of built-in methods that you can use on lists.
    #
    # Method	: Description
    # append()	: Adds an element at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

    # clear()	: Removes all the elements from the list\
thislist = ["apple", "banana", "cherry"]
print(thislist.index("banana"))

    # count()	: Returns the number of elements with the specified value
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist.count("Orange"))

    # extend()	: Add the elements of a list (or any iterable), to the end of the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

    # index()	: Returns the index of the first element with the specified value
thislist = ["apple", "banana", "cherry"]
print(thislist.index("banana"))

    # insert()	: Adds an element at the specified position

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

    # pop()	: Removes the element at the specified position
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Example
# Remove the last item:
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

    # remove()	: Removes the item with the specified value
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
    # reverse()	: Reverses the order of the list

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

    # sort()	: Sorts the list

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)