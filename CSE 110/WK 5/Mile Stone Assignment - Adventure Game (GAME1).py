# Game reset option
def play_again():
    again = input("\nWould you like to play again? (YES or NO): ")
    if again.lower() == "yes":
        lost_treasure()
    elif again.lower() == "no":
        print("\nThank you for playing!")
        return
    else:
        print("Invalid choice. Please enter either 'yes' or 'no'.")
        play_again()

# Greeting Message
print("Welcome to the Text-Based Adventure Game!")

#Game
def lost_treasure():
  # Level 1 (A/B)
  print("You are an adventurer on a quest to find the lost treasure that you will never find. \n\nYou come across a fork in the road and see a sign that reads:")
  print("LEFT PATH: leads to the dark forest")
  print("RIGHT PATH: leads to the abandoned mine")
  choice1 = input("Which path do you take? LEFT or RIGHT? ").lower()

  # Level 1 (A) => Level 2 (A/B)
  if choice1 == "left":
    print("\nYou follow the path and enter the dark forest. You see a clearing up ahead and notice a faint light. As you approach, you see that it's a campfire. Do you:")
    print("APPROACH: the campfire and see if anyone is there")
    print("TURN BACK: and return the way you came")
    choice2 = input("What do you do? APPROACH or TURN BACK? ").lower()

    # Level 2 (A) => Level 3 (A/B/C)
    if choice2 == "approach":
      print("\nAs you get closer to the campfire, you see that there are a group of bandits huddled around it. \nThey notice you and one of them stands up and approaches you with a menacing look in his eyes. Do you:")
      print("RUN: back the way you came")
      print("FIGHT: the bandits with your sword")
      print("SURRENDER: and hope for mercy")
      choice3 = input("What do you do? RUN, FIGHT, or SURRENDER? ").lower()

      # Level 3 (A)
      if choice3 == "run":
        print("\nYou turn and flee back the way you came. The bandits let out a chorus of jeers and insults as you go, but they do not follow. \nYou escape unharmed, but you must abandon your quest for the lost treasure.")
        play_again()
      # Level 3 (B)
      elif choice3 == "fight":
        print("\nYou unsheath your sword and prepare to do battle. The bandits draw their own weapons and the fight begins. \nAfter a long and grueling battle, you emerge victorious. However, you are badly injured and decide to return home and recover before continuing your quest for the lost treasure.")
        play_again()
      # Level 3 (C)
      elif choice3 == "surrender":
        print("\nYou throw down your weapon and raise your hands in surrender. The bandits take your sword and supplies, but spare your life. \nYou are left with nothing and must return home empty-handed.")
        play_again()
      else:
        print("\nInvalid choice. You stand there indecisively and the bandits grow impatient. They attack and you are unprepared. You are killed and your quest for the lost treasure ends in failure.")
        play_again()

    # Level 2 (B)
    elif choice2 == "turn back":
      print("\nYou decide that the campfire and its occupants are best left alone and turn back the way you came. \nYou return home empty-handed, but at least you are alive to try again another day.")
      play_again()
    else:
      print("\nInvalid choice. You stand there indecisively and a group of goblins sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
      play_again()

  # Level 1 (B) => Level 2 (A/B)
  elif choice1 == "right":
    print("\nYou follow the path and enter the abandoned mine. You see a tunnel up ahead and hear the sound of running water. Do you:")
    print("FOLLOW: the sound of the water")
    print("INVESTIGATE: a nearby room")
    choice2 = input("What do you do? FOLLOW or INVESTIGATE? ").lower()

    # Level 2 (A) => Level 3 (A/B)
    if choice2 == "follow":
      print("\nYou follow the sound of the water and come across a underground river. Do you:")
      print("CROSS: the river using a nearby log")
      print("SEARCH: for another way across")
      choice3 = input("What do you do? CROSS or SEARCH? ").lower()

      # Level 3 (A)
      if choice3 == "cross":
        print("\nYou carefully make your way across the log, trying not to lose your balance. Halfway across, the log begins to roll and you fall into the river. \nYou manage to swim to the shore, but you lose your map and compass in the process. You must retrace your steps and try to find your way back to the entrance of the mine.")
        play_again()
      # Level 3 (B) => Level 4 (A/B)
      elif choice3 == "search":
        print("\nYou search for another way across the river and come across a rickety old bridge. Do you:")
        print("CROSS: the bridge")
        print("RETURN: the way you came")
        choice4 = input("What do you do? CROSS or RETURN? ").lower()

        # Level 4 (A)
        if choice4 == "cross":
          print("\nYou tentatively step onto the bridge and make your way across. The bridge holds and you reach the other side safely. \nYou continue on your quest for the lost treasure.")
          play_again()
        # Level 4 (B) => Level 5 (A/B)
        elif choice4 == "return":
          print("\nYou have returned home and are feeling defeated. Do you:")
          print("GIVE UP: on your quest for the lost treasure")
          print("TRY AGAIN: and set out on a new quest")
          choice5 = input("What do you do? GIVE UP or TRY AGAIN? ").lower()

          # Level 5 (A)
          if choice5 == "give up":
            print("\nYou hang up your adventuring hat and live the rest of your life in peace and comfort. \nHowever, you always wonder what could have been if you had just persevered a little longer.")
            play_again()
          # Level 5 (B)
          elif choice5 == "try again":
            print("\nYou brush yourself off and prepare for another journey. You are determined to find the lost treasure and will not let any obstacle stand in your way. \nGood luck on your new quest!")
            play_again()
          else:
            print("\nInvalid choice. You stand there indecisively and a group of dragons sneak up on you and attack. \nYou are killed and your quest for the lost treasure ends in failure.")
            play_again()

        else:
          print("\nInvalid choice. You stand there indecisively and a group of trolls sneak up on you and attack. \nYou are killed and your quest for the lost treasure ends in failure.")
          play_again()

      else:
        print("\nInvalid choice. You stand there indecisively and a group of kobolds sneak up on you and attack. \nYou are killed and your quest for the lost treasure ends in failure.")
        play_again()

    # Level 2 (B) => Level 3 (A/B)
    elif choice2 == "investigate":
      print("\nYou enter the nearby room and see that it is filled with old mining equipment. Do you:")
      print("SEARCH: the room for anything useful")
      print("LEAVE: the room and continue on your way")
      choice3 = input("What do you do? SEARCH or LEAVE? ").lower()

      # Level 3 (A)
      if choice3 == "search":
        print("\nYou search the room and find a pickaxe and a lantern. You add these to your supplies and continue on your quest for the lost treasure.")
        play_again()      
      # Level 3 (B)
      elif choice3 == "leave":
        print("You decide that the room is not worth your time and leave to continue on your quest. You come across a dead end and are forced to turn back. You return home empty-handed, but at least you are alive to try again another day.")
        play_again()
      else:
        print("\nInvalid choice. You stand there indecisively and a group of giant spiders sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
        play_again()
  else:
    print ("\nYou forgot you can't read, you fell of a cliff not knowing where to go :(")
    play_again()
  
lost_treasure()

"""
The program starts by printing a welcome message and then calls the ‘lost_treasure’ function to start the game.
I made 2 functions 'lost_treasure' and 'play_again' that can be easily called when handling game resets.
The ‘lost_treasure’ function represents the main gameplay with at least 3 to four lelvels, where the player is asked to make a series of choices. The game provides different responses based on the player's choices. The game is played in a tree structure, with the first choice leading to two possible branches, then each of those branches leading to another set of choices, and so on.
The ‘play_again’ function is called after the game ends, and it asks the player if they would like to play again. If the player inputs "yes", the game restarts from the beginning by calling the ‘lost_treasure’ function. If the player inputs "no", the game thanks the player and terminates. If the player inputs anything other than "yes" or "no", the game informs the player that the input is invalid and repeats the ‘play_again’ function.
Used a method '.lower()' to convert all user inputs to lowercase to match case sensitivity on the program so we can compare them regardless of their original capitalization. Also used different variables to easily understand and match the right response based on the user's chosen input.

‘==’ for comparison operator

"""