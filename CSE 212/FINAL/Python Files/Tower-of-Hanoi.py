# In this example, the `Stack` class represents the stack data structure, 
# and it provides the basic operations of `push`, `pop`, `peek`, and `is_empty`.

# The `tower_of_hanoi` function takes as input the number of disks, the source stack, 
# the destination stack, and the auxiliary stack. It uses a recursive approach to solve 
# the puzzle, moving disks between the stacks according to the rules of the Tower of Hanoi. 
# Each move is printed out for visualization.

# Define the Stack class
class Stack:
    def __init__(self, label):
        self.items = []  # Initialize an empty list to store the stack items
        self.label = label  # Set the label for the stack

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty

    def push(self, item):
        self.items.append(item)  # Push/Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Pop/Remove and return the top item from the stack

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the top item from the stack without removing it


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        disk = source.pop()  # Remove the top disk from the source stack
        destination.push(disk)  # Place the disk onto the destination stack
        print(f"Move disk {disk} from {source.label} to {destination.label}")
    else:
        tower_of_hanoi(n-1, source, auxiliary, destination)  # Move n-1 disks from source to auxiliary
        disk = source.pop()  # Remove the top disk from the source stack
        destination.push(disk)  # Place the disk onto the destination stack
        print(f"Move disk {disk} from {source.label} to {destination.label}")
        tower_of_hanoi(n-1, auxiliary, destination, source)  # Move n-1 disks from auxiliary to destination


# Creating three stacks representing the rods
source = Stack("Source")
auxiliary = Stack("Auxiliary")
destination = Stack("Destination")

# Example usage
# n = 3

# Get the number of disks from the user
n = int(input("Enter the number of disks: "))

# Pushing the disks onto the source stack
for disk in range(n, 0, -1):
    source.push(disk) # Push disks onto the source stack

# Solving the Tower of Hanoi puzzle
tower_of_hanoi(n, source, destination, auxiliary)

# You can customize the `n` variable to change the number of disks in the puzzle. 