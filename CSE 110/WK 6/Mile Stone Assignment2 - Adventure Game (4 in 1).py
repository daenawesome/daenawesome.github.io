def play_again():
    again = input("Would you like to play again? (yes/no): ")
    if again.lower() == "yes":
        if game_choice == "1":
            lost_treasure()
        elif game_choice == "2":
            into_the_woods()
    elif again.lower() == "no":
        print("Thank you for playing!")
        return
    else:
        print("Invalid choice. Please enter either 'yes' or 'no'.")
        play_again()




# GAME 1
def lost_treasure():

  # Level 1 (A/B)
  print("\nYou are an adventurer on a quest to find the lost treasure that you will never find. \n\nYou come across a fork in the road and see a sign that reads:")
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
      print("\nAs you get closer to the campfire, you see that there are a group of bandits huddled around it. They notice you and one of them stands up and approaches you with a menacing look in his eyes. Do you:")
      print("RUN: back the way you came")
      print("FIGHT: the bandits with your sword")
      print("SURRENDER: and hope for mercy")
      choice3 = input("What do you do? RUN, FIGHT, or SURRENDER? ").lower()
      # Level 3 (A)
      if choice3 == "run":
        print("\nYou turn and flee back the way you came. The bandits let out a chorus of jeers and insults as you go, but they do not follow. You escape unharmed, but you must abandon your quest for the lost treasure.")
      # Level 3 (B)
      elif choice3 == "fight":
        print("\nYou unsheath your sword and prepare to do battle. The bandits draw their own weapons and the fight begins. After a long and grueling battle, you emerge victorious. However, you are badly injured and decide to return home and recover before continuing your quest for the lost treasure.")
      # Level 3 (C)
      elif choice3 == "surrender":
        print("\nYou throw down your weapon and raise your hands in surrender. The bandits take your sword and supplies, but spare your life. You are left with nothing and must return home empty-handed.")
      else:
        print("\nInvalid choice. You stand there indecisively and the bandits grow impatient. They attack and you are unprepared. You are killed and your quest for the lost treasure ends in failure.")
    # Level 2 (B)
    elif choice2 == "turn back":
      print("\nYou decide that the campfire and its occupants are best left alone and turn back the way you came. You return home empty-handed, but at least you are alive to try again another day.")
    else:
      print("\nInvalid choice. You stand there indecisively and a group of goblins sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
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
        print("\nYou carefully make your way across the log, trying not to lose your balance. Halfway across, the log begins to roll and you fall into the river. You manage to swim to the shore, but you lose your map and compass in the process. You must retrace your steps and try to find your way back to the entrance of the mine.")
      # Level 3 (B) => Level 4 (A/B)
      elif choice3 == "search":
        print("\nYou search for another way across the river and come across a rickety old bridge. Do you:")
        print("CROSS: the bridge")
        print("RETURN: the way you came")
        choice4 = input("What do you do? CROSS or RETURN? ").lower()
        # Level 4 (A)
        if choice4 == "cross":
          print("\nYou tentatively step onto the bridge and make your way across. The bridge holds and you reach the other side safely. You continue on your quest for the lost treasure.")
        # Level 4 (B) => Level 5 (A/B)
        elif choice4 == "return":
          print("\nYou have returned home and are feeling defeated. Do you:")
          print("GIVE UP: on your quest for the lost treasure")
          print("TRY AGAIN: and set out on a new quest")
          choice5 = input("What do you do? GIVE UP or TRY AGAIN? ").lower()
          # Level 5 (A)
          if choice4 == "give up":
            print("\nYou hang up your adventuring hat and live the rest of your life in peace and comfort. However, you always wonder what could have been if you had just persevered a little longer.")
          # Level 5 (B)
          elif choice4 == "try again":
            print("\nYou brush yourself off and prepare for another journey. You are determined to find the lost treasure and will not let any obstacle stand in your way. Good luck on your new quest!")
          else:
            print("\nInvalid choice. You stand there indecisively and a group of dragons sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
        else:
          print("\nInvalid choice. You stand there indecisively and a group of trolls sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
      else:
        print("\nInvalid choice. You stand there indecisively and a group of kobolds sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
    # Level 2 (B) => Level 3 (A/B)
    elif choice2 == "investigate":
      print("\nYou enter the nearby room and see that it is filled with old mining equipment. Do you:")
      print("SEARCH: the room for anything useful")
      print("LEAVE: the room and continue on your way")
      choice3 = input("What do you do? SEARCH or LEAVE? ").lower()
      # Level 3 (A)
      if choice3 == "search":
        print("\nYou search the room and find a pickaxe and a lantern. You add these to your supplies and continue on your quest for the lost treasure.")
      # Level 3 (B)
      elif choice3 == "leave":
        print("You decide that the room is not worth your time and leave to continue on your quest. You come across a dead end and are forced to turn back. You return home empty-handed, but at least you are alive to try again another day.")
      else:
        print("\nInvalid choice. You stand there indecisively and a group of giant spiders sneak up on you and attack. You are killed and your quest for the lost treasure ends in failure.")
  else:
    print ("\nYou forgot you can't read, you fell of a cliff not knowing where to go :(")
    play_again()
      
###########################################################################################################################################################
  
#GAME 2
def into_the_woods():

  # First level
  print("\nYou are on a journey through a dark forest. You come to a fork in the road and see a sign that reads:")
  print("LEFT PATH: leads to a haunted house")
  print("RIGHT PATH: leads to a river")

  choice = input("Which path do you take? LEFT or RIGHT? ")
  if choice.lower() == "left":
    print("You decide to take the left path and come across a haunted house. The door creaks open and you see two figures inside: a ghost and a witch. Who do you approach?")
    print("GHOST or WITCH?")
    choice = input("What do you do? ")
    if choice.lower() == "ghost":
      print("The ghost takes you on a tour of the haunted house and tells you stories about its history. You learn a lot about the house and the ghost thanks you for listening to its stories.")
    elif choice.lower() == "witch":
      print("The witch cackles and offers you a potion. Do you DRINK the potion or REFUSE?")
      choice = input("What do you do? ")
      if choice.lower() == "drink":
        print("The potion was poison and you fall to the ground, never to wake up again.")
      elif choice.lower() == "refuse":
        print("The witch gets angry and casts a spell on you, turning you into a frog. You hop away and spend the rest of your days as a frog in the haunted house.")
    else:
      print("Invalid choice. You are stuck in the haunted house forever.")
  elif choice.lower() == "right":
    print("You take the right path and come across a river. The water is rushing and there is no bridge in sight. Do you TRY to swim across or LOOK for another way?")
    choice = input("What do you do? ")
    if choice.lower() == "try":
      print("You brave the currents and make it to the other side of the river. You continue on your journey, feeling proud of your bravery.")
    elif choice.lower() == "look":
      print("You search for another way and find a small boat tied to a tree. Do you STEAL the boat or LEAVE it alone?")
      choice = input("What do you do? ")
      if choice.lower() == "steal":
        print("You steal the boat and use it to cross the river. However, the boat's owner, a powerful sorceress, curses you for stealing her boat. You are doomed to wander the earth, unable to die, until you make amends with the sorceress.")
      elif choice.lower() == "leave":
        print("You decide to leave the boat alone and continue your journey on foot. You come across a village and are able to rest and replenish your supplies before continuing on your journey.")
    else:
      print("Invalid choice. You fall into the river and drown.")
  else:
    print("Invalid choice. You are lost in the forest forever.")

  # Second level
  print("As you continue your journey, you come across a fork in the road again. This time, the sign reads:")
  print("LEFT PATH: leads to a mountain")
  print("RIGHT PATH: leads to a dense jungle")

  choice = input("Which path do you take? LEFT or RIGHT? ")
  if choice.lower() == "left":
    print("You decide to take the left path and come across a mountain. It is a steep climb and you are tired, but you are determined to reach the top. Do you REST and regain your energy or PRESS ON?")
    choice = input("What do you do? ")
    if choice.lower() == "rest":
      print("You rest for a while and regain your energy. You continue the climb and reach the top of the mountain, where you are rewarded with a breathtaking view.")
    elif choice.lower() == "press on":
      print("You push yourself to the limit and make it to the top of the mountain, but you are too exhausted to enjoy the view. You collapse and are unable to continue your journey.")
    else:
      print("Invalid choice. You slip and fall off the mountain, plummeting to your death.")
  elif choice.lower() == "right":
    print("You take the right path and come across a dense jungle. You see two paths ahead: one that goes deeper into the jungle and one that leads to a clearing. Which path do you take?")
    print("DEEPER or CLEARING?")
    choice = input("What do you do? ")
    if choice.lower() == "deeper":
      print("You venture deeper into the jungle and come across a tribe of friendly natives. They welcome you and teach you about their way of life. You learn a lot from them and continue your journey with new knowledge and skills.")
    elif choice.lower() == "clearing":
      print("You take the path to the clearing and come across a beautiful waterfall. Do you STOP and rest or KEEP GOING?")
      choice = input("What do you do? ")
      if choice.lower() == "stop":
        print("You decide to rest and take in the beauty of the waterfall. You refill your water bottle and continue your journey refreshed and rejuvenated.")
      elif choice.lower() == "keep going":
        print("You decide to keep going and come across a pack of hungry wolves. You are forced to defend yourself and are severely injured in the process. You are unable to continue your journey and are forced to turn back.")
    else:
      print("Invalid choice. You get lost in the jungle and are never seen again.")
  else:
    print("Invalid choice. You are lost in the wilderness forever.")

  # Third level
  print("As you continue your journey, you come across a fork in the road once again. This time, the sign reads:")
  print("LEFT PATH: leads to a dark cave")
  print("RIGHT PATH: leads to a sunny meadow")

  choice = input("Which path do you take? LEFT or RIGHT? ")
  if choice.lower() == "left":
    print("You decide to take the left path and come across a dark cave. You see a faint light in the distance and decide to investigate. Do you FOLLOW the light or TURN BACK?")
    choice = input("What do you do? ")
    if choice.lower() == "follow":
      print("You follow the light and come across a treasure chest. Do you OPEN the chest or LEAVE it alone?")
      choice = input("What do you do? ")
      if choice.lower() == "open":
        print("You open the chest and find a map leading to a hidden treasure. You follow the map and find the treasure, becoming rich beyond your wildest dreams. You continue your journey, feeling grateful and fortunate.")
      elif choice.lower() == "leave":
        print("You decide to leave the chest alone and continue your journey. As you walk away, you hear a loud noise behind you and turn to see the chest explode, revealing that it was actually a trap set by a group of thieves. You narrowly escape with your life and continue your journey, shaken but grateful to be alive.")
    elif choice.lower() == "turn back":
      print("You decide to turn back and continue your journey. As you walk away, you hear a loud noise behind you and turn to see the cave collapse, trapping whoever was inside. You continue your journey, feeling grateful to have made the right choice.")
    else:
      print("Invalid choice. You are stuck in the cave forever.")
  elif choice.lower() == "right":
    print("You take the right path and come across a sunny meadow. You see a small cottage in the distance and decide to investigate. Do you KNOCK on the door or WALK away?")
    choice = input("What do you do? ")
    if choice.lower() == "knock":
      print("You knock on the door and an old man answers. He invites you in and offers you a meal and a place to rest. You accept his hospitality and spend a pleasant evening chatting with him. You continue your journey feeling grateful and refreshed.")
    elif choice.lower() == "walk away":
      print("You decide to walk away and continue your journey. As you walk, you feel a sharp pain in your leg and realize you have been bitten by a venomous snake. You struggle to make it to the nearest town and receive treatment, but the venom has already spread through your body. You spend the rest of your days bedridden, regretting your decision to walk away from the cottage.")
    else:
      print("Invalid choice. You are attacked by a swarm of bees and die.")
  else:
    print("Invalid choice. You are lost in the wilderness forever.")

  # Fourth level
  print("As you continue your journey, you come across a fork in the road yet again. This time, the sign reads:")
  print("LEFT PATH: leads to a vast desert")
  print("RIGHT PATH: leads to a snowy tundra")

  choice = input("Which path do you take? LEFT or RIGHT? ")
  if choice.lower() == "left":
    print("You decide to take the left path and come across a vast desert. You see a mirage in the distance and decide to investigate. Do you FOLLOW the mirage or IGNORE it?")
    choice = input("What do you do? ")
    if choice.lower() == "follow":
      print("You follow the mirage and come across a oasis. Do you DRINK the water or LEAVE it alone?")
      choice = input("What do you do? ")
      if choice.lower() == "drink":
        print("You drink the water and feel rejuvenated. You continue your journey, feeling grateful to have found such a wonderful source of hydration.")
      elif choice.lower() == "leave":
        print("You decide to leave the water alone and continue your journey. As you walk away, you feel a sharp pain in your stomach and realize the water was actually poisoned. You struggle to make it to the nearest town and receive treatment, but the poison has already spread through your body. You spend the rest of your days bedridden, regretting your decision to leave the oasis.")
    elif choice.lower() == "ignore":
      print("You decide to ignore the mirage and continue your journey. As you walk away, you hear a loud noise behind you and turn to see the mirage explode, revealing that it was actually a trap set by a group of thieves. You narrowly escape with your life and continue your journey, shaken but grateful to be alive.")
    else:
      print("Invalid choice. You are stuck in the desert forever.")
  elif choice.lower() == "right":
    print("You take the right path and come across a snowy tundra. You see a group of friendly looking polar bears in the distance and decide to investigate. Do you APPROACH the polar bears or WALK away?")
    choice = input("What do you do? ")
    if choice.lower() == "approach":
      print("You approach the polar bears and they welcome you into their den. You spend a warm and comfortable night with them, learning about their way of life. You continue your journey feeling grateful and refreshed.")
    elif choice.lower() == "walk away":
      print("You decide to walk away and continue your journey. As you walk, you feel a sharp pain in your leg and realize you have been bitten by a venomous snake. You struggle to make it to the nearest town and receive treatment, but the venom has already spread through your body. You spend the rest of your days bedridden, regretting your decision to walk away from the polar bears.")
    else:
      print("Invalid choice. You are attacked by a swarm of bees and die.")
  else:
    print("Invalid choice. You are lost in the wilderness forever.")
    play_again()
  
print("Welcome to the Adventure Games!")
print("Please choose a game:")
print("1. Mystery/Detective")
print("2. Journey in the Woods")

game_choice = input("Enter your choice (1 or 2): ")

if game_choice == "1":
    lost_treasure()
elif game_choice == "2":
    into_the_woods()
else:
    print("Invalid choice. Please enter either 1 or 2.")