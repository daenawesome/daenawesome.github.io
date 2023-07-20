"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        def __init__(self, value, priority):
            self.value = value
            self.priority = priority

        def __str__(self):
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        self.queue = []

    def enqueue(self, value, priority):
        new_node = Priority_Queue.Node(value, priority) # Corrected parameter order
        self.queue.append(new_node)

    def dequeue(self):
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority: # Corrected comparison operator
                high_pri_index = index
            elif self.queue[index].priority == self.queue[high_pri_index].priority:
                if index < high_pri_index: # Corrected FIFO strategy
                    high_pri_index = index
        # Remove and return the item with the highest priority
        node = self.queue.pop(high_pri_index) # Return the node object instead of only the value
        return node.value

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: Add multiple nodes with different priorities to the queue and dequeue them.
# Expected Result: The nodes should be dequeued in the order of their priorities.
print("Test 1")
pq = Priority_Queue()
pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 2)
assert pq.dequeue() == "B"
assert pq.dequeue() == "C"
assert pq.dequeue() == "A"
# Defect(s) Found: The values and priorities are swapped in the Node constructor. 
# The correct order is Node(value, priority) instead of Node(priority, value). 
# This results in the priorities being stored as values and vice versa. 
# Also, the comparison operator in the dequeue method is incorrect, it should be '>' instead of '>='. 
# These issues cause the incorrect order of dequeuing in the test case.
print("=================")


# Test 2
# Scenario: Add multiple nodes with the same priority and dequeue them
# Expected Result: The nodes should be dequeued in the order they were enqueued (FIFO)
print("Test 2")
queue = Priority_Queue()
queue.enqueue("Task 1", 2)
queue.enqueue("Task 2", 1)
queue.enqueue("Task 3", 3)
queue.enqueue("Task 4", 2)
dequeued = []
while len(queue) > 0:
    dequeued.append(queue.dequeue())
assert dequeued == ["Task 3", "Task 1", "Task 4", "Task 2"]
# Defect(s) Found: The priority and value parameters are reversed when creating a new node in the enqueue method. 
# This causes the node to be created with the wrong values and the priorities to be reversed. 
print("=================")


# Test 3
# Scenario: Test adding and removing multiple items with different priorities.
# Expected Result: The dequeue function should return the items in the correct priority order, and the length should be zero.
print("Test 3")
q = Priority_Queue()
q.enqueue("A", 1)
q.enqueue("B", 3)
q.enqueue("C", 2)
assert len(q) == 3
assert q.dequeue() == "B"
assert q.dequeue() == "C"
assert q.dequeue() == "A"
assert len(q) == 0
# Defect(s) Found: The Node constructor arguments are swapped when creating a new node in the enqueue function. 
print("=================")


# Test 4
# Scenario: Add a single node to the queue and dequeue it.
# Expected Result: The node's value should be returned by the dequeue function.
print("Test 4")
pq = Priority_Queue()
pq.enqueue("A", 1)
assert pq.dequeue() == "A"
print("=================")


# Test 5
# Scenario: Dequeue from an empty queue.
# Expected Result: An error message should be displayed.
print("Test 5")
pq = Priority_Queue()
assert pq.dequeue() == None
# Defect(s) Found: The test case is working as expected because the queue is empty and the dequeue function displays an error message.
print("=================")


# Test 6
# Scenario: Test trying to remove an item from an empty queue.
# Expected Result: The dequeue function should return None and display an error message.
print("Test 6")
q = Priority_Queue()
assert len(q) == 0
assert q.dequeue() is None
print("=================")