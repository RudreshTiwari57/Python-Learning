
class Queue:

    def __init__(self):
        # items will store the item in queues
        self.__items : list = []


    # this method will add new item to the queue
    def enqueue(self,
               item):
        self.__items.append(item)

    # this method will remove the item from queue
    def dequeue(self):

        return self.__items.pop(0) if len(self.__items)>0 else None

    # this method will return true if the queue is empty
    def is_empty(self):

        return len(self.__items) == 0

    # this method will read first item of the top
    def peek(self):
        return self.__items[-1] if len(self.__items)>0 else None

    def return_queue(self):
        return self.__items


queue : Queue = Queue()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue(98)
queue.enqueue(68)
queue.enqueue(45)
print(queue.return_queue())
print(queue.dequeue())
print(queue.return_queue())



