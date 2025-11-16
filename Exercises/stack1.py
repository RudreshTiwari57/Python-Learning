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


def validate_input(string: str):
    stack : Stack = Stack()
    mapping = {'(': ')', '[': ']', '{': '}'}
    for s in string:
        if s in mapping.keys():
            print(stack.peek() ,mapping[s])
            if stack.peek() == mapping[s]:
                stack.pop(s)
            else:
                stack.append(s)
    return stack.is_empty()
print(validate_input("[({})]"))