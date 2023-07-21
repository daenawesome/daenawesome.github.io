# Break from terminal default for user interface readability.
print()
print("---------------------------------------------------------------------------")
print()
# Greet user and acquire name.
pl_name = input("Greetings Adventurer! Please enter your name below:\n\n").capitalize()
# Break line for readbility.
print()
print("---------------------------------------------------------------------------")
print()
# Affirm user and ask if they would like to play the game.
choice_1 = input(
    f"Hello {pl_name}, It is a pleasure to meet you. Would you like to play a game?\n\nYES/NO: "
).capitalize()
# Set condition default.
trapped = False
# If user chose to play, begin game.
if choice_1 == "Yes":
    # Break line for readability.
    print()
    print("---------------------------------Character---------------------------------")
    print()
    # Give user a short description of their hero and their objective.
    print(
        "You are a Warrior. Clad in a suit of platemail and wielding a long-sword\nand shield, few men can stand against you, but you are not hunting men,\nyou are hunting monsters.\n\nYou have 25 Hit Points"
    )
    # Break line for readability
    print()
    print("-----------------------------------Start-----------------------------------")
    print()
    choice_2 = input(
        "Your adventure starts at the entrance to an ancient tomb, untouched by man\nfor millenia, where you have tracked a monster that has been preying on the\nlocal village for the better half of the past year. There are runes etched\ninto the surface of the door and it appears to be unlocked. You are unsure\nif the runes are left over from ages past or if the monster you have been\ntracking has the intelligence to create such things. Do you wish to OPEN\nthe door, EXAMINE the runes, or SEARCH for another entrance.\n\nYour Choice: "
    ).capitalize()
    # Break line for readability
    print()
    print("---------------------------------------------------------------------------")
    print()
    if choice_2 == "Search":
        choice_3 = input(
            "As you search the surrounding landscape, you come across a trap door that\nappears to lead down into the tomb. Do you wish to ENTER the trap door or\nBLOCK it off to prevent anything from inside escaping and return to the\nmain entrance?\n\nYour Choice: "
        ).capitalize()
        # Break line for readability
        print()
        print(
            "---------------------------------------------------------------------------"
        )
        print()
        if choice_3 == "Enter":
            choice_4 = input(
                'You slip into a dark cave and find yourself face to face with your target; \na large half snake, half woman known only as "Marilith." Do you wish to\nATTACK or attempt to SUBDUE her?\n\nYour Choice: '
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if choice_4 == "Attack":
                print("Your blade strikes true as the Marilith falls before you.")
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print(
                    "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                )
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            elif choice_4 == "Subdue":
                # Third level resolution.
                print(
                    "The Marilith deftly slips from your grasp and slithers up and out of the\ntrap door. A loud *thud* shortly follows as the door is blocked from the\nother side."
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                print("Stay tuned for further adventures!")
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            else:
                print()
                print("Invalid choice, please try again.")
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
        elif choice_3 == "Block":
            print("After blocking off the trap door, you return to the entrance.")
            # Trigger condition change.
            trapped = True
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            choice_2 = input(
                "As you return to the entrance, you are left with 2 choices: OPEN the door\nor EXAMINE the runes.\n\nYour Choice: "
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
        else:
            print("Invalid choice, please try again.")
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
    if choice_2 == "Open":
        print(
            "The runes were a trap!\n\nAs you open the door, they shine a bright blue hue and explode in your\nface. You narrowly escape with your head intact but are damaged and\n are temporarily blinded from the explosion\n\nYou now have 15 Hit Points."
        )
        # Break line for readability
        print()
        print(
            "---------------------------------------------------------------------------"
        )
        print()
        choice_3 = input(
            "As you reel from the shock of the explosion, still unable to see straight,\nyou hear thundering footsteps rushing towards you yelling a battlecry.\nDo you wish to STRIKE blindly towards the sound, raise your SHIELD in an\nattempt to block the oncoming attack, or SPEAK to your attacker?\n\nYour Choice: "
        ).capitalize()
        # Break line for readability
        print()
        print(
            "---------------------------------------------------------------------------"
        )
        print()
        if choice_3 == "Strike":
            print(
                "As you strike wildly, you feel your sword thrust into open space. As the\nrealization that you have missed your target sets in, a heavy weight comes\ncrashing down onto your arm and knocks your sword out of your hand.\n\nYou now have 10 Hit Points"
            )
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            choice_4 = input(
                "As you look up from the ground, your sight begins to return to you. You see\na hulking barbarian, one foot pinning your arm to the ground, raising his\nmaul above his head, preparing to crush your skull. Do you wish to try to\nESCAPE, RAISE your shield to try and block the blow, or PLEAD for your life?\n\nYour Choice: "
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if choice_4 == "Escape":
                print(
                    "As you attempt to wrench free, the man swings his maul down on your face."
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print("You Died")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            elif choice_4 == "Raise":
                print(
                    "You manage to get your shield in between you and your attacker but at a\nheavy price. Your shield is now broken, as is your arm, and you black out.\n\nYou have 1 Hit Point.\n\nYou awaken some time later with a splitting headache to find that your gea\nhas been stripped from you but you are alive. Better yet, the body of the\nMarilith lies dead a short distance away. Maybe you can still turn in the\nhead for the reward."
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print("CONGRATULATIONS! Someone else has done your job for you.")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            elif choice_4 == "Plead":
                print(
                    'The man standing above you looks down in disgust. "Puny man," he mocks,\n"why have you--"\n\nHe is cut off mid-sentence as the tail of the Marilith wraps around his neck'
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                choice_5 = input(
                    "Do you wish to RUN away or FINISH your mission?\n\nYour Choice: "
                ).capitalize()
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if choice_5 == "Run":
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    print(
                        "You flee the cave not even daring to look back. You hear the Marilith\ntaunting you from within the cave."
                    )
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("CONGRATULATIONS! You escaped with your life.")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()  # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                elif choice_5 == "Finish":
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    print(
                        "You grab your sword through the agony in your arm and sweep around behind the Marilith, plunging your sword through her heart. The man is dead from the attack but at least you still accomplished your objective."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print(
                        "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                    )
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()  # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                else:
                    print("Invalid choice, please try again.")
            else:
                print("Invalid choice, please try again.")
        elif choice_3 == "Shield":
            print(
                "You raise your shield just in time to absorb the massive blow. You are knocked back\na few feet from the force but have bought yourself a few, much needed,\nseconds to react.\n\nYou still have 15 Hit Points"
            )
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            choice_4 = input(
                "As you recover from the blow, your sight comes back into focus. You are\nable to see your foe and are surprised to find that you are not fighting\nthe description of the monster you were contracted to kill but are instead\nfacing a behemoth of a man wearing leather clothing and wielding a giant\nmaul. Do you wish to continue the FIGHT, REASON with the man, or FLEE this\nforsaken place?\n\nYour Choice: "
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if choice_4 == "Fight":
                print(
                    "As you strike at the man before you, he is suddenly attacked from behind.\nHe gasps for air as the tail of the Marilith wraps around his neck"
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                choice_5 = input(
                    "Do you wish to RUN away or FINISH your mission?\n\nYour Choice: "
                ).capitalize()
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if choice_5 == "Run":
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    print(
                        "You flee the cave not even daring to look back. You hear the Marilith\ntaunting you from within the cave."
                    )
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("CONGRATULATIONS! You escaped with your life.")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                elif choice_5 == "Finish":
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    print(
                        "You grab your sword through the agony in your arm and sweep around behind\nthe Marilith, plunging your sword through her heart. The man is dead from\nthe attack but at least you still accomplished your objective."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print(
                        "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                    )
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
            elif choice_4 == "Reason":
                print(
                    'You shout at the man, "halt! Whoever you are, I mean you no harm! I have\ncome to slay the Marilith."\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."'
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if trapped == True:
                    print(
                        "As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate."
                    )
                    print("Your blade strikes true as the Marilith falls before you.")
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print(
                        "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                    )
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                else:
                    print(
                        "As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("OH NO! The monster has escaped. Better luck next time!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
            elif choice_4 == "Flee":
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                print(
                    "You flee the cave not even daring to look back. You hear the man\ntaunting you from within the cave."
                )
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print("CONGRATULATIONS! You escaped with your life.")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            else:
                print("Invalid choice, please try again.")
        elif choice_3 == "Speak":
            print(
                'Realizing that the prey you seek slithers across the ground and does not\nhave feet to run with, you shout, "halt! Whoever you are, I mean you no harm!\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."'
            )
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if trapped == True:
                print(
                    "As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate."
                )
                print("Your blade strikes true as the Marilith falls before you.")
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print(
                    "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                )
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            else:
                print(
                    "As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side."
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print("OH NO! The monster has escaped. Better luck next time!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
        else:
            print("Invalid choice, please try again.")
    elif choice_2 == "Examine":
        choice_3 = input(
            "As you examine the runes, you can see they are meant to be a trap. Though\nthe finer points of how they work elude you, you do know that it will\nexplode if you just open the door. What is even more disturbing however,\nis that you have confirmed that the runes are freshly, if crudely, etched.\nDo you wish to try and SNEAK past the trap or SUFFER the\ntrap regardless of the outcome?\n\nYour Choice: "
        ).capitalize()
        # Break line for readability
        print()
        print(
            "---------------------------------------------------------------------------"
        )
        print()
        if choice_3 == "Sneak":
            print(
                "You manage to get yourself past the runes without an explosion to the face\n\nYou still have 25 Hit Points."
            )
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            choice_4 = input(
                'As you begin to straighten yourself out, a giant of a man grabs your\narm and pins you to the wall\n\n"I thought you were the creature there for a moment."\n\nAs the man releases you, the trap explodes as an angry Marilith\nenters into the cave through the entrance you just passed through. Do you wish\nto DEFEND the man next to you or LUNGE forward with your blade?\n\nYour Choice: '
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if choice_4 == "Defend":
                print(
                    "You instinctively raise your shield to block the attack against the man you\njust met. You manage to block the first attack but receive a nasty bite\non your neck.\n\nYou now have 20 Hit Points and are poisoned."
                )
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                choice_5 = input(
                    "As the poison rushes through your veins, you can feel yourself weakening. Do you wish to FLEE or FIGHT?\n\nYour Choice: "
                ).capitalize()
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if choice_5 == "Flee":
                    print(
                        "You run for your life knowing full-well that if you do not make it back\nto the village in time, the poison will kill you.\n\nSeveral hours later as you are recovering from the poison in the village,\nyou see the man from the cave walk by carrying the body of the dead \nMarilith into the office of the local hunting guild."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("CONGRATULATIONS! Someone else has done your job for you.")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                elif choice_5 == "Fight":
                    print(
                        "You lunge forward with all your might, narrowly avoiding the first attack\nand seeing the second get blocked by the man. Suddenly, you realize the\nMarilith is trapped in his grip allowing you a final blow. Shortly\nafterward, you collapse. You wake up some time later, healed of your\npoisoning, thanks to the man who carried you to the village and absconded\nwith the bounty"
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print(
                        "CONGRATULATIONS! You have slain the monster terrorizing the nearby village.\nToo bad about the money though."
                    )
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                else:
                    print("Invalid choice, please try again.")
            elif choice_4 == "Lunge":
                print(
                    'You lunge towards your target only to feel a giant hand grab you from behind and toss you back. You watch on in awe as the man you just met tears into the Marilith with a ferocity you have only seen in wild animals. When the fight is over, the man walks over to you and says, "thank you for the distraction, let us head back to the village for the reward"'
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print("CONGRATULATIONS! You survived!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                # Break line for readability
                print(
                    "---------------------------------------------------------------------------"
                )
                print("Stay tuned for further adventures!")
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
            else:
                print("Invalid choice, please try again.")
        elif choice_3 == "Suffer":
            print(
                "As you open the door, the runes shine a bright blue hue and explode in\nyour face. You take the full brunt of the damage and are\ntemporarily blinded from the explosion\n\nYou now have 10 Hit Points."
            )
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            choice_3 = input(
                "As you reel from the shock of the explosion, still unable to see straight,\nyou hear thundering footsteps rushing towards you yelling a battlecry.\nDo you wish to STRIKE blindly towards the sound, raise your SHIELD in an\nattempt to block the oncoming attack, or SPEAK to your attacker?\n\nYour Choice: "
            ).capitalize()
            # Break line for readability
            print()
            print(
                "---------------------------------------------------------------------------"
            )
            print()
            if choice_3 == "Strike":
                print(
                    "As you strike wildly, you feel your sword thrust into open space. As the\nrealization that you have missed your target sets in, a heavy weight comes\ncrashing down onto your arm and knocks your sword out of your hand.\n\nYou now have 10 Hit Points"
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                choice_4 = input(
                    "As you look up from the ground, your sight begins to return to you. You see\na hulking barbarian, one foot pinning your arm to the ground, raising his\nmaul above his head, preparing to crush your skull. Do you wish to try to\nESCAPE, RAISE your shield to try and block the blow, or PLEAD for your life?\n\nYour Choice: "
                ).capitalize()
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if choice_4 == "Escape":
                    print(
                        "As you attempt to wrench free, the man swings his maul down on your face."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("You Died")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                elif choice_4 == "Raise":
                    print(
                        "You manage to get your shield in between you and your attacker but at a\nheavy price. Your shield is now broken, as is your arm, and you black out.\n\nYou have 1 Hit Point.\n\nYou awaken some time later with a splitting headache to find that your gea\nhas been stripped from you but you are alive. Better yet, the body of the\nMarilith lies dead a short distance away. Maybe you can still turn in the\nhead for the reward."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("CONGRATULATIONS! Someone else has done your job for you.")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                elif choice_4 == "Plead":
                    print(
                        'The man standing above you looks down in disgust. "Puny man," he mocks,\n"why have you--"\n\nHe is cut off mid-sentence as the tail of the Marilith wraps around his neck'
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    choice_5 = input(
                        "Do you wish to RUN away or FINISH your mission?\n\nYour Choice: "
                    ).capitalize()
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    if choice_5 == "Run":
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        print(
                            "You flee the cave not even daring to look back. You hear the Marilith\ntaunting you from within the cave."
                        )
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("CONGRATULATIONS! You escaped with your life.")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                    elif choice_5 == "Finish":
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        print(
                            "You grab your sword through the agony in your arm and sweep around behind the Marilith, plunging your sword through her heart. The man is dead from the attack but at least you still accomplished your objective."
                        )
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print(
                            "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                        )
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                    else:
                        print("Invalid choice, please try again.")
                else:
                    print("Invalid choice, please try again.")
            elif choice_3 == "Shield":
                print(
                    "You raise your shield just in time to absorb the massive blow. You are knocked back\na few feet from the force but have bought yourself a few, much needed,\nseconds to react.\n\nYou still have 15 Hit Points"
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                choice_4 = input(
                    "As you recover from the blow, your sight comes back into focus. You are\nable to see your foe and are surprised to find that you are not fighting\nthe description of the monster you were contracted to kill but are instead\nfacing a behemoth of a man wearing leather clothing and wielding a giant\nmaul. Do you wish to continue the FIGHT, REASON with the man, or FLEE this\nforsaken place?\n\nYour Choice: "
                ).capitalize()
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if choice_4 == "Fight":
                    print(
                        "As you strike at the man before you, he is suddenly attacked from behind.\nHe gasps for air as the tail of the Marilith wraps around his neck"
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    choice_5 = input(
                        "Do you wish to RUN away or FINISH your mission?\n\nYour Choice: "
                    ).capitalize()
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    if choice_5 == "Run":
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        print(
                            "You flee the cave not even daring to look back. You hear the Marilith\ntaunting you from within the cave."
                        )
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("CONGRATULATIONS! You escaped with your life.")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                    elif choice_5 == "Finish":
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        print(
                            "You grab your sword through the agony in your arm and sweep around behind\nthe Marilith, plunging your sword through her heart. The man is dead from\nthe attack but at least you still accomplished your objective."
                        )
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print(
                            "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                        )
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                elif choice_4 == "Reason":
                    print(
                        'You shout at the man, "halt! Whoever you are, I mean you no harm! I have\ncome to slay the Marilith."\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."'
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    if trapped == True:
                        print(
                            "As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate."
                        )
                        print(
                            "Your blade strikes true as the Marilith falls before you."
                        )
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print(
                            "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                        )
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                    else:
                        print(
                            "As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side."
                        )
                        # Break line for readability
                        print()
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("OH NO! The monster has escaped. Better luck next time!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                        # Break line for readability
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print("Stay tuned for further adventures!")
                        print(
                            "---------------------------------------------------------------------------"
                        )
                        print()
                elif choice_4 == "Flee":
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    print(
                        "You flee the cave not even daring to look back. You hear the man\ntaunting you from within the cave."
                    )
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("CONGRATULATIONS! You escaped with your life.")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                else:
                    print("Invalid choice, please try again.")
            elif choice_3 == "Speak":
                print(
                    'Realizing that the prey you seek slithers across the ground and does not\nhave feet to run with, you shout, "halt! Whoever you are, I mean you no harm!\n\nThe man replies, "the Marilith has fled deeper into the cave. Come, join\nme in finishing her off."'
                )
                # Break line for readability
                print()
                print(
                    "---------------------------------------------------------------------------"
                )
                print()
                if trapped == True:
                    print(
                        "As you enter the final part of the cave, you find the Marilith attempting\nto escape through the trap door you blocked off earlier. Your new friend\ngrabs her by the tail and slams her to the ground in font of you as you\ndeliver the final coup de grâce. The two of you lop off the head and head\nback to town to collect the bounty and celebrate."
                    )
                    print("Your blade strikes true as the Marilith falls before you.")
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print(
                        "CONGRATULATIONS! You have slain the monster terrorizing the nearby village."
                    )
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                else:
                    print(
                        "As you enter the final part of the cave, you find the Marilith escaping\nthrough a trap door in the ceiling towards the back. A loud *thud* shortly\nfollows as the door is blocked from the other side."
                    )
                    # Break line for readability
                    print()
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("OH NO! The monster has escaped. Better luck next time!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
                    # Break line for readability
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print("Stay tuned for further adventures!")
                    print(
                        "---------------------------------------------------------------------------"
                    )
                    print()
            else:
                print("Invalid choice, please try again.")
        else:
            print("Invalid choice, please try again.")
    else:
        # If loop designed to remove a double 'invalid choice' error code when going through
        # search option at beginning of code due to the 2 separate if loops. I'm sure there
        # is a better way to do my overall loops with while statements but I couldn't get them
        # to work how I wanted them to so this at least works.
        if choice_2 != "Search":
            print("Invalid choice, please try again.")

elif choice_1 == "No":
    # Break line for readability
    print()
    print("---------------------------------------------------------------------------")
    print(f"Well, your loss, I guess. Goodbye, {pl_name}.")
    print("---------------------------------------------------------------------------")
    print()
else:
    # Break line for readability
    print()
    print("---------------------------------------------------------------------------")
    print("Invalid choice, please try again.")
    print("---------------------------------------------------------------------------")
    print()
