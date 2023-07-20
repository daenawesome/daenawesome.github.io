"""
For the purpose of demonstration I have made the following code that provides functions to 
perform various operations on the BST, including insertion, search, deletion, and finding 
the minimum and maximum values. Additionally, it calculates the height of the BST, 
which is the maximum depth of the tree.

To highlight the efficiency of binary search over linear search, the code also performs 
linear search on a sorted array and binary search on the BST to find a specific target value. 

But note that in some cases, linear search may perform better than binary search. 
These cases typically occur when the dataset is small or not sorted, as linear search can 
have a constant time complexity of O(1) for finding the target value in such scenarios. 
On the other hand, binary search relies on the dataset being sorted, and its time complexity 
is logarithmic (O(log n)), making it more efficient for large sorted datasets.
"""
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def linear_search_steps(arr, target):
    # Function to perform linear search in a sorted array and count the steps
    steps = 0
    for i in range(1, len(arr)):  # Start from the second element (index 1)
        steps += 1
        if arr[i] == target:  # If the target is found, return the number of steps taken
            return steps
    return steps  # If target is not found, return the total number of steps taken

def insert_into_bst(root, key):
    # Function to insert a new node with the given key into the binary search tree
    if root is None:  # If the tree is empty or the position is found for insertion
        return TreeNode(key)

    if key < root.key:  # If the key is less than the current node's key, traverse to the left subtree
        root.left = insert_into_bst(root.left, key)
    elif key > root.key:  # If the key is greater than the current node's key, traverse to the right subtree
        root.right = insert_into_bst(root.right, key)

    return root  # Return the modified root of the tree

def search_in_bst(root, key, steps=0):
    # Function to search for a key in the binary search tree and count the steps
    if root is None or root.key == key:  # If the root is None or the key is found in the current node
        return steps

    if key < root.key:  # If the key is less than the current node's key, traverse to the left subtree
        return search_in_bst(root.left, key, steps + 1)
    else:  # If the key is greater than the current node's key, traverse to the right subtree
        return search_in_bst(root.right, key, steps + 1)

def find_min_value_bst(root):
    # Function to find the minimum value in a binary search tree
    if root is None:
        return None

    current = root
    while current.left is not None:  # Keep traversing left until reaching the leftmost node
        current = current.left

    return current.key  # Return the key of the leftmost node (minimum value)

def find_max_value_bst(root):
    # Function to find the maximum value in a binary search tree
    if root is None:
        return None

    current = root
    while current.right is not None:  # Keep traversing right until reaching the rightmost node
        current = current.right

    return current.key  # Return the key of the rightmost node (maximum value)

def delete_from_bst(root, key):
    # Function to delete a node with the given key from the binary search tree
    if root is None:
        return root

    if key < root.key:  # If the key is less than the current node's key, traverse to the left subtree
        root.left = delete_from_bst(root.left, key)
    elif key > root.key:  # If the key is greater than the current node's key, traverse to the right subtree
        root.right = delete_from_bst(root.right, key)
    else:
        if root.left is None:  # If the node has no left child, replace it with the right child (if any)
            return root.right
        elif root.right is None:  # If the node has no right child, replace it with the left child
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        root.key = find_min_value_bst(root.right)

        # Delete the inorder successor from the right subtree
        root.right = delete_from_bst(root.right, root.key)

    return root  # Return the modified root of the tree

def calculate_height_bst(root):
    # Function to calculate the height of a binary search tree
    if root is None:
        return -1  # Height of an empty tree is -1

    left_height = calculate_height_bst(root.left)  # Calculate the height of the left subtree
    right_height = calculate_height_bst(root.right)  # Calculate the height of the right subtree

    return max(left_height, right_height) + 1  # Return the maximum height among the subtrees + 1 (for the root)

def inorder_traversal(root):
    # Function to perform inorder traversal of the binary search tree
    if root:
        inorder_traversal(root.left)  # Traverse the left subtree
        print(root.key, end=" ")  # Visit the current node (print its key)
        inorder_traversal(root.right)  # Traverse the right subtree

# Creating BST with 21 as the root
sorted_array = [5, 11, 12, 14, 15, 18, 19, 21, 23, 25, 27, 28, 30, 32, 37]
root = TreeNode(21)

# Insert elements into the BST
for num in sorted_array:
    if num != 21:  # Skip the root value, as it's already the root of the BST
        insert_into_bst(root, num)

# Searching for 27 in the sorted array using linear search
target_value = 27
steps_linear_search = linear_search_steps(sorted_array, target_value)
print(f"Number of steps taken to find {target_value} using linear search: {steps_linear_search}")

# Searching for 27 in the BST
steps_bst = search_in_bst(root, target_value)
print(f"Number of steps taken to find {target_value} in the BST: {steps_bst}")
print()
# Find minimum and maximum values in the BST
min_value = find_min_value_bst(root)
max_value = find_max_value_bst(root)
print(f"Minimum value in the BST: {min_value}")
print(f"Maximum value in the BST: {max_value}")
print()
# Calculate height of the BST
height_before_delete = calculate_height_bst(root)
print(f"Height of the BST before deleting: {height_before_delete}")

# Deleting values from the BST
values_to_delete = [11, 27, 32]
for value in values_to_delete:
    root = delete_from_bst(root, value)

# Calculate height of the BST after deleting
height_after_delete = calculate_height_bst(root)
print(f"Height of the BST after deleting values 11, 27 and 32: {height_after_delete}")
print()
# Insert other values into the BST
values_to_insert = [13, 16, 17]
for value in values_to_insert:
    insert_into_bst(root, value)

# Print the elements of the BST in inorder traversal
print("Elements of the BST in inorder traversal after inserting values 13, 16 and 17:")
inorder_traversal(root)
