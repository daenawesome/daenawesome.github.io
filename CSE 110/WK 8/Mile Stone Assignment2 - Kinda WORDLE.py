import random

secret_words = ["mosiah", "temple", "prophet", "scripture", "revelation"] # list of secret words
secret_word = random.choice(secret_words) # choose a secret word at random
guesses = [] # list to store the guesses

# convert the secret word to a list of underscores
hint = ["_" for _ in secret_word]

# display the hint with the number of letters in the secret word
print("Here is your first hint:", " ".join(hint))

# loop until the user guesses the word correctly
while True:
  # prompt the user for a guess
  guess = input("Enter your guess: ").lower()

  # check if the guess is the same length as the secret word
  if len(guess) != len(secret_word):
    print("Your guess must have the same number of letters as the secret word.")
    continue

  # add the guess to the list of guesses
  guesses.append(guess)

  # check if the guess is correct
  if guess == secret_word:
    print("You won! Number of guesses:", len(guesses))
    break

  # update the hint based on the rules in the prompt
  for i in range(len(guess)):
    if guess[i] == secret_word[i]:
      hint[i] = guess[i].upper()
    elif guess[i] in secret_word:
      hint[i] = guess[i]

  # display the hint
  print("Your hint is:", " ".join(hint))


"""
In this modified code, I have defined a list of 'secret_words' 
and used the 'random.choice()' function to choose one at random. 
The rest of the code is unchanged and follows the same logic as before.

This way, the program will choose one of the five secret words 
at random each time it runs, and the user will have to guess it.
"""