# approach that uses a for loop and modulo operator
def rotate_list_right(data, amount):

    rotated_list = []
    
    # Loop through each item in the list using enumerate to get the index
    for i, item in enumerate(data):
        
        # Calculate the new index by subtracting the rotation amount and taking the modulus
        new_index = (i - amount) % len(data)
        
        # Add the item at the new index to the rotated list
        rotated_list.append(data[new_index])
    
    return rotated_list

print(rotate_list_right([1,2,3,4,5,6,7,8,9],1)) # [9, 1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],5)) # [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(rotate_list_right([1,2,3,4,5,6,7,8,9],9)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
DESCRIPTION:
Initialize an empty list called rotated_list to store the rotated elements.
Loop through each item in the input data list using the enumerate function to get both the item and its index in the list.
Calculate the new index for the current item by subtracting the amount of rotation from its index, 
    and then taking the modulus of the length of the data list to ensure that the index is within the range of the list.
Append the item at the new index to the rotated_list.
Once all items have been looped through and added to the rotated_list, return the list as the final result.
The print statements at the end of the code show how the function works with different amount values.


EXAMPLE:
input list: [1,2,3,4,5,6,7,8,9]
amount: 1

The rotated_list is initialized as an empty list.
The loop starts with the first item in the data list, which is 1.
The new index for 1 is (0 - 1) % 9, which is 8. So, the item at index 8 in the data list, which is 9, is added to the rotated_list.
The loop continues with the second item in the data list, which is 2.
The new index for 2 is (1 - 1) % 9, which is 0. So, the item at index 0 in the data list, which is 1, is added to the rotated_list.
The loop continues until all items in the data list have been looped through and added to the rotated_list.
The final rotated_list is [9, 1, 2, 3, 4, 5, 6, 7, 8], which is the input list rotated by one element to the right.
"""