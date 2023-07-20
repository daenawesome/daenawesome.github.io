"""
CSE212 
(c) BYU-Idaho
01-Teach - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def list_selector(list1, list2, selector):
    """
    The list1 and list2 inputs will be combined into a single
    list.  The order in which they are added is determined by 
    the selector list.  The selector list will only contain
    the values 1 or 2.  A value of 1 means to select the next
    value from list 1.  A value of 2 means to select the next 
    value from list 2.  It is assumed that the selector list
    will not contain any invalid values and it is also assumed
    that the sizes of list1 and list2 agree with the selector 
    list.
    """
    # Initialize two variables to keep track of the positions in the lists
    pos_list1 = 0  
    pos_list2 = 0
    
    # Initialize an empty list to hold the result
    result = []
    
    # Loop through each element in the selector list
    for s in selector:
        # If the selector is 1, append the element at the current position in list1 to the result
        if s == 1:
            result.append(list1[pos_list1])
            # Increment the position in list1
            pos_list1 += 1
        
        # If the selector is 2, append the element at the current position in list2 to the result
        elif s == 2:
            result.append(list2[pos_list2])
            # Increment the position in list2
            pos_list2 += 1
    
    # Return the resulting list
    return result

l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
select = [1, 1, 1, 2, 2, 1, 2, 2, 2, 1]
print(list_selector(l1, l2, select))  # [1, 2, 3, 2, 4, 4, 6, 8, 10, 5]

l1 = ['A', 'A', 'A', 'A', 'A']
l2 = ['B', 'B', 'B', 'B', 'B']
select = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(list_selector(l1, l2, select))  # ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', ]

"""
The 'list_selector' function takes three arguments: 'list1', 'list2', and 'selector'.

'list1' and 'list2' are two lists of equal length, which will be combined to form a single list. 
    'selector' is a list that contains only the integers 1 and 2, which determines the order 
    in which the elements from 'list1' and 'list2' will be added to the resulting list.

The function initializes two variables, 'pos_list1' and 'pos_list2', to keep track of the current 
    position in 'list1' and 'list2', respectively. It also initializes an empty list, 'result', 
    to hold the resulting list.

The function then loops through each element in the 'selector' list. If the current element is 1, 
    the element at the current position in 'list1' is appended to the 'result' list, and the 
    'pos_list1' variable is incremented. If the current element is 2, the element at the 
    current position in 'list2' is appended to the result list, and the 'pos_list2' variable is incremented.

Finally, the function returns the resulting list.
"""

"""
l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
select = [1, 1, 1, 2, 2, 1, 2, 2, 2, 1]

| 1 | 2 | 3 | 4 | 5 |
  ^   ^   ^   ^   ^
  L1  L1  L1  L2  L2

| 2 | 4 | 6 | 8 | 10|
  ^   ^   ^   ^   ^
  L2  L2  L2  L2  L2

| 1 | 2 | 3 | 2 | 4 | 4 | 6 | 8 | 10 | 5 |
  ^   ^   ^   ^   ^   ^   ^   ^    ^   ^
  L1  L1  L1  L2  L2  L1  L2  L2   L2  L1

At each step, the 'selector' list determines 
    whether the next element should be taken from 
    'list1' or 'list2'. The variables 'pos_list1' and 
    'pos_list2' keep track of the current position 
    in each list, and are incremented as elements 
    are added to the result list
"""