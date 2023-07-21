# Program to capitalize every n-th letter in a string

# Step 1: Declare a variable to hold the quote
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

# Step 2: Create a counter variable
counter = 1

# Step 3: Ask the user for a number
n = int(input("Please enter a number: "))

# Step 4: Loop through the quote letter by letter
for letter in quote:
    # Step 5: Check if the current letter is the n-th letter
    if counter % n == 0:
        # Step 6: If it is the n-th letter, print it as a capital letter
        print(letter.upper(), end="")
    else:
        # Step 7: If it is not the n-th letter, print it as a lowercase letter
        print(letter, end="")
    # Step 8: Increment the counter
    counter += 1

# Step 9: Ask the user if they want to enter another number
while True:
    user_response = input("\nWould you like to enter another number? ")
    if user_response.lower() == 'yes':
        # Step 10: If yes, ask for a number again
        n = int(input("Please enter a number: "))
        # Step 11: Create a counter variable
        counter = 1
        # Step 12: Loop through the quote letter by letter
        for letter in quote:
            # Step 13: Check if the current letter is the n-th letter
            if counter % n == 0:
                # Step 14: If it is the n-th letter, print it as a capital letter
                print(letter.upper(), end="")
            else:
                # Step 15: If it is not the n-th letter, print it as a lowercase letter
                print(letter, end="")
            # Step 16: Increment the counter
            counter += 1
    else:
        # Step 17: If no, break out of the loop
        print("Goodbye")
        break

"""
In step 3, the input function is used to prompt the user for a number.
In step 6, 'print(letter.upper(), end="")' is used to capitalize the n-th letter of the quote and 'end=""' is used to print all letters on the same line
In step 7, 'print(letter, end="")' is used to print the letters of the quote on the same line
In step 9, the input function is used to prompt the user if they want to enter another number, and a while loop is used to keep asking until the user types "no"
In step 12, the same steps are repeated to capitalize the n-th letter of the quote
"""