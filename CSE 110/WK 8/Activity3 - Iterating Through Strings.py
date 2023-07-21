# Program to manipulate every n-th letter in a string using enumerate

# Step 1: Ask the user for a word or phrase
word_or_phrase = input("Please enter a word or phrase: ")

# Step 2: Ask the user for a number
while True:
    try:
        n = int(input("Please enter a number: "))
        if n<=0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive number.")

# Step 3: Ask the user for the type of manipulation they want to perform
print("Select the type of manipulation you want to perform: ")
print("1. Capitalize every n-th letter")
print("2. Lowercase every n-th letter")
print("3. Hide every n-th letter with an underscore")
manipulation_type = int(input())

# Step 4: Loop through the word or phrase using enumerate
for i, letter in enumerate(word_or_phrase):
    # Step 5: Check if the current index is a multiple of the user's number
    if (i+1) % n == 0:
        # Step 6: If it is, perform the selected manipulation
        if manipulation_type == 1:
            print(letter.upper(), end="")
        elif manipulation_type == 2:
            print(letter.lower(), end="")
        elif manipulation_type == 3:
            print("_", end="")
    else:
        # Step 7: If it is not, print the letter as is
        print(letter, end="")

# Step 8: Ask the user if they want to enter another number
while True:
    user_response = input("\nWould you like to enter another number? (yes or no) ")
    if user_response.lower() == 'yes':
        # Step 9: Ask the user for a word or phrase again
        word_or_phrase = input("\nPlease enter a word or phrase: ")
        # Step 10: Ask the user for a number again
        n = int(input("Please enter a number: "))
        # Step 11: Ask the user for the type of manipulation they want to perform
        while True:
            try:
                manipulation_type = int(input("Select the type of manipulation you want to perform: \n1. Capitalize every n-th letter \n2. Lowercase every n-th letter\n3. Hide every n-th letter with an underscore\n"))
                if manipulation_type not in [1,2,3]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please select a valid option.")
        # Step 12: Loop through the word or phrase using enumerate
        for i, letter in enumerate(word_or_phrase):
            # Step 13: Check if the current index is a multiple of the user's number
            if (i+1) % n == 0:
                # Step 14: If it is, perform the selected manipulation
                if manipulation_type == 1:
                    print(letter.upper(), end="")
                elif manipulation_type == 2:
                    print(letter.lower(), end="")
                elif manipulation_type == 3:
                    print("_", end="")
            else:
                # Step 15: If it is not, print the letter as is
                print(letter, end="")
    else:
        # Step 16: If no, break out of the loop
        print("Goodbye")
        break


"""
Added: 
1.Instead of only capitalizing the n-th letter in the string, the program now allows the user to select the type of manipulation they want to perform: capitalizing every n-th letter, lowercasing every n-th letter, or hiding every n-th letter with an underscore.
2.The program now allows the user to enter a word or phrase, rather than using a pre-programmed string.
3.Some input validation if the input provided by the user is a positive number and it's one of the valid options, otherwise it will prompt an error message and ask the user again to provide the input.

Summary:
This allows the user to enter a word or phrase, a number, and a type of manipulation to perform. 
It then loops through the letters of the word or phrase, and it will manipulate every n-th letter, 
depending on the user's input. The user can choose between capitalizing, lowercasing, or hiding with 
an underscore every n-th letter. Once the program finishes going through all the letters, it will 
ask the user if they want to repeat the process again and it will finish when the user inputs "no". 
It includes input validation and error message handling for invalid input.
"""