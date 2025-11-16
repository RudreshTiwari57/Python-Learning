
# Given a string containing only '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# # Example
#     Input: "(()"
#     Output: 2  # "()"
#
#     Input: ")()())"
#     Output: 4  # "()()"

#declare a class called Stack
class Stack:
    # define a constructor to automatically create an empty list object to store data
    def __init__(self):
        self.items : list = []              # list to store all the values

    # this method will add value to our stack
    def append(self,
               value
               ):
        self.items.append(value)


    # the method will remove item from our stack
    def pop(self,
            *value):
        if len(self.items)>0:
            return self.items.pop(0)
        else:
            print("the stack is removed")

    # this method will extend the stack
    def extend(self,
               value):
        self.items.extend(value)

    # this method will read first item of the top
    def peek(self):
        return self.items[-1] if len(self.items)>0 else None

#     this method will check if the stack is empty or not
    def is_empty(self):
        return len(self.items)==0

    # this method will retrun the size of stack
    def size(self):
        return len(self.items)

def longest_valid_parentheses(s: str) -> int:
    stack = [-1]  # base index to calculate length
    max_len = 0

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # update base for future valid substring
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

print(longest_valid_parentheses(")()()(())"))