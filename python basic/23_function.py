# In Python, functions can be classified based on their input (parameters) and
# output (return values). Here are the four main types based on these criteria:

# 1. -------------------------Takes Nothing, Returns Nothing-----------------------------------

    # Definition
        # These functions do not take any parameters and also do not return a value. They simply perform an operation.
        #
        # Example: A Function that Prints a Message
            # python
            # Copy
            # Edit

def say_hello():
    print("Hello, World!")  # Only prints, does not return anything

result = say_hello()  # Calls the function
print(result)  # Output: None


    # How it Works
        # The function say_hello() does not take any arguments.
        # It prints a message.
        # Since there is no return statement, calling the function will result in None.
    # Use Cases
        # Simple greeting messages
        # Running setup tasks at the start of a program
        # Clearing the screen or resetting configurations`

# 2. -----------------------------Takes Something, Returns Nothing-------------------------
    # Definition
        # These functions accept parameters (input values) but do not return a value.
        # Instead, they usually perform some operation like printing, modifying a global variable,
        # writing to a file, etc. If there is no explicit return statement, Python implicitly returns None.
    # Example: A Function that Prints a Greeting
        # python
        # Copy
        # Edit

def greet(name):
    print(f"Hello, {name}!")  # Performs an action but does not return anything

result = greet("Rudresh")  # Calls the function
print(result)  # Output: None (because nothing is returned)

    # How it Works
        # The function greet(name) takes a parameter name.
        # It prints a greeting message.
        # It does not return anything, so if you try to assign its result to a variable, it will store None.
    # Use Cases
        # Logging information
        # Printing messages to users
        # Writing data to files


# 3. -----------------------------------Takes Something, Returns Something---------------------------------
#     Definition
#     These functions accept parameters and also return a value using the return keyword. This makes them reusable and useful in calculations or data processing.
#
#     Example: A Function that Adds Two Numbers
#         python
#         Copy
#         Edit

def add(a, b):
    return a + b  # Returns the sum of a and b

result = add(5, 10)  # Calls the function and stores the return value
print(result)  # Output: 15

    # How it Works
        # The function add(a, b) takes two numbers.
        # It calculates their sum and returns the result.
        # The calling function receives the value and stores it in result.
    # Use Cases
        # Mathematical calculations (sum, product, etc.)
        # Processing and transforming data
        # Fetching values from databases or APIs

# 4. ----------------------------------Takes Nothing, Returns Something---------------------------------
#     Definition
#     These functions do not take parameters but still return a value. They are useful when you need to fetch or generate data but don’t need any input.
#
#     Example: A Function that Returns the Current Time
#         python
#         Copy
#         Edit

import time

def get_time():
    return time.ctime()  # Returns current system time

current_time = get_time()  # Calls the function and stores the return value
print(current_time)  # Output: (Current system time)


    # How it Works
    #     The function get_time() does not accept any input.
    #     It retrieves the current system time and returns it.
    #     The returned value is stored in current_time.
    # Use Cases
    #     Generating random numbers
    #     Fetching current system information (time, date, etc.)
    #     Creating default values

