"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

# list slicing approach, efficiently written
def rotate_list_right(data, amount):
    """
    Rotate the 'data' to the right by the 
    'amount'.   For example, if the data is 
    [1, 2, 3, 4, 5, 6, 7, 8, 9] and an amount
    is 5 then the list returned should be 
    [5, 6, 7, 8, 9, 1, 2, 3, 4].  The value 
    of amount will be in the range of 1 and 
    len(data).
    """
    # Save the last 'amount' elements of the list
    rotated_elements = data[-amount:]

    # Remove the last 'amount' elements from the list
    data = data[:-amount]

    # Insert the saved elements at the beginning of the list
    data = rotated_elements + data

    # Return the rotated list
    return data


print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
DESCRIPTION:
This code works by taking the last 'amount' elements of the input list and storing them in a new variable called 'rotated_elements'. 
Then, it removes these elements from the original list using slicing. 
Finally, it adds the 'rotated_elements' variable to the beginning of the original list to create the rotated list, which is then returned.

It saves the last 'amount' elements of the list to a new variable 'rotated_elements'.
It removes the last 'amount' elements from the original list 'data' using slicing and assigns it back to the same variable.
It then inserts the saved elements at the beginning of the list by concatenating the 'rotated_elements' variable with the 'data' variable.
Finally, the function returns the 'data' variable which is the rotated list.
The code then calls the 'rotate_list_right' function three times, each with a different amount parameter, and prints the resulting rotated list.

For example, if the 'rotate_list_right([1,2,3,4,5,6,7,8,9],1)' is called, 
it will save the last element '[9]' of the list and remove it from the original list, 
then concatenate it with the remaining elements in the list 'data', 
resulting in the list '[9, 1, 2, 3, 4, 5, 6, 7, 8]', which is then returned by the function and printed.
"""