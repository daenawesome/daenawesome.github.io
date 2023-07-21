secret_word = "mosiah" # the secret word
guesses = [] # list to store the guesses

# convert the secret word to a list of underscores
hint = ["_" for _ in secret_word]

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
This code defines the 'secret_word' and initializes an empty list called 'guesses' to
store the guesses made by the user. It then converts the secret word to a list of
underscores and assigns it to the 'hint' variable. The code then enters a loop that
prompts the user for a guess, checks if the guess is the same length as the secret 
word, and adds the guess to the list of guesses. If the guess is correct, it displays 
a message and breaks out of the loop.

If the guess is not correct, the code updates the 'hint' based on the rules like using 
uppercase for exact matches and lowercase for partial matches and displays the hint to 
the user. The loop then continues, prompting the user for another guess.
"""