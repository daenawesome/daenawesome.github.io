"""
CSE212 
(c) BYU-Idaho
07-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """
        
        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value) # create a new Node 
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    ###################
    # Start Problem 1 #
    ###################
    
    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        new_node = LinkedList.Node(value)  # Create the new node

        if self.tail is None:           # Check is head is None 
            self.head = new_node        # Assign new_node to head
            self.tail = new_node        # Assign new_node to tail
        else:                           
            new_node.prev = self.tail   # Connect new node to the current tail
            self.tail.next = new_node   # Connect the current tail to the new node
            self.tail = new_node        # Update the tail to point to the new node

    #################
    # End Problem 1 #
    #################

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    ###################
    # Start Problem 2 #
    ###################
    
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            prev_node = self.tail.prev  # Get the previous node
            prev_node.next = None       # Disconnect the current tail
            self.tail = prev_node       # Update the tail to point to the previous node

    #################
    # End Problem 2 #
    #################

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    ###################
    # Start Problem 3 #
    ###################
    
    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # If the list is empty, there's nothing to remove
        if self.head is None:
            return

        # If the head node contains the value, remove it using remove_head function
        if self.head.data == value:
            self.remove_head()
            return

        # Start searching for the value from the second node
        curr = self.head.next

        # Traverse the list until the end or until a match is found
        while curr is not None:
            if curr.data == value:
                # If the node to remove is the tail, remove it using remove_tail function
                if curr == self.tail:
                    self.remove_tail()
                else:
                    curr.prev.next = curr.next  # Connect the previous node to the next node
                    curr.next.prev = curr.prev  # Connect the next node to the previous node
                return
            curr = curr.next

    #################
    # End Problem 3 #
    #################

    ###################
    # Start Problem 4 #
    ###################
    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        # If the list is empty, there's nothing to replace
        if self.head is None:
            return

        # Start from the head node
        curr = self.head

        # Traverse the list and replace values
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value  # Replace the value with new_value
            curr = curr.next

    #################
    # End Problem 4 #
    #################

    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        curr = self.head  # Start at the beginning since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    ###################
    # Start Problem 5 #
    ###################
    
    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        curr = self.tail  # Start at the end since this is a backward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.prev  # Go backward in the linked list

    #################
    # End Problem 5 #
    #################

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    
# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0, -1]

print("\n=========== PROBLEM 2 TESTS ===========")
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0]
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]

print("\n=========== PROBLEM 3 TESTS ===========")
ll.insert_after(3, 3.5)
ll.insert_after(5, 6)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(-1)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(3)
print(ll) # linkedlist[5, 6, 4, 3.5, 2, 2, 2, 1]
ll.remove(6)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2, 1]
ll.remove(1)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(7)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(5)
print(ll) # linkedlist[4, 3.5, 2, 2, 2]
ll.remove(2)
print(ll) # linkedlist[4, 3.5, 2, 2]

print("\n=========== PROBLEM 4 TESTS ===========")
ll.replace(2, 10)
print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(7, 5)
print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(4, 100)
print(ll) # linkedlist[100, 3.5, 10, 10]


print("\n=========== PROBLEM 5 TESTS ===========")
print(list(reversed(ll)))  # [10, 10, 3.5, 100]
