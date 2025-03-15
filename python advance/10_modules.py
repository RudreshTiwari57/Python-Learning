# Python modules are files containing Python code (functions, classes, or variables) that can be reused in different programs.
# They help organize code and promote reusability.
#
# --------------------------------------------------Types of Python Modules:--------------------------------------------------
            # Built-in Modules – Pre-installed in Python (e.g., os, sys, math, datetime).
            # User-defined Modules – Created by users as .py files.
            # Third-party Modules – External libraries installed via pip (e.g., requests, numpy, pandas).


#----------------------------------------- 1. Creating a Module-----------------------------------------------------------
# A module is simply a Python file with functions, classes, or variables.
#
# Example (my_module.py):
# my_module.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.1416

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age



# ------------------------------------------------2. Importing a Module------------------------------------------------
# ------------------------------------a) Import the Entire Module

# import my_module
#
# print(my_module.greet("Rudresh"))  # Output: Hello, Rudresh!
# print(my_module.PI)  # Output: 3.1416


# --------------------------------------b) Import Specific Items

# from my_module import greet, PI
#
# print(greet("Rudresh"))
# print(PI)


# ---------------------------------------c) Import with an Alias

# import my_module as mm
#
# print(mm.greet("Rudresh"))



#--------------------------------------d) Import Everything (Not Recommended)

# from my_module import *


# -----------------------------------------------3. Module Search Path (sys.path)--------------------------------------------------------------------
# Python searches for modules in:
#
# The current directory.
# The directories in the PYTHONPATH environment variable.
# The standard library directories.
# You can check the module search path:

import sys
print(sys.path)

# If you want to add a custom path:
sys.path.append("/path/to/your/module")

# -------------------------------------------------Finding Module Location-------------------------------------
# import my_module
# print(my_module.__file__)  # Shows the file path of the module



# --------------------------------------------4. Standard Built-in Modules----------------------------------------------------------------

import os
import sys
import math
import datetime
import random
import json
import re



# Example:

import math
print(math.sqrt(16))  # 4.0


import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# ---------------------------------------------------5. Installing and Using Third-Party Modules------------------------------------------------

# command:

# pip install requests

# then
import requests
response = requests.get("https://api.github.com")
print(response.status_code)


#--------------------------------------------------------- 6. Custom Module in a Package---------------------------------------------------

# A package is a folder with a __init__.py file that groups multiple modules.
#
# Example Directory Structure:

# my_package/
#     |- __init__.py
#     |
#     |- module1.py
#     |
#     |- module2.py

# Content of module1.py:
def add(a, b):
    return a + b




# ------------------------------------------- 7. Compiled Python Modules (.pyc and .pyo)----------------------------------------------------
# When a module is imported, Python compiles it to a .pyc file (bytecode) for faster execution.

# To manually compile:
# command:

# python -m compileall my_module.py


# This creates a __pycache__/ directory with a .pyc file.



# --------------------------------------------------- 8. Dynamically Importing Modules-------------------------------------------------------
# You can import modules dynamically using importlib:

import importlib

module_name = "math"
math_module = importlib.import_module(module_name)

print(math_module.sqrt(16))  # Output: 4.0


# ------------------------------------------------------------ 9. Reloading a Module---------------------------------------------------------
#
#
# If you modify a module after importing it, Python won't reload it unless explicitly instructed.

# import importlib
# import my_module
#
# importlib.reload(my_module)


# ------------------------------------------------------ 10. Writing and Using __main__ in Modules------------------------------------------
#
# If a module is executed directly, __name__ == "__main__".
#
# Example: my_module.py

def main():
    print("This script is running as the main program.")

if __name__ == "__main__":
    main()

# When run directly:
# command:
# python my_module.py

# Output: This script is running as the main program.
#
# If imported, it won't execute main().


# ---------------------------------------------- 11. Differences Between import and from ... import --------------------------------------------
#
# Method	Usage	Example

            # -------------------------------------------------------------------------------------------------------------
            # |   import module_name	         |         Imports the entire module	        |     import math         |
            # -------------------------------------------------------------------------------------------------------------
            # |  from module_name import func	 |     Imports specific functions/classes	    |  from math import sqrt  |
            # |  import module_name as alias	 |         Imports with an alias	            |   import numpy as np    |
            # |  from module_name import *	     |   Imports everything (not recommended)	    |from math import *       |
            # -------------------------------------------------------------------------------------------------------------




