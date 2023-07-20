"""
PLAN:
Initialize an empty list result to store the result of the combination of list1 and list2.
Use a for loop to iterate through the selector list.
If the value of the selector list is 1, then append the next value from list1 to the result list using the pop() method to remove the value from the list.
If the value of the selector list is 2, then append the next value from list2 to the result list using the pop() method to remove the value from the list.
Return the result list.
"""

def list_selector(list1, list2, selector):
    # Initialize an empty list to hold the output
    output = []

    # Iterate through the selector list
    for sel in selector:
        # If the selector value is 1, add the next value from list1 to the output
        if sel == 1:
            output.append(list1.pop(0))
        # If the selector value is 2, add the next value from list2 to the output
        elif sel == 2:
            output.append(list2.pop(0))

    # Add any remaining values from list1 to the output
    output.extend(list1)
    # Add any remaining values from list2 to the output
    output.extend(list2)

    # Return the output list
    return output

l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
select = [1, 1, 1, 2, 2, 1, 2, 2, 2, 1]
print(list_selector(l1, l2, select))  # [1, 2, 3, 2, 4, 4, 6, 8, 10, 5]

l1 = ['A', 'A', 'A', 'A', 'A']
l2 = ['B', 'B', 'B', 'B', 'B']
select = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(list_selector(l1, l2, select))  # ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', ]