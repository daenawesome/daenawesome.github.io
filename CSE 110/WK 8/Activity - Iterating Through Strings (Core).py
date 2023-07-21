# Program to loop through a word and display letters based on user input

# Step 1: Declare a variable to hold the word
word = "Commitment"

# Step 2: Ask the user for their favorite letter
favorite_letter = input("What is your favorite letter? ")

# Step 3: Loop through the word letter by letter
for letter in word:
    # Step 4: Check if the letter is the user's favorite letter
    if letter.lower() == favorite_letter.lower():
        # Step 5: If the letter is the user's favorite, hide it with an underscore
        print("_", end="")
    else:
        # Step 6: If the letter is not the user's favorite, print it as is
        print(letter, end="")


"""
In step 2, the input function is used to prompt the user for their favorite letter.
In step 5, 'print("_", end="")' is used to hide the user's favorite letter with an underscore and 'end=""' is used to print all letters on the same line
In step 6, 'print(letter, end="")' is used to print the letters of the word on the same line
In step 4, 'letter.lower() == favorite_letter.lower()' is used to make the program case-insensitive.
"""