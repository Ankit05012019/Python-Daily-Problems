# create a linked list

class Node:

    def __init__(self,data):

        self.data=data
        self.next=None

class Linkedlist:

    def __init__(self):

        self.head=None

        # Function to insert a new node at the beginning
    def push(self, new_data):
        # allocate node and put the data
        new_node = Node(new_data)

        # Make next of new node as head
        new_node.next = self.head

        # move the head to point to the new Node
        self.head = new_node

    def print_llist(self):

        node = self.head
        while node is not None:
           print(node.data)
           #print(node.next)
           node=node.next

    def rotate_llist(self,k):

        if self.head == None:
            return "there is one or none elements"

        node=self.head
        count=1
        while count <= k and node is not None:

            node=node.next
            count += 1
        kthnode=node

        while node.next is not None:
            node=node.next
        node.next=self.head

        self.head=kthnode.next
        kthnode.next=None


llist = Linkedlist()
llist.push(2)
llist.push(3)
llist.push(4)

llist.print_llist()
llist.rotate_llist(2)
llist.print_llist()
