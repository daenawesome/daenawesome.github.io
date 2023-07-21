

def start_game():
    print("Welcome to the Mystery/Detective Text Adventure Game!")
    print("What's your name?")
    player_name = input().strip()
    print("Hi, {}! Let's start the adventure.".format(player_name))

    scenario_1(player_name)
    
def ending_scenario(player_name):
    print("\nCongratulations, {}! You have solved the crime and brought the culprit to justice.".format(player_name))
    print("Thank you for playing the Mystery/Detective Text Adventure Game. Have a great day!")
    return

# done
def scenario_1(player_name):
    print("\nYou are a detective and received a mysterious call from an unknown number. The caller says, 'Detective {}, I have information about a crime and I want to meet with you at the park.'".format(player_name))
    print("What would you like to do next?\nMEET THE CALLER\nIGNORE THE CALL\nCALL THE POLICE")
    
    # takes the user's input, removes any whitespaces from the start and end, and returns the input in uppercase.
    choice = input().strip().upper()

    if choice == "MEET THE CALLER":
        scenario_2a(player_name)
    elif choice == "IGNORE THE CALL":
        scenario_2b(player_name)
    elif choice == "CALL THE POLICE":
        scenario_2c(player_name)
    else:
        print("Invalid choice. Please choose MEET THE CALLER, IGNORE THE CALL, or CALL THE POLICE.")
        scenario_1(player_name)

def scenario_2a(player_name):
    print("\nYou decide to meet the caller at the park.")
    print("As you approach the meeting spot, you see a person wearing a hoodie and a mask. What would you like to do next?\nAPPROACH THE PERSON\nRUN AWAY\nCALL FOR BACKUP")

    choice = input().strip().upper()

    if choice == "APPROACH THE PERSON":
        scenario_3a(player_name)
    elif choice == "RUN AWAY":
        scenario_3b(player_name)
    elif choice == "CALL FOR BACKUP":
        scenario_3c(player_name)
    else:
        print("Invalid choice. Please choose APPROACH THE PERSON, RUN AWAY, or CALL FOR BACKUP.")
        scenario_2a(player_name)

def scenario_2b(player_name):
    print("\nYou decide to ignore the call.")
    print("However, the caller continues to call and leave you threatening messages. What would you like to do next?\nCHANGE YOUR NUMBER\nCONTACT THE POLICE\nMEET THE CALLER")

    choice = input().strip().upper()

    if choice == "CHANGE YOUR NUMBER":
        scenario_3d(player_name)
    elif choice == "CONTACT THE POLICE":
        scenario_3e(player_name)
    elif choice == "MEET THE CALLER":
        scenario_3f(player_name)
    else:
        print("Invalid choice. Please choose CHANGE YOUR NUMBER, CONTACT THE POLICE, or MEET THE CALLER.")
        scenario_2b(player_name)

def scenario_2c(player_name):
    print("\nYou decide to call the police.")
    print("The police arrive and take the information about the mysterious call. They say they'll look into it and get back to you. What would you like to do next?\nWAIT FOR POLICE UPDATE\nCONTINUE INVESTIGATION\nGO ON VACATION")
    
    choice = input().strip().upper()

    if choice == "WAIT FOR POLICE UPDATE":
        scenario_3g(player_name)
    elif choice == "CONTINUE INVESTIGATION":
        scenario_3h(player_name)
    elif choice == "GO ON VACATION":
        scenario_3i(player_name)
    else:
        print("Invalid choice. Please choose WAIT FOR POLICE UPDATE, CONTINUE INVESTIGATION, or GO ON VACATION.")
        scenario_2c(player_name)
        
def scenario_3a(player_name):
    print("\nYou approach the person and they reveal the information about the crime. They tell you that they saw a suspicious figure at the nearby bank. What would you like to do next?\nINVESTIGATE THE BANK\nIGNORE THE TIP\nCALL THE POLICE")
    
    choice = input().strip().upper()

    if choice == "INVESTIGATE THE BANK":
        scenario_4a(player_name)
    elif choice == "IGNORE THE TIP":
        scenario_4b(player_name)
    elif choice == "CALL THE POLICE":
        scenario_4c(player_name)
    else:
        print("Invalid choice. Please choose INVESTIGATE THE BANK, IGNORE THE TIP, or CALL THE POLICE.")
        scenario_3a(player_name)
        
def scenario_3b(player_name):
    print("\nYou run away from the person. Later, you receive an anonymous call from the same number, revealing that the person had important information about the crime. What would you like to do next?\nRETURN TO THE PARK\nCONTACT THE POLICE\nIGNORE THE CALL")
    
    choice = input().strip().upper()

    if choice == "RETURN TO THE PARK":
        scenario_4d(player_name)
    elif choice == "CONTACT THE POLICE":
        scenario_4e(player_name)
    elif choice == "IGNORE THE CALL":
        scenario_4f(player_name)
    else:
        print("Invalid choice. Please choose RETURN TO THE PARK, CONTACT THE POLICE, or IGNORE THE CALL.")
        scenario_3b(player_name)
        
def scenario_3c(player_name):
    print("\nYou call for backup. The police arrive and the person with the information about the crime flees the scene. What would you like to do next?\nPURSUE THE PERSON\nWAIT FOR THE POLICE TO HANDLE IT\nCONTINUE INVESTIGATION ELSEWHERE")
    
    choice = input().strip().upper()

    if choice == "PURSUE THE PERSON":
        scenario_4g(player_name)
    elif choice == "WAIT FOR THE POLICE TO HANDLE IT":
        scenario_4h(player_name)
    else:
        print("Invalid choice. Please choose RETURN TO THE PARK, CONTACT THE POLICE, or IGNORE THE CALL.")
        scenario_3c(player_name)

start_game()