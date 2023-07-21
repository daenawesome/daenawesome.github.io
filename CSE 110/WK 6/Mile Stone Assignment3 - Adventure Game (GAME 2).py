# Welcome message
print("Welcome to the Adventure Game!")

# First level
print("You are on a journey through a dark forest. You come to a fork in the road and see a sign that reads:")
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
  
