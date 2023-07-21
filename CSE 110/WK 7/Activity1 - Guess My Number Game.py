import random

# Ask the user for the range of the magic number
print("Welcome to the Guess My Number game!")
print("Enter the range of the magic number:")
min_range = int(input("Minimum value: "))
max_range = int(input("Maximum value: "))

# Generate a random number from the specified range
magic_number = random.randint(min_range, max_range + 1)

# Initialize the number of guesses to 0
num_guesses = 0

# Start a loop to play the game
while True:
  # Get a guess from the user
  guess = int(input("Enter your guess: "))

  # Increment the number of guesses
  num_guesses += 1

  # Check if the guess is correct
  if guess == magic_number:
    print("You guessed it! The magic number was", magic_number)
    print("It took you", num_guesses, "guesses.")
    break
  # If the guess is not correct, give the user a hint and tell them if they need to guess higher or lower
  elif guess < magic_number:
    if magic_number % 2 == 0:
      print("The magic number is even. Guess higher.")
    else:
      print("The magic number is odd. Guess higher.")
  else:
    if magic_number % 2 == 0:
      print("The magic number is even. Guess lower.")
    else:
      print("The magic number is odd. Guess lower.")

# Ask the user if they want to play again
play_again = input("Do you want to play again? (yes/no) ")

if play_again == "yes":
  # If the user wants to play again, start a new game
  magic_number = random.randint(min_range, max_range + 1)
  num_guesses = 0
else:
  # If the user doesn't want to play again, exit the game
  print("Thanks for playing! Goodbye.")


"""
This version allows the user to choose the range of the magic number, 
and it gives the user a hint about the magic number (whether it is odd or even). 
"""