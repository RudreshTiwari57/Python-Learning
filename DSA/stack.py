# Stack is first in last out type of data structure. like a pile of plates. you add from top and remove from bottom.


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



stack : Stack = Stack()
stack.append(12)
stack.append([45,654,6,876,87,78,89])
stack.extend([546,47567,68,9,89,0,1,64])
print(stack.peek())
print(stack.items)
print(stack.size())
