# Create an empty list to store the numbers
numbers = []

# Ask the user for a number
while True:
    try:
        number = int(input("Enter a number, type 0 when finished: "))
        if number == 0:
            break
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

sort_order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")
if sort_order == "asc":
    numbers.sort()
elif sort_order == "desc":
    numbers.sort(reverse=True)
else:
    print("Invalid input. Defaulting to ascending order.")
    numbers.sort()

# Compute the sum of the numbers
total = sum(numbers)

# Compute the average of the numbers
average = total / len(numbers)

# Find the maximum number
maximum = max(numbers)

# Find the smallest positive number
smallest_positive = float('inf')
for number in numbers:
    if number > 0 and number < smallest_positive:
        smallest_positive = number

# Print the results
print("\nThe sum is:", total)
print("\nThe average is:", average)
print("\nThe largest number is:", maximum)
print("\nThe smallest positive number is:", smallest_positive)
print("\nThe sorted list is:", numbers)


"""
I have added input validation using try-except block to ensure that the user enters only valid numbers. 
Also, I have added feature to allow the user to specify if they want the numbers sorted in ascending or descending order, if the user enters invalid input for the sort order, the program defaults to ascending order. 
And added error message handling for invalid input, it will print an error message "Invalid input. Please enter a valid number." if the user enters an invalid input.
"""