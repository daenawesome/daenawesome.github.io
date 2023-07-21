import random

# define the themes and the corresponding secret words
themes = {
  "sports": ["soccer", "basketball", "baseball", "tennis", "golf"],
  "music": ["guitar", "piano", "drum", "singer", "song"],
  "movies": ["actor", "director", "producer", "screenplay", "cinema"]
}

while True:
  # prompt the user to choose a theme
  print("\nChoose a theme:")
  for i, theme in enumerate(themes):
    print(f"{i+1}. {theme}")

  choice = input()
  
  # validate the user's input
  if not choice.isdigit() or not (1 <= int(choice) <= len(themes)):
    print("Invalid choice. Please enter a number between 1 and", len(themes))
    continue

  choice = int(choice) - 1
  theme = list(themes.keys())[choice]
  secret_words = themes[theme]

  # choose a secret word at random
  secret_word = random.choice(secret_words)
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
      print("\nYou won! Number of guesses:", len(guesses))
      break

    # update the hint based on the rules in the prompt
    for i in range(len(guess)):
      if guess[i] == secret_word[i]:
        hint[i] = guess[i].upper()
      elif guess[i] in secret_word:
        hint[i] = guess[i]

    # display the hint
    print("Your hint is:", " ".join(hint))
  
  # prompt the user to play again or exit
  play_again = input("Do you want to play again? (y/n) ").lower()
  if play_again != "y":
    break




"""
In this modified code, I have defined a dictionary called themes that 
maps themes to lists of secret words. I have also added a section that 
prompts the user to choose a theme and displays a list of available themes 
to the user.

Once the user has chosen a theme, I use the themes dictionary to retrieve 
the list of secret words for that theme and choose one at random. The rest 
of the code is unchanged and follows the same logic as before.

This way, the user can choose the theme of the game and play with secret 
words related to that theme. This also has input validation on the theme 
and an option to play again or close when won
"""