# Secret word
secret_word = "secret"

# Initial hint
hint = ["_" for _ in secret_word]

# Number of guesses
guesses = 0

# Game loop
while True:
  # Get guess from user
  guess = input("Enter your guess: ").lower()
  
  # Check if the length of the guess is the same as the length of the secret word
  if len(guess) != len(secret_word):
    print("Your guess must have the same number of letters as the secret word!")
    continue
  
  # Increment number of guesses
  guesses += 1
  
  # Check if the guess is correct
  if guess == secret_word:
    print("You won!")
    print(f"Number of guesses: {guesses}")
    break
  
  # Update hint
  for i in range(len(secret_word)):
    if secret_word[i] == guess[i]:
      hint[i] = guess[i].upper()
    elif guess[i] in secret_word:
      hint[i] = guess[i]
  
  # Print hint
  print("Hint: ", "".join(hint))
