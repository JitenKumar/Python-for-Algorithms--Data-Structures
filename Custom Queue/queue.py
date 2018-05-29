class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items ==[]


Q = Queue()

Q.enqueue(1333)
Q.enqueue(23)
Q.enqueue(53)
Q.enqueue(13)
Q.enqueue(33)
Q.enqueue(194)
Q.enqueue(1823)
print(Q.items)
# Printing the size of the Queue
print(Q.size())
# printing the or deque the element
print(Q.deque())
# Printing is Empty
print(Q.isEmpty())


# Deque Implementation

class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

# making a deque

DQ = Deque()

DQ.addFront('First')
DQ.addFront('First2')
DQ.addRear('Rear')
print(DQ.items)

DQ.removeFront()
print(DQ.items)
DQ.removeRear()
print(DQ.items)
print(DQ.size())
print(DQ.isEmpty())