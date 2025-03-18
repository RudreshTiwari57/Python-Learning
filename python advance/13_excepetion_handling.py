# try-except in Python is a way to handle runtime errors so that your program doesn’t crash.

# Real-Life Example:
#         Imagine you are using an ATM to withdraw cash. Several things can go wrong, and the system must handle these errors properly:
#
#             a. Insufficient Funds > You try to withdraw more money than your balance.
#             b. Invalid PIN > You enter the wrong PIN multiple times.
#             c. Machine Out of Cash > The ATM doesn’t have enough cash to dispense.
#             d. Network Issues > The bank server is down, and the transaction cannot be processed.
#
#
#        How try-except Helps
#             a. The ATM tries to process the withdrawal.
#             b. If any issue occurs, it catches the specific error.
#             c. The system shows a proper message instead of crashing.
#             d. If everything is fine, it dispenses the cash and updates your balance.
#

# Let's explore it in-depth, covering advanced concepts like:
#
        # 1. Basic Try-Except
        # 2. Catching Multiple Exceptions
        # 3. Using else and finally
        # 4. Handling Nested Exceptions
        # 5. Logging Exceptions Properly
        # 6. Raising Exceptions Manually (raise)
        # 7. Custom Exceptions


# -----------------------------1️. Basic Try-Except (Error Handling)-----------------------------------------------------
# Whenever Python encounters an error, it throws an exception. We can catch those exceptions using try-except.


try:
    result = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Handling the error


# Output:
    # Cannot divide by zero!



# -----------------------------------------------2. Catching Multiple Exceptions-----------------------------------------------------------
# You can handle multiple types of errors separately:

try:
    num = int("hello")  # Trying to convert a string to an integer
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Output:
#         Invalid input! Please enter a number.


#---------------------------------- Why not use a single except block?
    #
    # If we only used except Exception, we wouldn’t know what type of error occurred.
    # Using multiple specific except blocks makes debugging easier.


# ------------------------------------------------------------------3. Using else and finally----------------------------------------------------------------
        # else: Executes only if no exception occurs.
        # finally: Executes no matter what (even if there is an error).

try:
    num = int("42")  # No error here
except ValueError:
    print("Invalid input!")
else:
    print("Conversion successful:", num)
finally:
    print("Execution completed.")


# OUTPUT:
    # Conversion successful: 42
    # Execution completed.


# ----------------------------------------------Use cases of finally:
#
#                         a. Closing a database connection
#                         b. Releasing a file lock
#                         c. Cleaning up resources



# -------------------------------------------------------4. Handling Nested Exceptions----------------------------------------------
# When working with nested operations, you might need to use multiple try-except blocks.
#
#  Bad Practice (Deep Nesting):

try:
    with open("data.txt", "r") as file:
        try:
            content = file.read()
            try:
                number = int(content)  # Convert file content to integer
            except ValueError:
                print("Content is not a number!")
        except IOError:
            print("File could not be read!")
except FileNotFoundError:
    print("File not found!")


#  Problem: Too many nested try-except blocks make it difficult to read.
#
# Better Approach: Using Functions

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found!")
        return None
    except IOError:
        print("File could not be read!")
        return None

def convert_to_int(data):
    try:
        return int(data)
    except ValueError:
        print("Content is not a number!")
        return None

content = read_file("data.txt")
if content:
    number = convert_to_int(content)


# ----------------------------------------------------Why is this better?
#
                    # a. The logic is separated into functions.
                    # b. The code is more readable and reusable.


#---------------------------------------------- 5. Logging Exceptions Properly-----------------------------------------------------------
# Instead of just printing errors, log them for better debugging.


import logging

logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Error: {e}")  # Logs the error into a file


# This will log errors into errors.log instead of just printing them.
#
# -------------------------------Why use logging
#
                        # a. Helps in debugging production issues.
                        # b. Stores detailed logs for later analysis.
                        # c. Avoids missing important errors.



#----------------------------------------------6. Raising Exceptions Manually (raise)----------------------------------------------------
# You can forcefully raise an exception using raise.



def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero!")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")


# Output:
        # Caught an error: You cannot divide by zero!



#------------------------------------------------------- Why use raise?
#
                            # a. To enforce certain conditions in your code.
                            # b. To signal an error before it happens naturally.



# ------------------------------------------------------------7. Creating Custom Exceptions---------------------------------------------
#
# You can define your own custom exceptions for more specific error handling.

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Number cannot be negative!")
    return num

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Error: {e}")


# OUTPUT:
#                 Error: Number cannot be negative!
# ------------------------------------------------------Why use custom exceptions?
#
                    # a. Makes errors more meaningful.
                    # b.  Helps differentiate between different types of errors.