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

# Find the smallest positive number
smallest_positive = float('inf')
for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number

# Compute the sum of the numbers
total = sum(numbers)

# Compute the average of the numbers
average = total / len(numbers)

# Find the maximum number
maximum = max(numbers)

# Sort the numbers
numbers.sort()

# Print the results
print("\nThe sum is:", total)
print("\nThe average is:", average)
print("\nThe largest number is:", maximum)
print("\nThe smallest positive number is:", smallest_positive)
print("\nThe sorted list is:", numbers)


"""
uses a while loop that continues to ask the user for a number until the user types 0. 
Inside the loop, it checks if the number is 0. If the number is not 0, it is added to the list of numbers. 
After the loop, the program uses a for loop to find the smallest positive number, it checks if the current 
number is greater than 0 and less than the current smallest positive number.
Then it uses the 'sort()' method to sort the numbers in the list. Finally, it prints the results.
"""