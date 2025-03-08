# Python Nested Loops
# In Python programming language there are two types of loops which are for loop and while loop.
# Using these loops we can create nested loops in Python. Nested loops mean loops inside a loop.
# For example, while loop inside the for loop, for loop inside the for loop, etc.


# Python Nested Loops Syntax:
# Outer_loop Expression:
#     Inner_loop Expression:
#         Statement inside inner_loop
#     Statement inside Outer_loop
x = [1, 2]
y = [4, 5]
i = 0
while i < len(x) :
  j = 0
  while j < len(y) :
    print(x[i] , y[j])
    j = j + 1
  i = i + 1