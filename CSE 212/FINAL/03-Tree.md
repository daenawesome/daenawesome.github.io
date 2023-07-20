# Tree Tutorial

<font size="1.5"> 

**:back: [Return to the Welcome Page](00-Welcome.md)**
**:arrow_left: [Back to Set Tutorial](02-Set.md)** 
</font>

---

<div style="display: flex;">
  <div style="width: 70%;">
    <h2>Table of Contents</h2>
    <ul>
      <li><a href="#introduction">Introduction</a></li>
      <li><a href="#purpose-and-characteristics-of-a-tree-data-structure">Purpose and Characteristics of a Tree Data Structure</a></li>
      <li><a href="#types-of-trees">Types of Trees</a></li>
      <li><a href="#basic-operations-and-performance">Basic Operations and Performance</a></li>
      <li><a href="#implementation-in-python">Implementation in Python</a></li>
      <li><a href="#binary-search-tree-bst">Binary Search Tree (BST)</a></li>
      <li><a href="#applications-of-tree">Applications of Tree</a></li>
      <li><a href="#example-problems">Example Problems</a></li>
      <li><a href="#common-errors">Common Errors</a></li>
      <li><a href="#independent-problem">Independent Problem</a></li>
      <li><a href="#conclusion-and-next-steps">Conclusion and Next Steps</a></li>
    </ul>
  </div>
  <div style="width: 30%; padding-left: 20px;">
    <div style="text-align: center;">
      <img src="/FINAL/Picture%20Files/AnimatedTreeDancing.gif" alt="Drawing Keys Animation" width="200" height="370" />
    </div>
  </div>
</div>

## Introduction

Welcome to the exhilarating Tree data structure tutorial! There is a lot to discuss about this Data structure so I will be keeping this introduction short. 

Throughout this module, we will explore the purpose, implementation, applications, and other important concepts of trees. Get ready for a captivating journey into this fascinating world, where we'll unravel the mysteries surrounding trees and ignite your passion for this incredible subject. So, fasten your seatbelts, because this adventure is bound to leave you spellbound by the boundless possibilities of trees! Let's dive in together!

## Purpose and Characteristics of a Tree Data Structure

A tree is a non-linear data structure composed of nodes connected by edges, forming a hierarchical structure that provides an efficient way to store and retrieve data and they find applications in various domains, including computer science, data organization, and problem-solving algorithms. 

It consists of nodes connected by edges, forming a structure resembling a real-world tree and each node in a tree can have zero or more child nodes, except for the root node, which has no parent. Trees are widely used to represent hierarchical relationships between objects and solve problems efficiently.

**Overall Structure**

Imagine you have a beautiful tree in your backyard, with its main trunk representing the "Overall Structure" of the tree data structure. Let's explore the tree terminology through this analogy:

<div style="text-align: center;">
        <img src="/FINAL/Picture%20Files/treeOverallStrcucture.png" alt="Tree Structure Image" width="650" height="300" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);" />
</div>

1. **Node**: Picture each branch or twig of the tree as a "Node." Each node contains a value, just like a fruit or ornament that you might hang on a branch.

2. **Child**: Think of a "Child" as a smaller branch connected to a bigger branch. In our tree analogy, a child node is connected to its parent node, just like a smaller branch extends from a larger one.

3. **Parent**: A "Parent" node is like the main branch from which the child branches (nodes) originate. It oversees and connects to its children.

4. **Root**: The "Root" of the tree is akin to the base of the tree, where it all begins. It's the starting point and the topmost node of the tree, just like the base of the main trunk.

5. **Leaf**: Now, imagine the leaves of the tree as the "Leaf" nodes. These are the nodes that have no children (branches) extending from them.

6. **Subtree**: A "Subtree" is like a smaller tree growing from a particular branch. Imagine you choose one of the branches and consider all its connected branches and leaves as a separate tree - that's a subtree.


## Types of Trees

There are various types of trees, each with its unique characteristics and applications. Some common types of trees include:

- **Binary Tree**: A binary tree is a tree in which each node has at most two children, known as the left child and the right child.
- **Binary Search Tree**: A binary search tree is a binary tree where the left child of a node contains values less than the node, and the right child contains values greater than the node.
- **Balanced tree**: A tree in which the height of the left and right subtrees of any node differs by at most one.
- **AVL Tree**: An AVL tree is a self-balancing binary search tree, ensuring that the heights of its left and right subtrees differ by at most one.
- **B-Tree**: A B-tree is a self-balancing tree designed to maintain efficient operations on large datasets and external storage.
- **Trie**: A trie, also known as a prefix tree, is an ordered tree structure that stores a collection of strings, making it efficient for prefix-based operations.

Each type of tree has its own properties and use cases, allowing for efficient operations and solving specific problems.

## Basic Operations and Performance

In Python, there is no built-in data structure called "tree" like lists, dictionaries, or sets. However, you can create a tree data structure using classes and objects to represent nodes and their relationships. Typically, you'd define a Node class to represent individual elements in the tree and then implement methods to handle the tree's operations, such as insertion, deletion, and traversal.Additionally, the performance of a tree depends on various factors such as the type of tree (e.g., binary tree, balanced tree), the number of nodes, and the specific operations being performed. Here are some commonly used operations with time complexities:

**Different methods of traversing a tree:**
| Method                  | Description                                                         | Syntax             |
|-------------------------|---------------------------------------------------------------------|---------------------|
| Pre-order Traversal     | Visit all nodes in a tree by starting at the root. Visit current, left subtree, right subtree. | `preorder_traversal`  |
| In-order Traversal      | Traverse a tree by visiting the left subtree, current node, and right subtree. | `inorder_traversal`   |
| Post-order Traversal    | Traverse a tree by traversing the left subtree, right subtree, and visiting the current node. | `postorder_traversal` |
| Level-order Traversal   | Visit nodes at each level from left to right, starting from the root and moving down. | `levelorder_traversal` |

_Note: The time complexity for all tree traversal methods is O(n), where n is the number of nodes in the tree._

**Other various tree operations:**
| Method                  | Description                                                         | Syntax             |
|-------------------------|---------------------------------------------------------------------|---------------------|
| Serialization           | Convert a tree into a serialized format for storage or transmission. | `serialize_tree()`      |
| Deserialization         | Recreate a tree by reading and constructing nodes from a serialized format. | `deserialize_tree()`    |
| Tree Height             | Determining the maximum number of edges from the root to any leaf node. | `calculate_height()`, `tree_height()`    |
| Tree Copy/Clone         | Create a duplicate copy of a tree recursively.                       | `copy_tree()`           |
| Tree Merging            | Combine two trees into a single tree recursively.                    | `merge_trees()`         |
| Tree Recursive Trimming/Pruning | Remove nodes or subtrees from a tree recursively.              | `trim_tree()`, `prune_tree()` |
| Tree Recursive Validation | Check if a tree satisfies conditions recursively.                 | `validate_tree()`       |
| Tree Recursive Verification | Check if a tree satisfies conditions recursively. Return true if all nodes satisfy conditions, otherwise false. | `is_valid_tree()`       |


The time complexity for operations in a tree data structure generally depends on the number of nodes in the tree and is estimated to be O(n), where n is the number of nodes.

**However**, it's important to consider that these time complexities are general estimates and can vary based on specific implementation details and tree properties. The performance of operations can also be influenced by factors such as tree balance, node distribution, and the utilization of optimization techniques.

These methods and operations described are commonly used and applicable to different types of trees. However, it's worth noting that the specific implementation and efficiency of these operations may vary based on the properties and requirements of the particular tree structure being used.


## Implementation in Python

In this section, we will develop fundamental functions in Python to accomplish typical operations on a tree structure. These operations involve performing inorder, preorder, postorder, and level-order traversals on a binary tree to print the values of its nodes.

```python
from collections import deque

# Node class represents a node in the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inorder Traversal: Left -> Root -> Right
def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)    # Traverse the left subtree
        print(node.value, end=' ')      # Print the value of the current node
        inorder_traversal(node.right)   # Traverse the right subtree

# Preorder Traversal: Root -> Left -> Right
def preorder_traversal(node):
    if node is not None:
        print(node.value, end=' ')      # Print the value of the current node
        preorder_traversal(node.left)   # Traverse the left subtree
        preorder_traversal(node.right)  # Traverse the right subtree

# Postorder Traversal: Left -> Right -> Root    
def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)  # Traverse the left subtree
        postorder_traversal(node.right) # Traverse the right subtree
        print(node.value, end=' ')      # Print the value of the current node

# Level-order Traversal (Breadth-First Traversal)
def levelorder_traversal(node):
    if node is None:
        return

    queue = deque()     # Create a deque (queue) to hold nodes during traversal
    queue.append(node)  # Enqueue the root node

    while queue:
        current_node = queue.popleft()      # Dequeue the current node from the front of the queue
        print(current_node.value, end=' ')  # Print the value of the current node

        # Enqueue the left child if it exists
        if current_node.left:
            queue.append(current_node.left)

        # Enqueue the right child if it exists
        if current_node.right:
            queue.append(current_node.right)

# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Perform traversals
print("Inorder Traversal:")
inorder_traversal(root)

print("\nPreorder Traversal:")
preorder_traversal(root)

print("\nPostorder Traversal:")
postorder_traversal(root)

print("\nLevel-order Traversal:")
levelorder_traversal(root)
```

## Binary Search Tree (BST)

Now we are going dive into Binary Search Tree as it offers a powerful and efficient way to store and manage data in a hierarchical manner. Its unique structure ensures that the elements are sorted, allowing for fast search, insertion, and deletion operations, all achieved in logarithmic time complexity.

<div style="text-align: center;">
    <a href="/FINAL/Python%20Files/03-treeSample-01.py">
        <img src="/FINAL/Picture%20Files/BinaryvsLinearSearch.gif" alt="BST Compare to a Linear Search" width="400" height="255" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);" />
    <br>Click here to see this example</a>
</div>

<br>
A binary search tree is a type of binary tree that follows a specific ordering property. The left subtree of a node contains only values lesser than the node's value, while the right subtree contains only values greater than the node's value.

<br>
<br>
<div style="text-align: center;">
    <a href="/FINAL/Python%20Files/03-treeSample-01.py">
        <img src="/FINAL/Picture%20Files/Inserting&SortingBST.gif" alt="BST Showing Insert and Sorting" width="800" height="255" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);" />
    <br>Click here to see this example</a>
</div>
<br>

**Basic tree operations with specific time complexities**
| Method                  | Description                                                         | Syntax              | Average Time Complexity | Worst-case Time Complexity |
|-------------------------|---------------------------------------------------------------------|---------------------|------------------------|---------------------------|
| Tree Insertion          | Adding a new node to the tree by comparing values to determine the appropriate position. | `insert_node(value)`  | O(log n)               | O(n)                      |
| Tree Deletion           | Removing a node from the tree, considering the number of children the node has. | `delete_node(value)`  | O(log n)               | O(n)                      |
| Tree Search             | Locating a specific node in the tree by comparing values and traversing the left or right subtree. | `search_node(value)`  | O(log n)               | O(n)                      |
| Tree Balancing          | Ensuring the tree is balanced by rearranging nodes to minimize the height difference. | `balance_tree()`      | O(n log n)             | O(n log n)                |

## Applications of Tree

Trees find applications in various domains, including:

- Representing hierarchical relationships, such as file systems, organization charts, and family trees.
- Implementing search algorithms like binary search and binary search tree.
- Creating efficient data structures like heaps, tries, and self-balancing trees.
- Constructing decision trees for problem-solving and decision-making processes.
- Modeling and solving graph-related problems, such as minimum spanning trees and shortest paths.

Trees provide a flexible and powerful structure to organize and manipulate data efficiently, depending on the problem requirements.


## Example Problems

**Problem Statement:**
Suppose you are tasked with implementing a system to manage a library's book collection using a binary search tree (BST). Each book is identified by its unique ISBN (International Standard Book Number). Design a program that allows librarians to efficiently insert new books into the library's catalog, search for specific books by their ISBN, and remove books from the collection when they are no longer available.

Your program should provide the following functionalities:

1. **Insertion**: Implement a function to insert a new book into the library's catalog using the ISBN as the key for the BST. Ensure that the books are inserted in a way that maintains the BST's properties.

2. **Searching**: Create a function to search for a book by its ISBN in the binary search tree. If the book is found, the function should return its details (e.g., title, author, genre). Otherwise, it should indicate that the book is not in the library.

3. **Deletion**: Implement a function to remove a book from the library's catalog when it is no longer available. Ensure that the BST properties are preserved after the deletion operation.

4. **Height Calculation**: Provide a function to calculate the height of the BST, representing the maximum number of levels in the tree.

Use `Book`, `TreeNode`, and `BookCatalogBST` classes to implement the library's book catalog system. Test the functionality of your program by inserting several books into the catalog, searching for specific books by their ISBN, and deleting books that are no longer available. Finally, print the height of the BST before and after the deletions to demonstrate the efficiency of your program's implementation.

**Solution:**
```python

class Book:
    """Class to represent a book in the library."""
    def __init__(self, isbn, title, author, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} ({self.genre})"


class TreeNode:
    """Node class for representing each node in the binary search tree."""
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookCatalogBST:
    """Binary Search Tree class for managing the library's book catalog."""
    def __init__(self):
        self.root = None

    def insert(self, book):
        """Insert a new book into the binary search tree."""
        self.root = self._insert_recursive(self.root, book)

    def _insert_recursive(self, root, book):
        """Helper function for recursive insertion."""
        if root is None:
            return TreeNode(book)
        if book.isbn < root.book.isbn:
            root.left = self._insert_recursive(root.left, book)
        elif book.isbn > root.book.isbn:
            root.right = self._insert_recursive(root.right, book)
        return root

    def delete(self, isbn):
        """Delete a book from the binary search tree by its ISBN."""
        self.root = self._delete_recursive(self.root, isbn)

    def _delete_recursive(self, root, isbn):
        """Helper function for recursive deletion."""
        if root is None:
            return root
        if isbn < root.book.isbn:
            root.left = self._delete_recursive(root.left, isbn)
        elif isbn > root.book.isbn:
            root.right = self._delete_recursive(root.right, isbn)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp = temp.left
            root.book = temp.book
            root.right = self._delete_recursive(root.right, temp.book.isbn)
        return root

    def search(self, isbn):
        """Search for a book in the binary search tree by its ISBN."""
        return self._search_recursive(self.root, isbn)

    def _search_recursive(self, root, isbn):
        """Helper function for recursive search."""
        if root is None or root.book.isbn == isbn:
            return root.book if root else None
        if isbn < root.book.isbn:
            return self._search_recursive(root.left, isbn)
        return self._search_recursive(root.right, isbn)

    def height(self):
        """Calculate the height of the binary search tree."""
        return self._height_recursive(self.root)

    def _height_recursive(self, root):
        """Helper function for recursive height calculation."""
        if root is None:
            return 0
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)
        return max(left_height, right_height) + 1

# Example usage
if __name__ == "__main__":
    book_catalog = BookCatalogBST()

    # Inserting books into the catalog
    book_catalog.insert(Book("9780061122415", "To Kill a Mockingbird", "Harper Lee", "Fiction"))
    book_catalog.insert(Book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction"))
    book_catalog.insert(Book("9781984823155", "1984", "George Orwell", "Science Fiction"))
    book_catalog.insert(Book("9781400079988", "The Catcher in the Rye", "J.D. Salinger", "Fiction"))
    book_catalog.insert(Book("9780385490818", "The Kite Runner", "Khaled Hosseini", "Fiction"))

    # Searching for a book by ISBN
    isbn_to_search = "9780743273565"
    found_book = book_catalog.search(isbn_to_search)
    if found_book:
        print(f"Book with ISBN {isbn_to_search} found: {found_book}")
    else:
        print(f"Book with ISBN {isbn_to_search} not found in the catalog.")

    # Deleting a book by ISBN
    isbn_to_delete = "9781984823155"
    book_catalog.delete(isbn_to_delete)
    print(f"Book with ISBN {isbn_to_delete} has been removed from the catalog.")

    # Print the height of the BST after deletions
    print("Binary Search Tree height:", book_catalog.height())

```

You can check a more detailed example just like this _**[HERE](/FINAL/Python%20Files/03-treeSample-02.py)**_ 

## Common Errors

While working with trees, there are some common errors that developers may encounter. Being aware for some of these issues can help you avoid pitfalls and improve the efficiency and correctness of your code:

1. **Infinite Recursion**: 
When implementing recursive tree functions, be cautious about potential infinite recursion. Ensure that your recursive functions have proper base cases to terminate the recursion.
2. **Memory Overflow**: 
Depending on the size and depth of the tree, certain operations like traversals or tree manipulations may lead to memory overflow. Always analyze the memory requirements of your code and consider using iterative approaches or optimization techniques to reduce memory consumption.
3. **Unbalanced Trees**: 
Unbalanced trees, such as skewed binary search trees, can lead to inefficient operations. When implementing a tree, consider using self-balancing techniques like AVL trees or Red-Black trees to maintain balance and improve performance.
4. **Missing Base Cases**: 
Recursive functions require proper base cases to terminate the recursion. Not providing appropriate base cases can lead to infinite recursion or incorrect results.
5. **Incorrect Tree Traversal Order**: 
Make sure to follow the correct order of traversal (e.g., pre-order, in-order, post-order, or level-order) based on the requirements of your specific problem. Using the wrong traversal order can lead to incorrect results.
6. **Data Type Mismatches**: 
When comparing or manipulating values within the tree, ensure that the data types match correctly. Mismatches can lead to unexpected behavior or errors.
7. **Duplicated Values**: 
When inserting elements into a binary search tree, avoid duplicating values if the tree does not allow duplicates. Implement proper checks to handle duplicate values according to your requirements.
8. **Incorrect Tree Structure**: 
When building custom tree implementations, ensure that the tree structure is maintained correctly. Incorrect links between nodes or misplaced values can lead to unexpected behavior.
9. **Inefficient Operations**: 
Some operations, such as finding the height of an unbalanced binary tree, may have inefficient time complexities. Consider using appropriate data structures or techniques to optimize specific operations.
10. **Inconsistent Node Handling**: 
Be consistent in handling NULL nodes or missing child nodes during tree manipulations or traversals. Properly handle such cases to avoid unexpected behavior.

Always thoroughly test your tree implementations and algorithms to verify their correctness and performance. Identifying and resolving common errors will help you build more reliable and efficient tree-based solutions.

## Independent Problem

Now it's your turn to solve a problem using the Tree data structure.

**Problem 1:** 
Your objective is to develop a Python script that analyzes a specified directory, creating a hierarchical tree structure using TreeNode objects to represent its subdirectories and files. The script should traverse the directory, calculating and presenting the total size occupied by files within the directory and its subdirectories. Additionally, it must count and display the number of directories and files present throughout the directory tree, as well as determine and reveal the maximum depth of the directory tree (the longest path from the root directory to a leaf node). Furthermore, the script should identify and present any duplicate files found within the directory and its subdirectories.

By completing this script, you will have a powerful tool to gain insights into the content distribution, storage usage, and potential redundancy within the directory and its nested structures.

Use and write your solution in this Python file **[Tree Problem 1](/FINAL/Python%20Files/Problems/03-treeProblem-1.py)**.

_*To help you, I have prepared a **[Solution 1](/FINAL/Python%20Files/Solutions/03-treeSolution-1.py)** for the given problem where you can check your own solution and compare it with a possible correct implementation. **Try to avoid looking at the solution to see how well you can implement a TREE Data Structure on your own.**_

### Good luck!

---

## Conclusion and Next Steps

That concludes the tutorial on trees!

In this module, we covered the tree data structure. We explored different types of trees, including binary trees and binary search trees, along with tree traversal algorithms. Trees offer a hierarchical way to organize data and solve various problems efficiently. Now that you have a solid understanding of trees, feel free to continue exploring other data structures.

Keep practicing working with trees and explore different tree operations and algorithms to deepen your understanding. Feel free to go back to the **_Welcome Page_** for an overview of the tutorial or back to **_Stack_** and **_Set_** topic.

If you'd like, you can explore additional data structures or revisit any of the previous modules in the tutorial.

<div style="display: flex; justify-content: space-between;">

<a href="/FINAL/02-Set.md"><h4>:arrow_left: Return to Set Tutorial</h4></a>

<a href="/FINAL/01-Stack.md"><h4>:arrow_up: Go Back to Stack Tutorial :arrow_up:</h4></a>

</div>

<div style="text-align: center;">

<a href="/FINAL/00-Welcome.md"><h5>:back: Return to the Welcome Page</h5></a>

<h1>Keep Up the Great Work!</h1>
</div>

---