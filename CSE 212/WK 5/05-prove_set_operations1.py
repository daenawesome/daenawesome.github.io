"""
CSE212 
(c) BYU-Idaho
05-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def intersection(set1, set2):
    """
    Perform an intersection between 2 sets. An intersection will contain
    the items in common between both sets. Do not use the set 
    operators (+, -, *, &, |) and functions (intersection, union) 
    that are built-in to Python.
    """
    # Initialize an empty set for the intersection
    result = set()

    # Iterate over each item in set1
    for item in set1:
        # Check if the item exists in set2
        if item in set2:
            # Add the item to the intersection set
            result.add(item)

    # Return the intersection set
    return result

def union(set1, set2):
    """
    Perform a union between 2 sets. A union will contain all the items
    from both sets. Do not use the set operators (+, -, *, &, |)
    and functions (intersection, union) that are built-in to Python.
    """
    # Create a new set to hold the union
    result = set()

    # Add items from set1 to the result set
    for item in set1:
        result.add(item)

    # Add items from set2 to the result set
    for item in set2:
        result.add(item)

    # Return the union set
    return result

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(intersection(s1, s2))  # Should show {4, 5}
print(union(s1, s2))  # Should show {1, 2, 3, 4, 5, 6, 7, 8}

s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 10}
print(intersection(s1, s2))  # Should show an empty set
print(union(s1, s2))  # Should show {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
