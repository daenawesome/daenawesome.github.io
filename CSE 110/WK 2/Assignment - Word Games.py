ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_BLUE = "\u001b[34m"
ANSI_YELLOW = "\u001b[33m"
ANSI_RESET = "\u001b[0m"

while True:
    animal = input("\nEnter an animal: ")
    print()
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter one more adjective: ")
    adjective4 = input("Enter one last adjective: ")
    print()
    verb = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter one more verb: ")
    print()
    noun = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")
    print()
    exclamation = input("Enter an exclamation: ")
    print()
    
    # Determine the correct article to use based on the first letter of the noun
    if noun[0] in ['a', 'e', 'i', 'o', 'u']:
      article = "an"
    else:
      article = "a"
     
    # Present the user with a list of possible endings for the story
    print("Choose one of the following endings for the story:" + ANSI_RESET)
    print(ANSI_RED + "1. The end." + ANSI_RESET)
    print(ANSI_GREEN + "2. To be continued..." + ANSI_RESET)
    print(ANSI_BLUE + "3. The story continues..." + ANSI_RESET)
    ending_choice = int(input("Enter the number of your chosen ending: "))

    # Choose the ending based on the user's choice
    if ending_choice == 1:
      ending = ANSI_RED + "The end." + ANSI_RESET
    elif ending_choice == 2:
      ending = ANSI_GREEN + "To be continued..." + ANSI_RESET
    elif ending_choice == 3:
      ending = ANSI_GREEN + "The story continues..." + ANSI_RESET
    else:
      ending =  ANSI_RED + "The END." + ANSI_RESET

    story = f"\nThe other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family. In the end, I realized that I had left {article} {noun} in the {adjective2} room and that was what attracted the {animal}. As it turned out, the {animal} was just looking for {article} {noun2} to eat. I quickly grabbed the {noun} and ran back to my {adjective3} room, where I locked the door behind me.\n\nAfter a few minutes, I heard a knock on the door. It was the {animal} again, but this time it was holding {article} {noun3} in its mouth. It seemed to be apologizing for its earlier behavior. I couldn't believe it! I slowly opened the door and took the {noun3} from the {animal}, which then ran off into the {adjective4} night. From that moment on, I made sure to always check for any stray {noun2} before leaving the room. And I also learned to always be prepared for the unexpected, especially when it comes to {adjective} {animal}! \n\n{ending}"

    print("\nSo the story goes like this:\n" + story)

    run_again = input(ANSI_YELLOW + "\nWould you like to run the script again? (y/n)\n" + ANSI_RESET)
    if run_again == "n":
        print("BYE!")
        break
        
    """
    I tried to adding simple options prompting the user for inputs for additional words to incorporate to the story,
    allowing the user to choose the ending of the story, and by using formatting techniques to add visual interest to the narrative.
    """







