"""
For this example, we'll create a binary search tree to store integers. 
We'll implement insertion, deletion, search, balancing, and finding the height 
of the tree.
"""
# Node class for representing each node in the binary search tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

##############################################  
# Section 1: Insertion in Binary Search Tree #
############################################## 
    """
    In this section, we define the `insert` method to insert a new key into 
    the binary search tree. The method calls the private `_insert_recursive` 
    function to perform the insertion operation recursively.

    The `_insert_recursive` function takes two parameters: `root` 
    (the current root node of the subtree) and `key` (the key value to be 
    inserted). The function returns the new root node of the tree (or subtree) 
    after the insertion.

    The `_insert_recursive` function starts by checking if the tree is empty 
    or if the current node is a leaf node (base case). If so, it creates a new 
    node with the given key and returns it.
    
    If the tree is not empty and the current node is not a leaf, the function 
    recursively finds the correct position to insert the new key. If the key 
    is less than the current node's key, it continues the insertion process 
    in the left subtree; otherwise, it continues in the right subtree.
    """
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        """
        Recursive helper function to insert a key into the binary search tree.

        Parameters:
            root (TreeNode): Current root node of the tree (subtree).
            key (int): Key value to be inserted.

        Returns:
            TreeNode: New root node of the tree (subtree) after insertion.
        """
        # If the tree is empty or we reached a leaf node, insert the new node here
        if root is None:
            return TreeNode(key)

        # Recursively find the correct position to insert the new node
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
            
        # Return the modified node
        return root

#############################################  
# Section 2: Deletion in Binary Search Tree #
############################################# 
    """
    This section contains the `delete` method and the private `_delete_recursive` 
    function for deleting a key from the binary search tree.

    The `delete` method is responsible for calling the `_delete_recursive` 
    function to delete a key from the binary search tree. It takes the `key` 
    as the parameter.

    The `_delete_recursive` function is a recursive helper function that takes 
    two parameters: `root` (the current root node of the subtree) and `key` 
    (the key value to be deleted). The function returns the new root node of 
    the tree (or subtree) after the deletion.

    The `_delete_recursive` function starts by checking if the tree is empty 
    or if the current node is a leaf node (base case). If so, it returns the 
    node itself (if found) or None.
    
    If the tree is not empty, and the current node is not a leaf, the function 
    recursively finds the node to delete. If the key is less than the current 
    node's key, it continues the search in the left subtree; otherwise, it 
    continues in the right subtree.

    Once the node to delete is found, the `_delete_recursive` function handles 
    three cases:
    If the node has no children or only one child, it returns the non-empty child (if any).
    If the node has two children, it finds the minimum node in the right subtree, copies its key to the current node, and 
    then recursively deletes the duplicate key from the right subtree.
    """
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        """
        Recursive helper function to delete a key from the binary search tree.

        Parameters:
            root (TreeNode): Current root node of the tree (subtree).
            key (int): Key value to be deleted.

        Returns:
            TreeNode: New root node of the tree (subtree) after deletion.
        """
        # Base case: If the tree is empty or we reached a leaf node, return the node (if found) or None
        if root is None:
            return root

        # Recursively find the node to delete
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # If the node has one child or no child, return the non-empty child (if any)
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # If the node has two children, find the minimum node in the right subtree
            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)

        # Return the modified node
        return root

    def _find_min(self, node):
        """
        Helper function to find the minimum node in a subtree.

        Parameters:
            node (TreeNode): Root node of the subtree.

        Returns:
            TreeNode: Node with the minimum key value in the subtree.
        """
        while node.left:
            node = node.left
        return node
    
###########################################  
# Section 3: Search in Binary Search Tree #
########################################### 
    """
    This section includes the `search` method and the private `_search_recursive` 
    function for searching a key in the binary search tree.

    The `search` method takes the `key` as the parameter and calls the 
    `_search_recursive` function to perform the search operation.

    The `_search_recursive` function is a recursive helper function that takes 
    two parameters: `root` (the current root node of the subtree) and `key` 
    (the key value to be searched). The function returns the node with the 
    matching key value or None if the key is not found.

    The `_search_recursive` function starts by checking if the tree is empty 
    or if the current node's key matches the search key (base case). 
    If so, it returns the node itself (if found). Otherwise, `None` is returned. The example usage also demonstrates how to handle the case when the key is not found in the tree.
    
    If the tree is not empty, and the current node's key does not match the 
    search key, the function recursively searches in the left subtree if the 
    key is less than the current node's key, or in the right subtree if the 
    key is greater than the current node's key.
    """
    def search(self, key):
        result = self._search_recursive(self.root, key)
        if result is None:
            print("Key {} not found in the binary search tree.".format(key))
        return result

    def _search_recursive(self, root, key):
        """
        Recursive helper function to search for a key in the binary search tree.

        Parameters:
            root (TreeNode): Current root node of the tree (subtree).
            key (int): Key value to be searched.

        Returns:
            TreeNode: Node with the matching key value, or None if not found.
        """
        # Base case: If the tree is empty or we found the node, return it
        if root is None or root.key == key:
            return root

        # Recursively search the left or right subtree based on the key
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

###############################################  
# Section 4: Height of the Binary Search Tree #
############################################### 
    """
    This section contains the `height` method and the private `_height_recursive` 
    function to calculate the height of the binary search tree.

    The `height` method simply calls the `_height_recursive` function with the 
    root of the tree as the parameter.

    The `_height_recursive` function is a recursive helper function that takes 
    `root` (the current root node of the tree) as the parameter. The function 
    calculates the height of the binary search tree using a recursive approach 
    and returns the height as an integer.

    The `_height_recursive` function starts with a base case: if the tree is 
    empty (root is None), it returns 0.
    
    If the tree is not empty, the function recursively calculates the height of 
    the left and right subtrees using `_height_recursive`. It then returns the
    maximum height of the left and right subtrees plus 1 
    (to account for the current node), which represents 
    the height of the current subtree.
    """
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, root):
        """
        Recursive helper function to calculate the height of the binary search tree.

        Parameters:
            root (TreeNode): Current root node of the tree (subtree).

        Returns:
            int: Height of the binary search tree.
        """
        # Base case: If the tree is empty, return 0
        if root is None:
            return 0

        # Recursively calculate the height of left and right subtrees
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)

        # Return the maximum height of left and right subtrees, plus 1 (for the current node)
        return max(left_height, right_height) + 1

############################  
# Section 5: Example usage #
############################ 
"""
In this section, an example usage of the binary search tree is provided. 
We create a `BinarySearchTree` object, insert some key values 
(50, 30, 70, 20, 40, 60, and 80), print the height of the tree using the 
`height` method, search for key 40 using the `search` method, delete 
several keys using the `delete` method, and then print the new height of the 
tree after deletion and try to search again for the deleted key (40).
"""
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print()
print("Binary Search Tree height:", bst.height()) 
# Output: Binary Search Tree height: 3
print()

print("Searching for key 40:", bst.search(40).key)
# Output: Searching for key 40: 40
print()

# Deleting values 20, 40, 60, and 80
bst.delete(20)
bst.delete(40)
bst.delete(60)
bst.delete(80)

print("After deleting 20, 40, 60, and 80, new height:", bst.height())
# Output: After deleting 20, 40, 60, and 80, new height: 2
print()

print("Search for key 40 after deletion:")
bst.search(40)
# Output: Key 40 not found in the binary search tree.

"""
This example demonstrates how to use the `BinarySearchTree` class and its 
methods to manage a binary search tree and perform various operations on it, 
including insertion, deletion, search, and finding the height of the tree.
"""