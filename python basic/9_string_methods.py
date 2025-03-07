# tring Methods
# Python has a set of built-in methods that you can use on strings.
#
# Note: All string methods return new values. They do not change the original string.
#
# Method
# capitalize()	: Converts the first character to upper case
b = "Hello, World!"
print(b.capitalize())


# count()	: Returns the number of times a specified value occurs in a string
b = "Hello, World!"
print(b.count("o"))




# endswith()	: Returns true if the string ends with the specified value
b = "Hello, World!"
print(b.endswith("ld"))

# index()	: Searches the string for a specified value and returns first the position of where it was found
b = "Hello, World!"
print(b.index("w"))



# isalnum()	: Returns True if all characters in the string are alphanumeric
b = "Hello, World!23"
print(b.isalnum())



# isalpha()	: Returns True if all characters in the string are in the alphabet
b = "Hello, World!"
print(b.isalpha())



# isdecimal()	: Returns True if all characters in the string are decimals
b = "23.3"
print(b.isdecimal())



# isdigit()	: Returns True if all characters in the string are digits
b = "12324"
print(b.isdigit())



# islower()	: Returns True if all characters in the string are lower case
b = "Hello, World!"
print(b.islower())



# isnumeric()	: Returns True if all characters in the string are numeric
b = "12324"
print(b.isnumeric())




# isupper()	: Returns True if all characters in the string are upper case
b = "Hello, World!"
print(b.isupper())



# join()	: Joins the elements of an iterable to the end of the string
b = "Hello, World!"
print(b.join("hello rudresh"))



# lower()	: Converts a string into lower case
b = "Hello, World!"
print(b.lower())



# lstrip()	: Returns a left trim version of the string
b = "Hello, World!"
print(b.lstrip("He"))



# replace()	: Returns a string where a specified value is replaced with a specified value
b = "Hello, World!"
print(b.replace("World","Rudresh"))



# rsplit()	: Splits the string at the specified separator, and returns a list
b = "Hello, World!"
print(b.capitalize())



# rstrip()	: Returns a right trim version of the string
b = "Hello, World!"
print(b.capitalize())



# split()	: Splits the string at the specified separator, and returns a list
b = "Hello, World!"
print(b.split("lo"))


# startswith()	: Returns true if the string starts with the specified value

b = "Hello, World!"
print(b.startswith("He"))


# title()	: Converts the first character of each word to upper case
b = "Hello, World!"
print(b.title())



# upper()	: Converts a string into upper case
b = "Hello, World!"
print(b.upper())


