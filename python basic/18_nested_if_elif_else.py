#--------------------------------------------------- Nested If------------------------------------------
# You can have if statements inside if statements, this is called nested if statements.
#
# Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#--------------------------------------------------- Nested elif------------------------------------------
# You can have if statements inside elif statements, this is called nested  statements.
#
# Example
x = 41

if x <30:
  print("below 30,")

elif x > 30:
  print("Above ten,")
  if x > 40:
    print("and also above 40!")
  else:
    print("but not above 40.")

#--------------------------------------------------- Nested elif------------------------------------------
# You can have if statements inside elif statements, this is called nested  statements.
#
# Example
x = 41

if x <30:
  print("below 30,")

elif x == 40:
  print("is 40,")

else:
    if x > 40:
        print("and also above 40!")
    else:
        print("but not above 40.")