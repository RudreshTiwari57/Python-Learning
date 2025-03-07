# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
#
# 'hello' is the same as "hello".
#
# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
#
# Square brackets can be used to access elements of the string.


# Example
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])


# String Length
# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))