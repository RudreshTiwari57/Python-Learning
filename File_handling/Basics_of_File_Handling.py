# File handling is a core concept in Python that allows you to read, write, and manipulate files on your system.
# Let's explore it in depth with advanced topics.


#------------------------------------------------------------- 1. Basics of File Handling-----------------------------------------------------

# Python provides built-in functions to work with files. The most commonly used function is open(), which is used to open files in
# different modes.
#
# ------------------------------------- File Opening Modes
#
#                         -------------------------------------------------------------------------------------------------------
#                         | Mode    |   Description                                                                             |
#                         -------------------------------------------------------------------------------------------------------
#                         | "r"	    |   Read mode (default) - Opens file for reading, raises an error if file does not exist.   |
#                         | "w"	    |   Write mode - Creates a new file or overwrites an existing file.                         |
#                         | "a"	    |   Append mode - Adds content at the end of the file.                                      |
#                         | "x"	    |   Exclusive mode - Creates a new file but raises an error if the file already exists.     |
#                         | "b"	    |   Binary mode - Opens file in binary format (e.g., images, PDFs).                         |
#                         | "t"	    |   Text mode (default) - Opens file as a text file.                                        |
#                         -------------------------------------------------------------------------------------------------------


# ----------------------------------- Example: Opening & Reading a File


# Open a file in read mode
file = open("example.txt", "r")

# Read the content of the file
content = file.read()
print(content)

# Close the file
file.close()


# Best Practice: Always close the file after reading or writing to free system resources.


# -------------------------------------------2. Using with Statement (Best Practice)------------------------------------------------------
# Instead of manually closing a file, use the with statement to automatically close it after execution.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block


# ------------------------------------Why use with?
#
            # a. No need to manually call close().
            # b. Prevents memory leaks.
            # c. Safer in case of exceptions.

#---------------------------------------------- Writing to Files (w, a, x Modes)
#-------------------------------------------- a. Write Mode (w) - Overwrites the File

with open("example.txt", "w") as file:
    file.write("Hello, World!")  # Overwrites the file content


# ---------------------------------------------- b. Append Mode (a) - Adds Content to the File

with open("example.txt", "a") as file:
    file.write("\nAppending a new line.")  # Adds new content without deleting previous data


#----------------------------------------------- c. Exclusive Mode (x) - Creates a File, Fails if Exists

with open("newfile.txt", "x") as file:
    file.write("This file is created using 'x' mode.")


# Error Handling: If "newfile.txt" already exists, Python will raise a FileExistsError.


# -------------------------------------------------3. Reading Large Files Efficiently--------------------------------------------------------------
# Instead of loading the entire file into memory, use line-by-line reading for better performance.
#
#-----------------------------------------a. Reading a File Line by Line

with open("largefile.txt", "r") as file:
    for line in file:
        print(line.strip())  # `.strip()` removes newline characters


 # -----------------------------------------b. Reading Specific Number of Bytes

with open("example.txt", "r") as file:
    chunk = file.read(10)  # Reads first 10 characters
    print(chunk)

# --------------------------------------------4. File Handling with Exception Handling------------------------------------------------------
# Always handle file-related exceptions to avoid crashes.


try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except IOError:
    print("Error: An I/O error occurred.")

# --------------------------------Why?

            # a. Prevents program crashes.
            # b. Provides user-friendly error messages.

# --------------------------------------------------3. File Pointers & Seeking--------------------------------------------------------------
# When working with files, you can move the file pointer to a specific position.
#
# ----------------------------a. Checking the Current File Pointer Position

with open("example.txt", "r") as file:
    print(file.tell())  # Shows the current position (in bytes)

# -----------------------------b. Moving the File Pointer (seek())

with open("example.txt", "r") as file:
    file.seek(5)  # Move pointer to the 5th byte
    print(file.read())  # Read from new position


# -------------------------------c. Deleting a File
# To delete a file, use the os module.

import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")
