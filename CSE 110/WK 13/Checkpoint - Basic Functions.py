# Function to display a string as is
def display_regular(string):
    print(string)

# Function to display a string in uppercase
def display_uppercase(string):
    print(string.upper())

# Function to display a string in lowercase
def display_lowercase(string):
    print(string.lower())

# Ask the user to input a message
message = input("What is your message? ")

# Call each of the three functions with the user's message
display_regular(message)
display_uppercase(message)
display_lowercase(message)
