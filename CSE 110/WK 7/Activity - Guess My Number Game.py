import random

# Generate a random number from 1 to 100
magic_number = random.randint(1, 101)

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
  # If the guess is not correct, tell the user if they need to guess higher or lower
  elif guess < magic_number:
    print("Guess higher.")
  else:
    print("Guess lower.")

# Ask the user if they want to play again
play_again = input("Do you want to play again? (yes/no) ")

if play_again == "yes":
  # If the user wants to play again, start a new game
  magic_number = random.randint(1, 101)
  num_guesses = 0
else:
  # If the user doesn't want to play again, exit the game
  print("Thanks for playing! Goodbye.")
