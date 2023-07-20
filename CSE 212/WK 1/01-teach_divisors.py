"""
CSE212 
(c) BYU-Idaho
01-Teach - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

def find_divisors_1(number):
    """
    Create a list of all divisors for a number including 1
    and excluding the number itself. Modulo will be used
    to test divisibility.
    """
    # using a for loop and an if statement
    divisors = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    return divisors


def find_divisors_2(number):
    """
    Same as find_divisors_1 but a list comprehension is used.
    """
    # using a list comprehension
    return [i for i in range(1, number) if number % i == 0]


print(find_divisors_1(80)) # [1, 2, 4, 5, 8, 10, 16, 20, 40]
print(find_divisors_2(80)) # [1, 2, 4, 5, 8, 10, 16, 20, 40]
print(find_divisors_1(79)) # [1] ... This is prime
print(find_divisors_2(79)) # [1]

"""
This code defines two functions, 'find_divisors_1' and 'find_divisors_2', 
    that both take a positive integer 'number' as input and return a 
    list of all its divisors (excluding the number itself but including 1).

The first function, 'find_divisors_1', uses a for loop to iterate over all 
    numbers in the range 2 to 'number - 1'. It checks whether number is divisible 
    by each of these 'numbers' by using the modulo operator '%'. If the result is 0, 
    then the number is a divisor of 'number' and it is added to the divisors list. 
    The function returns the 'divisors' list at the end.

The second function, 'find_divisors_2', achieves the same thing as the first function 
    but uses a list comprehension instead of a for loop. The comprehension iterates 
    over the range 1 to 'number - 1' and checks whether 'number' is divisible by each 
    number using the same '%' operator. It then creates a list of all such numbers 
    that are divisors of 'number' and returns it.

The functions are called with two examples - 'find_divisors_1(80)' and 'find_divisors_2(80)' - 
    and both return the list '[1, 2, 4, 5, 8, 10, 16, 20, 40]', which are all the divisors of 80 (excluding 80 itself). 
    The functions are also called with the prime number 79, and both return the list '[1]', since 79 only has one 
    divisor besides itself, which is 1.
"""

"""
     +------------------------------------------------------+
     |               find_divisors_1(number)                 |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |     Create an empty list called "divisors" and add 1  |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |      Loop through the range (2, number) and check if  |
     |        the number is divisible by the current value   |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |   If the number is divisible, add the current value   |
     |                 to the "divisors" list                  |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |             Return the "divisors" list                 |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |               find_divisors_2(number)                 |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     | Create a list comprehension to generate a list of all |
     |       divisors for a number including 1 and            |
     | excluding the number itself, using modulo to test     |
     |                 divisibility                          |
     +------------------------------------------------------+
                                    |
                                    v
     +------------------------------------------------------+
     |             Return the list of divisors                |
     +------------------------------------------------------+
"""