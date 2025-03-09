# In Python, scope refers to the region of code where a particular variable is accessible. Understanding scope is crucial to writing efficient, error-free programs.
#
    # Types of Scope in Python
    # Python has four types of scope, which follow the LEGB Rule:
    #
    # ---------------------------------------------Local Scope--------------------------------------------


# A variable defined inside a function has a local scope, meaning it is accessible only within that
# function. It cannot be accessed outside the function.
#
# Example:

def my_function():
    x = 10  # Local variable
    print(x)  # This works fine inside the function

my_function()
print(x)  # ERROR: x is not defined outside the function
# 🔹 x is local to my_function() and is not recognized outside.


    # --------------------------------------------Enclosing Scope-----------------------------------------
#
# If a function is nested inside another function, the inner function can access variables
# from its enclosing (outer) function. This is called enclosing scope.
#
# Example:

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        print(y)  # Accessing 'y' from the outer function

    inner_function()

outer_function()
# 🔹 y belongs to outer_function() and is accessible inside inner_function(),
# but not outside outer_function().


    # ---------------------------------------------Global Scope-------------------------------------------

# A variable declared outside any function or class is in the global scope and can be accessed
# from anywhere in the script.
#
# Example:

z = 30  # Global variable

def my_function():
    print(z)  # Accessible inside the function

my_function()
print(z)  # Accessible outside the function too


# z is global, meaning it can be used both inside and outside functions.
#
# ----------------------------Modifying a Global Variable Inside a Function----------------------
# By default, Python treats variables inside a function as local. To modify a global variable
# inside a function, use the global keyword.


a = 100  # Global variable

def modify_global():
    global a  # Declaring 'a' as global
    a = 200  # Modifying global variable

modify_global()
print(a)  # Output: 200 (global variable changed)
# Without global, a = 200 inside modify_global() would create a new local variable, leaving
# the global a unchanged.
    # --------------------------------------------Built-in Scope------------------------------------------


# Python has many built-in functions and keywords that are always available, like print(), len(), and range(). These exist in the built-in scope.
#
# Example:

print(len("Python"))  # Output: 6


# Here, len() is a built-in function, accessible from anywhere.
#
# We should not override built-in names:

len = 10  # BAD PRACTICE: Overriding built-in function
print(len("Python"))  # ERROR: 'int' object is not callable


# ------------------------------Scope Resolution: The LEGB Rule-------------------------------------------


# When Python encounters a variable, it follows this order to resolve it:
#
# Local – Check inside the function.
# Enclosing – Check inside the outer (enclosing) function if it's a nested function.
# Global – Check the global variables.
# Built-in – Check Python's built-in functions.
# If Python cannot find the variable in any of these scopes, it raises a NameError.
#
# Example of LEGB Rule

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # Local scope

    inner()
    print(x)  # Enclosing scope

outer()
print(x)  # Global scope
# Output:
#
#
# local
# enclosing
# global
#
# Python first looks for x in local scope, then enclosing, then global.


# ---------------------------Namespace and Scope-------------------------------------------------
# A namespace is like a dictionary where variable names are mapped to objects.
#
# Types of Namespaces:
# Local Namespace – Stores function variables.
# Global Namespace – Stores global variables.
# Built-in Namespace – Stores built-in functions.


# You can view the namespaces using:


print(globals())  # Shows global namespace
print(locals())  # Shows local namespace
# ---------------------------------------Nonlocal Keyword----------------------------------------------
# If you need to modify an enclosing variable (but not a global one), use nonlocal.
#
# Example:

def outer():
    x = "enclosing"

    def inner():
        nonlocal x  # Modifies the enclosing variable
        x = "modified"
        print(x)

    inner()
    print(x)  # Output: modified

outer()
# Without nonlocal, x = "modified" would create a new local variable instead of modifying the enclosing
# one.


# -------------------------------------------------Key Takeaways:
#
#
# Local variables exist only inside functions.
# Enclosing variables are accessible inside nested functions.
# Global variables can be accessed anywhere but need global to be modified inside functions.
# Built-in functions are always available.
# Python resolves variables using the LEGB Rule.
# Use nonlocal to modify variables in the enclosing scope.
#
# Would you like to see practical exercises on this topic?
