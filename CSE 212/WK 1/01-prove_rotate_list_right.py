"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

# list slicing approach
def rotate_list_right(data, amount):
    """
    Rotate the 'data' to the right by the 'amount'. 
    For example, if the data is [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    and an amount is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4]. The value of amount will 
    be in the range of 1 and len(data).
    """
    # Split the list into two parts
    left_part = data[:len(data)-amount]
    right_part = data[len(data)-amount:]
    
    # Reverse both parts
    left_part.reverse()
    right_part.reverse()
    
    # Concatenate the two reversed parts
    result = left_part + right_part
    
    # Reverse the entire list to get the final result
    result.reverse()
    
    return result



print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
PLAN:
1.Determine the number of elements to be rotated to the right. Since the value of the amount will be in the range of 1 and len(data), 
    I can determine the number of elements to be rotated by calculating len(data) - amount.
    For example, if the length of the list is 9 and the amount is 5, I need to rotate 4 elements to the right (9 - 5 = 4).

2.Slice the list into two parts. The first part will contain the last n elements (where n is the number of elements to be rotated), 
    and the second part will contain the remaining elements.

3.Concatenate the first and second parts of the list in reverse order to obtain the rotated list.

DESCRIPTION:
First, I split the original list into two parts:
    The left part contains everything before the index 'len(data)-amount'. For example, if the original list is '[1, 2, 3, 4, 5, 6, 7, 8, 9]' 
        and I want to rotate it to the right by an amount of '5', then the left part will contain '[1, 2, 3, 4]'.
    The right part contains everything from the index 'len(data)-amount' to the end. In our example, the right part will contain '[5, 6, 7, 8, 9]'.

Next, I reverse both parts. In our example, the left part becomes '[4, 3, 2, 1]' and the right part becomes '[9, 8, 7, 6, 5]'.
I concatenate the two reversed parts to create a new list. In our example, the concatenated list becomes '[4, 3, 2, 1, 9, 8, 7, 6, 5]'.
Finally, I reverse the entire list to get the final result. In our example, the final list is '[5, 6, 7, 8, 9, 1, 2, 3, 4]'.
"""