# Program to capitalize every n-th letter in a string using enumerate

# Step 1: Declare a variable to hold the quote
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

# Step 2: Ask the user for a number
n = int(input("Please enter a number: "))

# Step 3: Loop through the quote using enumerate
for i, letter in enumerate(quote):
    # Step 4: Check if the current index is a multiple of the user's number
    if (i+1) % n == 0:
        # Step 5: If it is, print the letter as a capital letter
        print(letter.upper(), end="")
    else:
        # Step 6: If it is not, print the letter as a lowercase letter
        print(letter, end="")
        
# Step 7: Ask the user if they want to enter another number
while True:
    user_response = input("\nWould you like to enter another number? ")
    if user_response.lower() == 'yes':
        # Step 8: If yes, ask for a number again
        n = int(input("Please enter a number: "))
        # Step 9: Loop through the quote using enumerate
        for i, letter in enumerate(quote):
            # Step 10: Check if the current index is a multiple of the user's number
            if (i+1) % n == 0:
                # Step 11: If it is, print the letter as a capital letter
                print(letter.upper(), end="")
            else:
                # Step 12: If it is not, print the letter as a lowercase letter
                print(letter, end="")
    else:
        # Step 13: If no, break out of the loop
        print("Goodbye")
        break
    
"""
the 'enumerate' function is used to loop through the string, providing both the index of the current letter and the letter itself.
In step 4, '(i+1) % n == 0' is used to check if the current index is a multiple of the user's number
In step 5, 'print(letter.upper(), end="")' is used to capitalize the n-th letter of the quote and 'end=""' is used to print all letters on the same line
In step 6, 'print(letter, end="")' is used to print the letters of the quote on the same line
In step 7, the input function is used to prompt the user if they want to enter another number, and a while loop is used to keep asking until the user types "no"
In step 9, the same steps are repeated to capitalize the n-th letter of the quote using the 'enumerate' function.
"""