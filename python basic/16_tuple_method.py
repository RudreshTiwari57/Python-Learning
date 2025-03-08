# Tuple Methods
# Python has two built-in methods that you can use on tuples.
#
# Method	: Description
# count()	: Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index()	: Searches the tuple for a specified value and returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(5)
print(x)