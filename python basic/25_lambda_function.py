# Lambda Functions in Python
    # A lambda function in Python is a small anonymous function (i.e., a function without a name). It is used for writing quick, single-expression functions in a concise way.
    #
    # Syntax of Lambda Function
        #
        # lambda arguments: expression


        # lambda – Keyword to define a lambda function.
        # arguments – Input parameters (just like normal functions).
        # expression – The operation to perform and return (only a single expression allowed).
        # Example of a Simple Lambda Function

square = lambda x: x ** 2
print(square(5))  # Output: 25
# 🔹 Equivalent to:


def square(x):
    return x ** 2
# Why Use Lambda Functions?
#     Concise and readable for simple operations.
#     Used in higher-order functions like map(), filter(), and sorted().
#     No need to explicitly define a function using def.

# Examples of Lambda Functions
# Lambda with Multiple Arguments

add = lambda x, y: x + y
print(add(10, 20))  # Output: 30

# 🔹 Equivalent to:

def add(x, y):
    return x + y


# Lambda in map()
# The map() function applies a function to each item in an iterable.


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Equivalent to:


def square(x):
    return x ** 2

squared = list(map(square, numbers))
# Lambda in filter()
# The filter() function filters elements based on a condition.

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

# Equivalent to:

def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))

# Lambda in sorted()
# The sorted() function uses a lambda function for custom sorting.

students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])  # Sort by age
print(sorted_students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]


# Limitations of Lambda Functions
#     Cannot have multiple expressions (only a single expression allowed).
#     Hard to debug since they are anonymous (no function name).
#     Not ideal for complex logic—better to use a def function.
#
# When to Use Lambda Functions?
#     When you need a quick, throwaway function (e.g., inside map(), filter(), etc.).
#     When defining a function in a single line makes the code cleaner.
#     When a full def function would be unnecessary overhead.