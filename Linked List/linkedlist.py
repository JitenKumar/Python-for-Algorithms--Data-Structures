class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self,data):
        #allocate new node and add the data

        new_node = Node(data)
        # make the next of new node as head
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,data):
        # if the node not present then throw an error

        if prev_node is None:
            print("Previous Node must exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def appendAtLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.next = None

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.appendAtLast(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7);

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1);

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.appendAtLast(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print('List is')
    llist.printLinkedList()