# --------------------------------The while Loop------------------------------------
# With the while loop we can execute a set of statements as long as a condition is true.
#
# Example
# Print i as long as i is less than 6:

i = 1
while i < 6:
  print(i)
  i += 1


# ----------------------The break Statement----------------------------------------
# With the break statement we can stop the loop even if the while condition is true:
#
# Example
# Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#------------------------------------------------------ The continue Statement------------------------------
# With the continue statement we can stop the current iteration, and continue with the next:
#
# Example
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


