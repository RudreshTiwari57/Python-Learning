# Variables
# Variables are containers for storing data values.
#
# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# Variables do not need to be declared with any particular type, and
# can even change type after they have been set.



# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))


# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#the starting and ending comas should be same or else python will throw error

# Case-Sensitive
# Variable names are case-sensitive.

a = 4
A = "Sally"
#A will not overwrite a