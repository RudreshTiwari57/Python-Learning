# Python Match Case Statement
# Introduced in Python 3.10, the match case statement offers a powerful mechanism for pattern matching
# in Python. It allows us to perform more expressive and readable conditional checks.
# Unlike traditional if-elif-else chains, which can become unwieldy with complex conditions,
# the match-case statement provides a more elegant and flexible solution.


# Python Match Case Statement Syntax

# match subject:
#     case pattern1:
#         # Code block if pattern1 matches
#     case pattern2:
#         # Code block if pattern2 matches
#     case _:
#         # Default case (wildcard) if no other pattern matches


x=10
match x:
    case 10:
        print("It's 10")
    case 20:
        print("It's 20")
    case _:
        print("It's neither 10 nor 20")
# Explanation:
    #
    # In this example, we use a match-case statement to compare the value of x to
    # the constants 10 and 20. If x equals 10, it prints “It’s 10”. If x equals 20, it prints “It’s 20”.
    # If neither condition is met, the wildcard _ matches any value, leading to the message “It’s neither 10
    # nor 20”.


