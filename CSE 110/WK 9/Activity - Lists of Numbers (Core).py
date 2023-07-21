# Create an empty list to store the numbers
numbers = []

# Ask the user for a number
while True:
    number = int(input("Enter a number, type 0 when finished: "))
    # Check if the number is 0
    if number == 0:
        break
    # If the number is not 0, add it to the list of numbers
    numbers.append(number)

# Compute the sum of the numbers
total = sum(numbers)

# Compute the average of the numbers
average = total / len(numbers)

# Find the maximum number
maximum = max(numbers)

# Print the results
print("\nThe sum is:", total)
print("\nThe average is:", average)
print("\nThe largest number is:", maximum)


"""
a while loop that continues to ask the user for a number until the user types 0. 
Inside the loop, it checks if the number is 0. If the number is not 0, it is added 
to the list of numbers. After the loop, the program uses the 'sum()' method to compute 
the sum of the numbers, the 'len()' method to compute the average of the numbers, 
and the 'max()' method to find the maximum number in the list, and print the results.
"""