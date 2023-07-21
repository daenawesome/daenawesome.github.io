ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_BLUE = "\u001b[34m"
ANSI_YELLOW = "\u001b[33m"
ANSI_RESET = "\u001b[0m"

while True:
    name = input(ANSI_GREEN + "Please enter your name: \n" + ANSI_RESET)

    while True:
        age = input(ANSI_GREEN + "Please enter your age: \n" + ANSI_RESET)
        if age.isdigit():
            age = int(age)
            break
        else:
            print(ANSI_RED + "Error: Please use numbers for age input.\n" + ANSI_RESET)
            
    while True:
        favorite_color = input(ANSI_GREEN + "Please enter your favorite color: \n" + ANSI_RESET)
        if favorite_color.isalpha():
            break
        else:
            print(ANSI_RED + "Error: Please use letters for this input." + ANSI_RESET)
            
    while True:    
        shirt_color = input(ANSI_GREEN + "Please enter the color of your shirt: \n" + ANSI_RESET)
        if shirt_color.isalpha():
            break
        else:
            print(ANSI_RED + "Error: Please use letters for this input." + ANSI_RESET)

    if age < 18:
        print(ANSI_BLUE + "\nHello, " + name + "!")
        print("You are " + str(age) + " years old and your favorite color is " + favorite_color + ".")
        print("You are not yet an adult." + ANSI_RESET)
    elif age < 30:
        print(ANSI_BLUE + "\nHello, " + name + "!")
        print("You are " + str(age) + " years old and your favorite color is " + favorite_color + ".")
        print("You are a young adult." + ANSI_RESET)
    elif age < 50:
        print(ANSI_BLUE + "\nHello, " + name + "!")
        print("You are " + str(age) + " years old and your favorite color is " + favorite_color + ".")
        print("You are a middle-aged adult." + ANSI_RESET)
    else:
        print(ANSI_BLUE + "\nHello, " + name + "!")
        print("You are " + str(age) + " years old and your favorite color is " + favorite_color + ".")
        print("You are a senior adult." + ANSI_RESET)

    if shirt_color != favorite_color:
        print(ANSI_BLUE + "And why are you not wearing your favorite color?" + ANSI_RESET)
    else:
        print(ANSI_BLUE + "Why am I not surprised you chose that shirt :P" + ANSI_RESET)
        
    #input('Press ENTER to exit')

    run_again = input(ANSI_YELLOW + "\nWould you like to run the script again? (y/n)\n" + ANSI_RESET)
    if run_again == "n":
        print("BYE!")
        break
    
    
    """
    This program demonstrates the use of input and output, as well as the use of if and elif statements and while loops to control the flow of the program. 
    It also shows creativity in the way it shows different text colors, personalizes the messages based on the user's inputs, and allows the user to run the script multiple times with new inputs each time.
    """
