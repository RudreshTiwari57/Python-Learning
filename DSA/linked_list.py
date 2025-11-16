

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None

    def append(self,data):
        new_node = Node(data)
        if not self._head:
            self._head = new_node
            return
        temp = self._head
        while temp.next:
            temp = temp.next

        temp.next = new_node
    def display(self):
        temp = self._head
        while temp:
            print(temp.data)
            temp = temp.next


    def delete(self,data):
        if self._head.data == data:
            self._head = self._head.next
            return
        temp = self._head
        prev = None
        while temp:
            if temp.data == data:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next




ll = LinkedList()
ll.append(3)
ll.append(34)
ll.append(54)
ll.append(67)
ll.append(12)
ll.append(76)
ll.append(89)
ll.append(58)
ll.display()
print("-----------------------")
ll.delete(90)
ll.display()
