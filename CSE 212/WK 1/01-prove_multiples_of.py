"""
CSE212 
(c) BYU-Idaho
01-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def multiples_of(number, length):
    """
    This function will produce a list of size 'length' starting
    with 'number' followed by multiples of 'number'.  For 
    example, multiples_of(7, 5) will result in:
    [7, 14, 21, 28, 35].  Assume that length is a positive
    integer greater than 0.  The implementation must be
    done using a list comprehension.
    """
    return [number * i for i in range(1, length+1)]

print(multiples_of(7, 5))    # [7, 14, 21, 28, 35]
print(multiples_of(1.5, 10)) # [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0, 13.5, 15.0]
print(multiples_of(-2, 10))  # [-2, -4, -6, -8, -10, -12, -14, -16, -18, -20]

"""
The function uses the range function to generate a sequence of integers from 1 to length. 
It then multiplies each integer in the sequence by the given number to generate the corresponding multiple, 
and returns the resulting list of multiples.
"""