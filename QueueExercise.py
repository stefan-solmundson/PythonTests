"""
Create a class called Queue.
Declare the maxSize (int), array of integer type, front (int), rear (int) and total items (int nItems).
Use the following signature for the constructor.

public Queue(int s) //size of the queue you want to create

In constructor instantiate the maxSize, array, front, rear and nItems.
Define insert (), remove(), peekFront(), isEmpty(), isFull(), size() methods in the class.

Create an object of Queue class by passing the size of the queue you want to create.
Insert 4 integers in the queue using the insert() method.
Remove 3 items from the queue.
Insert another 4 items in the queue.
Remove an display all items in the queue (while loop).
Submit your exercise on the Black Board.
"""

# https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues
# from collections import deque  # NOPE, deque isn't really necessary


class Queue:

    def __init__(self, queue_size=10, input_list=[]):
        self.queue_size = queue_size
        self.list = input_list[0:9]

    def front(self):
        return self.list[0]

    def peek_front(self):
        self.front(self)

    def rear(self):
        return self.list[len(self.list)]

    def total_items(self):
        return len(self.list)

    def items(self):
        self.total_items(self)

    def length(self):
        self.total_items(self)

    def insert(self, x):
        if len(self.list) == self.queue_size:
            print("This list is full.")
            return False
        else:
            self.list.append(x)
            return True

    def remove(self, start=0, end=None):
        if len(self.list) == 0:
            return False
        else:
            if end is None:
                temp = self.list[start]
                del self.list[start]
                return temp
            else:
                temp = self.list[start:end]
                del self.list[start:end]
                return temp

    def is_empty(self):
        return len(self.list) == 0

    def is_full(self):
        return len(self.list) == self.queue_size

    def size(self):
        return self.queue_size


testQueue = Queue(5)

testQueue.insert(2)
testQueue.insert(5)
testQueue.insert(3)
testQueue.insert(1)
print(testQueue.list)

testQueue.remove()
testQueue.remove()
testQueue.remove()
print(testQueue.list)

testQueue.insert(4)
testQueue.insert(4)
testQueue.insert(4)
testQueue.insert(4)
print(testQueue.list)

print("Queue size: " + str(len(testQueue.list)))
print("Queue max size: " + str(testQueue.queue_size))
testQueue.insert(7)

# Do-While Loop
while True:
    a = testQueue.remove()
    if a != False:
        print(a)
    else:
        break

# For Loop
for i in range(testQueue.total_items()):
    print(testQueue.remove())
