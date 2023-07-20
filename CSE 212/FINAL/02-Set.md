# Set Tutorial

<font size="1.5"> 

**:back: [Return to the Welcome Page](00-welcome.md)**
**:arrow_left: [Back to Stack Tutorial](01-Stack.md)** 
</font>

---

<div style="display: flex;">
  <div style="width: 70%;">
    <h2>Table of Contents</h2>
    <ul>
      <li><a href="#introduction">Introduction</a></li>
      <li><a href="#purpose">Purpose</a></li>
      <li><a href="#basic-operations-and-performance">Basic Operations and Performance</a></li>
      <li><a href="#implementation-in-python">Implementation in Python</a></li>
      <li><a href="#applications-of-set">Applications of Set</a></li>
      <li><a href="#example-problems">Example Problems</a></li>
      <li><a href="#common-errors">Common Errors</a></li>
      <li><a href="#independent-problems">Independent Problems</a></li>
      <li><a href="#conclusion-and-next-steps">Conclusion and Next Steps</a></li>
    </ul>
  </div>
  <div style="width: 30%; padding-left: 20px;">
    <div style="text-align: center;">
      <img src="/FINAL/Picture%20Files/drawingkeys.gif" alt="Drawing Keys Animation" width="200" height="300" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);"/>
    </div>
  </div>
</div>

## Introduction
In this module, we will explore the purpose, basic operations and performance, its usage, problem-solving capabilities, and common errors associated with sets in Python.

A **set** is a mutable collection of unique elements, without any particular order unlike a stack which focuses on maintaining a specific order and allows elements to be added or removed from the top, following the LIFO principle. Each element in a set is distinct, and duplicates are not allowed. Sets provide efficient operations to add elements, remove elements, and checking the existence of elements.

In Python, sets are mutable collections that store unique elements. However, the elements in a set must be immutable (that means you cannot change/mutate an element of a set once declared). However, you can add/remove elements from the set.

If that was confusing, let me try and summarize:
- A set is a mutable, unordered group of elements, where the elements themselves are immutable.
- Another characteristic of a set is that it may include elements of different types. This means you can have a group of numbers, strings, and even tuples, all in the same set!

Imagine you have a key ring that holds various keys, it ensures each key is unique and has no specific order or ranking. Similar to accessing any key directly from the key ring, you can retrieve any element from the set based on its unique properties, without following a specific order. The set data structure embodies the principles of uniqueness, unorderedness, and direct access, making it a valuable tool for handling collections of distinct elements in Python.

## Purpose
The purpose of a set is to store a collection of unique elements. It allows for efficient membership testing, eliminating duplicates, and performing set operations like union, intersection, and difference.

## Basic Operations and Performance
<div style="text-align: center;">
    <img src="/FINAL/Picture%20Files/setops.png" alt="Set Example Image" width="800" height="200" style="box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);"/>
</div>

In Python, you can create a set using the `set()` function or curly braces `{}`. In this discussion, we will cover the fundamental operations of a set, namely the `add` operation adds an element to the set, `remove` deletes an element, and the `in` operator allows you to check if an element is present in the set.

**Add**:
To add an element to a set, you can use the `add()` method. The performance of a set can be analyzed using Big O notation. O(1) Adding an element to a set takes constant time.

**Remove**:
To remove an element from a set, you can use the `remove()` method or the `discard()` method if you want to avoid raising an error when the element doesn't exist. O(1) - Removing an element from a set also takes constant time.

**Check Membership**:
To check if an element is present in a set, you can use the `in` keyword. O(1) - Checking if an element exists in a set is a constant-time operation.

Performing set operations like union, intersection, and difference takes time proportional to the size of the smaller set involved. The time complexity is O(min(len(set1), len(set2))). The `union` operation combines two sets and returns a new set containing all elements from both sets. Its time complexity is also O(min(len(set1), len(set2))).


You can also use other operations like `pop` and `clear` to manipulate sets.

Shown below are examples and definition of terms for your easy reference.


| Method          | Description                               |
|-----------------|-------------------------------------------|
| `add()`         | Adds the specified `element` to the set. If the `element` is already present, it does nothing.|
| `clear()`       | Removes all elements from the set, making it empty.|
| `copy()`        | Returns a shallow copy of the set.|
| `difference()`  | Returns a new set containing elements that are present in the set but not in the specified iterable or set.|
| `difference_update()` | Removes all elements from the set that are also present in the specified iterable or set.|
| `discard()`     | Removes an element from the set if it is present. If the element is not present, it does nothing.|
| `intersection()` | Returns a new set containing elements that are common to the set and the specified iterable or set.|
| `intersection_update()` | Updates the set with elements that are common to the set and the specified iterable or set, removing elements that are not present in both.|
| `isdisjoint()`  | Returns `True` if the set has no elements in common with the specified iterable or set. Otherwise, it returns `False`.|
| `issubset()`    | Returns `True` if all elements of the set are present in the specified iterable or set. Otherwise, it returns `False`.|
| `issuperset()`  | Returns `True` if the set contains all elements of the specified iterable or set. Otherwise, it returns `False`.|
| `pop()`         | Removes and returns an arbitrary element from the set. Raises a `KeyError` if the set is empty.|
| `remove()`      | Removes an element from the set. If the element is not present, it raises a `KeyError`.|
| `symmetric_difference()` | Returns a new set containing elements that are present in either the set or the specified iterable or set, but not both.|
| `symmetric_difference_update()` | Updates the set with elements that are present in either the set or the specified iterable or set, but not both, removing elements that are present in both.|
| `union()`       | Returns a new set containing all elements that are present in the set and the specified iterable or set.|
| `update()`      | Updates the set with elements from the specified iterable or set.|

These methods provide various ways to manipulate and perform operations on sets in Python. Remember to refer to the official Python documentation for more detailed explanations and usage examples of each method.


## Implementation in Python
In Python, the set data structure is implemented using a technique called hashing. Hashing is a process that converts an object into a unique numerical value called a hash code. This enables efficient insertion, removal, and membership testing operations on sets. Sets use a hash table, which is an array of buckets where elements are stored based on their hash values. Behind the scenes, sets use a hash table, which is an array of buckets where elements are stored based on their hash values. Here's an example of how you can create a set and perform basic operations:

```python
# Creating a set
my_set = set()

# Adding elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Removing an element from the set
my_set.remove(2)

# Checking membership
if 3 in my_set:
    print("Element found in the set!")

# Displaying the set
print(my_set)  # Output: {1, 3}
```

## Applications of Set
Sets have various applications due to their unique properties. Some common scenarios where sets are useful includes:

- Removing duplicates from a list or dataset
- Checking for membership or existence of elements.
- Performing mathematical set operations such as set intersection, union, and difference
- Implementing algorithms like breadth-first search (BFS) and graph traversal.
- Finding common elements between multiple sets.


Sets can be utilized to solve specific problems efficiently. For example, finding the intersection of two lists can be achieved using a set data structure.

When using sets, it's important to consider potential errors or challenges. Common issues include accidentally modifying a set while iterating over it or misunderstanding the concept of uniqueness.

Sets are particularly useful when you need to deal with a collection of unique elements and perform operations related to set theory.

## Example Problem

**Problem:** *Social Media Influencer Analysis*
You are working as a data analyst for a social media marketing agency. Your task is to analyze the followers of various social media influencers and identify potential collaborations for a client's new product launch. The influencers' followers are stored in sets, representing unique user IDs.

You have the following sets available:
```python
Helaman_followers = {'Kishkumen486', 'Mathoni512', 'Shimnilom534', 'Chemish555'}
Alma_followers = {'Shimnilom534', 'Chemish555', 'Shemlon570', 'Aha595'}
Nephi_followers = {'Shimnilom534', 'Aha595', 'Irijah601', 'Giddianhi440'}
```

Your goal is to find users who are following multiple influencers, as they are likely to have a higher influence on social media. Additionally, you need to identify users who are following only one influencer, as they might be interested in collaborating with your client.

**Solution:**
To solve this problem, you can utilize the set operations provided by Python. Here's an outline of the steps you can take:
1. Combine all the sets using the union operation (`|`) to create a single set of unique followers.
2. Use the intersection operation (`&`) to find users who are following multiple influencers.
3. Use the difference operation (`-`) to find users who are following only one influencer.

```python
# Step 1: Combine all sets
all_followers = Helaman_followers | Alma_followers | Nephi_followers

# Step 2: Find users following multiple influencers
following_multiple = Helaman_followers & Alma_followers & Nephi_followers

# Step 3: Find users following only one influencer
following_single = (Helaman_followers ^ Alma_followers ^ Nephi_followers) - following_multiple

print("Users following multiple influencers:", following_multiple) 
# Output: Users following multiple influencers: {'Shimnilom534'}

print("Users following only one influencer:", following_single)
# Output: Users following only one influencer: {'Irijah601', 'Shemlon570', 'Mathoni512', 'Giddianhi440', 'Kishkumen486'}
```

The output of the above code will provide you with the users who are following multiple influencers and the users who are following only one influencer. This information can help your client identify potential collaboration opportunities and target their marketing strategies accordingly.

You can check this problem out **[HERE](/FINAL/Python%20Files/02-setSample-01.py)** for more details.


## Common Errors
- Modifying a set while iterating over it: It is not recommended to modify a set while iterating over it using a for loop. This can lead to unexpected behavior or errors. For example, if you remove an element from the set while iterating, it may result in skipping or repeating elements. If you need to modify a set while iterating, consider creating a copy of the set or using a different approach.
- Misunderstanding uniqueness: Sets enforce uniqueness, which means each element can only appear once in the set. If you try to add a duplicate element, it will not be added to the set. It's important to understand this behavior to avoid unexpected results.
- Using the wrong set operation: When performing set operations like union, intersection, or difference, make sure you are using the correct method based on your requirements. Using the wrong method can lead to incorrect results.
- Forgetting to convert data types: Sets in Python can only contain hashable elements. Hashable elements are those that have a hash value and can be used as dictionary keys or set elements. Examples of hashable elements are numbers, strings, and tuples. On the other hand, unhashable elements like lists or dictionaries cannot be used in sets. Which means you may encounter errors if you try to add unhashable objects to a set. Make sure to convert the data types appropriately before adding elements to a set.
- Neglecting to handle errors: Some set operations, such as removing an element using the `remove()` method, can raise an error if the element is not present in the set. It's important to handle such errors using try-except blocks or by using the `discard()` method instead, which doesn't raise an error if the element is not found.

## Independent Problems <a name="independent-problems"></a>

Now it's your turn to solve a problem using the set data structure.

**Problem 1:** 
Implement the `'count_unique_words(text)'` function to correctly analyze the text, and return the following information: the number of unique words, the number of duplicate words and the number of non-unique words (total words minus unique words)

Use and write your solution in this Python file **[Set Problem 1](/FINAL/Python%20Files/Problems/02-setProblem-1.py)**.

**Problem 2:** 
You are tasked with implementing a friend suggestion feature for your social media application. Implement the `'suggest_friends(user_id, num_suggestions)'` function to be able to generate friend suggestion feature based on shared interests. 

Use and write your solution in this Python file **[Set Problem 2](/FINAL/Python%20Files/Problems/02-setProblem-2.py)**.

_*To help you, I have prepared a **[Solution 1](/FINAL/Python%20Files/Solutions/02-setSolution-1.py)** & **[Solution 2](/FINAL/Python%20Files/Solutions/02-setSolution-2.py)** for the given problems where you can check your own solution and compare it with a possible correct implementation. **Try to avoid looking at the solution to see how well you can implement a SET on your own.**_

### Good luck!
---

## Conclusion and Next Steps

Congratulations on completing the Set module! In this tutorial, we covered the purpose, basic operations, performance, implementation in Python, applications, example problems, common errors, and next steps related to the set data structure. We also solved a problem using a set and provided you with a new problems to work on.

Continue practicing working with sets and exploring different set operations to enhance your understanding. In the next module, we will explore the Tree data structure.

<div style="display: flex; justify-content: space-between;">

<a href="/FINAL/01-Stack.md"><h4>:arrow_left: Return to Stack Tutorial </h4></a>

<a href="/FINAL/03-Tree.md"><h4>Go to Tree Tutorial :arrow_right:</h4></a>

</div>

<div style="text-align: center;">

<a href="/FINAL/00-Welcome.md"><h5>:back: Return to the Welcome Page</h5></a>

<h1>Keep Going!</h1>

</div>

---