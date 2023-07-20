# Stack Tutorial

 **:back: [Return to the Welcome Page](00-welcome.md)**
 
---
<div style="display: flex;">
  <div style="width: 70%;">
    <h2>Table of Contents</h2>
    <ul>
      <li><a href="#introduction">Introduction</a></li>
      <li><a href="#purpose">Purpose</a></li>
      <li><a href="#basic-operations-and-performance">Basic Operations and Performance</a></li>
      <li><a href="#implementation-in-python">Implementation in Python</a></li>
      <li><a href="#applications-of-stack">Applications of Stack</a></li>
      <li><a href="#example-problems">Example Problems</a></li>
      <li><a href="#common-errors">Common Errors</a></li>
      <li><a href="#independent-problems">Independent Problems</a></li>
      <li><a href="#conclusion-and-next-steps">Conclusion and Next Steps</a></li>
    </ul>
  </div>
  <div style="width: 30%; padding-left: 20px;">
    <div style="text-align: center;">
      <img src="/FINAL/Picture%20Files/bookstacking.gif" alt="Book Stacking Animation" width="200" height="300" />
    </div>
  </div>
</div>


## Introduction <a name="introduction"></a>

In this tutorial, we will explore the purpose, basic operations and performance, it's usage, problem-solving capabilities, and common errors associated with stacks. 

A **stack** is a linear data structure that follows the _Last-In-First-Out (LIFO)_ principle. It can be visualized as a stack of objects, where the last object placed on top is the first one to be removed. Think of a stack of books. You can only remove the book that is at the top of the stack, and to add a new book, you place it on top of the stack.

## Purpose <a name="purpose"></a>

The purpose of a stack is to store and retrieve data in a specific order. It provides an efficient way to manage function calls, track program execution, undo/redo operations, and perform various other tasks.

## Basic Operations and Performance <a name="basic-operations-and-performance"></a>

<div style="text-align: center;">
    <img src="/FINAL/Picture%20Files/stackops.png" alt="Stack Operations Image" width="800" height="300" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);" />
</div>

In Python, there are two options to create a stack: utilizing a list or the `'deque'` class from the `'collections'` module. In this discussion, we will cover the fundamental operations of a stack, namely push, pop, and peek.

**Push:**
To add an element to the stack, you can use the `'append()'` method if using a list or the `'append()'` method if using a deque. This operation adds the element to the top of the stack. Regardless of the size of the stack, the time it takes to push an element remains constant when using the `'deque'` class. However, if you are using a list, the time complexity of `'append()'` is amortized O(1) but may occasionally require resizing the underlying array, resulting in an O(n) time complexity in those cases.

**Pop:**
To remove the topmost element from the stack, you can use the `pop()` method if using a list or the `pop()` method if using a deque. This operation removes and returns the top element of the stack. Similar to the push operation, when using the `deque` class, the time complexity of `pop()` is O(1) regardless of the stack's size. However, with a list, the time complexity of `pop()` is also amortized O(1), but in rare cases, it may require resizing the underlying array, resulting in an O(n) time complexity.

**Peek:**
To view the topmost element without removing it, you can access the last element of the list or deque. This operation allows you to examine the value of the top element. It does not require modifying the stack and can be performed in constant time regardless of the stack's size.

Performance of the basic operations of a stack, namely push, pop, and peek, all have a time complexity analyzed using Big O notation of O(1) when using the `deque` class. This makes stacks implemented with `deque` an efficient data structure for managing elements in a Last-In-First-Out manner.

***Note:** The actual performance of the list-based implementation may vary depending on the implementation details and the underlying data structure used.*


## Implementation in Python <a name="implementation-in-python"></a>
In Python, you can implement a stack using a list or by creating a custom Stack class. Let's look at an example of using a list as a stack:

```python
stack = []  # Creating an empty stack

# Push operation
stack.append(10)  # Adding element 10 to the top of the stack
stack.append(20)  # Adding element 20 to the top of the stack

# Pop operation
top_element = stack.pop()  # Removing the top element from the stack
print(top_element)  # Output: 20

# Peek operation
top_element = stack[-1]  # Accessing the top element without removing it
print(top_element)  # Output: 10
```

Alternatively, you can create a custom Stack class using the principles of object-oriented programming.

## Applications of Stack <a name="applications-of-stack"></a>
Stacks have various applications in programming. Some common scenarios where stacks are useful include:
- Function call management (e.g., call stack)
- Undo/Redo operations (e.g., text editor)
- Balancing parentheses and checking syntax in expressions
- Depth-first search algorithms

Stacks are particularly useful in solving problems that involve a last-in-first-out order, such as balancing parentheses, evaluating postfix expressions, or checking the validity of a string with nested brackets.

For example, solving the Tower of Hanoi puzzle can be achieved using a stack data structure.
<div style="text-align: center;">
    <img src="/FINAL/Picture%20Files/ToH.gif" alt="Tower of Hanoi" width="600" height="200" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);"/>
</div>

You can check this out **[Here]( /FINAL/Python%20Files/Tower-of-Hanoi.py)**.

## Example Problems <a name="example-problems"></a>

Let's consider a problem where we need to reverse a string using a stack.

**Problem Statement:** 
Given a string, reverse its characters using a stack.

```python
def reverse_string(string):
    stack = []
    reversed_string = ""

    for char in string:
        stack.append(char)

    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Test the function
text = "Hello, world!"
reversed_text = reverse_string(text)
print(reversed_text)  # Output: "!dlrow ,olleH"
```

**Solution:** To reverse a string using a stack, you can iterate over the characters in the input string and push them onto the stack. Then, pop the elements from the stack to obtain the reversed string.

Here's the step-by-step solution:
1. Create an empty stack.
2. Push each character of the input string onto the stack. This operation has a time complexity of O(n), where n is the length of the string.
3. Pop each character from the stack and append it to a new string. This operation also has a time complexity of O(n) because popping from the stack takes constant time per element, and there are n elements in the stack.
4. Return the new string as the reversed version of the input.

The overall time complexity of the `reverse_string` function is O(n) because both the push and pop operations iterate over the string with n characters. Additionally, the space complexity is also O(n) because the function uses an additional stack to store the characters.

Therefore, the `reverse_string` function has linear time and space complexity, making it an efficient solution for reversing a string using a stack.

## Common Errors <a name="common-errors"></a>

- Stack Overflow: If you keep pushing elements onto the stack without any limit, it may cause a stack overflow error.
- Stack Underflow: If you try to pop an element from an empty stack, it may cause a stack underflow error.
- Forgetting to check if the stack is empty: Before performing any pop or peek operations, always check if the stack is empty to avoid errors.

To check if the stack is empty, you can use the `len()` function or the `not` keyword in Python. Here's an example:

```python
# Check if the stack is empty
if len(stack) == 0:
    print("Stack is empty")
```
or
```python
# Check if the stack is empty
if not stack:
    print("Stack is empty")
```

## Independent Problems <a name="independent-problems"></a>

Now it's your turn to solve a problem using the stack data structure.

**Problem 1:** 
Implement the function `'is_balanced'` that takes a string containing parentheses as input and returns True if the parentheses are balanced, and False otherwise. 
Use and write your solution in this Python file **[Stack Problem 1](/FINAL/Python%20Files/Problems/01-stackProblem-1.py)**.

**Problem 2:** 
You are implementing a text editor that supports undo and redo operations. Implement the classes `'TextEditor'` and `'Stack'` to enable these operations. 
Use and write your solution in this Python file **[Stack Problem 2](/FINAL/Python%20Files/Problems/01-stackProblem-2.py)**.

**Problem 3:** 
Implement a function named `'reverse_words_in_phrase'` that takes a single parameter `'phrase'` representing the input phrase. The function should return the input phrase with each word reversed. 
Use and write your solution in this Python file **[Stack Problem 3](/FINAL/Python%20Files/Problems/01-stackProblem-3.py)**.

_*To help you, I have prepared a **[Solution 1](/FINAL/Python%20Files/Solutions/01-stackSolution-1.py)**, **[Solution 2](/FINAL/Python%20Files/Solutions/01-stackSolution-2.py)** & **[Solution 3](/FINAL/Python%20Files/Solutions/01-stackSolution-3.py)** for the given problems where you can check your own solution and compare it with a possible correct implementation. **Try to avoid looking at the solution to see how well you can implement a stack on your own.**_

### Good luck!
---
## Conclusion and Next Steps <a name="conclusion-and-next-steps"></a>

Congratulations on completing the Stack module! In this tutorial, we covered what Stack is, its purpose, basic operations and performance, implementation, and applications of the stack data structure. We also solved a problem using a stack and provided you with problems to work on.

Remember to practice implementing and using stacks in different scenarios to reinforce your understanding. In the next module, we will explore the Set data structure. 

Feel free to go back to the welcome page for an overview of the tutorial or proceed to the next topic.

<div style="display: flex; justify-content: space-between;">

<a href="/FINAL/00-Welcome.md"><h4>:back: Return to the Welcome Page</h4></a>

<a href="/FINAL/02-Set.md"><h4>Go to Set Tutorial :arrow_right:</h4></a>

</div>

<div style="text-align: center;">

<a href="/FINAL/03-Tree.md"><h5>:arrow_down: Skip & Go to Tree Tutorial :arrow_down:</h5></a>

<h1>Happy learning!</h1>

</div>

---