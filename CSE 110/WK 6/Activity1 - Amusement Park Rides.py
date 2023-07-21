def can_ride(age, height):
    if age < 12 or height < 36:
        return False
    if age >= 18 and height >= 62:
        return True
    return False

def can_ride_with_other(age1, height1, age2, height2):
    if age1 >= 18 or age2 >= 18:
        return True
    if age1 < 12 or age2 < 12 or height1 < 52 or height2 < 52:
        return False
    return True

def can_ride_with_other_14_16(age1, age2):
    if age1 >= 16 and age2 >= 14:
        return True
    if age2 >= 16 and age1 >= 14:
        return True
    return False

def display_ticket(name):
    print("Hello, {}! Here is your virtual ticket for the ride:".format(name))
    print("---------------------------")
    print("|  AMUSEMENT PARK RIDE   |")
    print("|                        |")
    print("|       VIRTUAL TICKET   |")
    print("|                        |")
    print("|  Enjoy the ride!       |")
    print("---------------------------")

def display_sorry_message(name):
    print("Sorry, {}. You are not allowed to ride the car.".format(name))

def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age < 0:
                raise ValueError
            return age
        except ValueError:
            print("Please enter a valid age (a positive integer).")

def get_height(prompt):
    while True:
        try:
            height = int(input(prompt))
            if height < 0:
                raise ValueError
            return height
        except ValueError:
            print("Please enter a valid height (a positive integer).")

name1 = input("Enter the name of the first rider: ")
age1 = get_age("Enter the age of the first rider: ")
height1 = get_height("Enter the height of the first rider (in inches): ")

if can_ride(age1, height1):
    display_ticket(name1)
else:
    display_sorry_message(name1)

has_second_rider = input("Is there a second rider (y/n)? ")

if has_second_rider == 'y':
    name2 = input("Enter the name of the second rider: ")
    age2 = get_age("Enter the age of the second rider: ")
    height2 = get_height("Enter the height of the second rider (in inches): ")
    if can_ride_with_other(age1, height1, age2, height2):
        display_ticket(name1)
        display_ticket(name2)
    elif can_ride_with_other_14_16(age1, age2):
        display_ticket(name1)
        display_ticket(name2)
    else:
        display_sorry_message(name1)
        display_sorry_message(name2)


"""
Added a virtual ticket display if the riders are allowed to ride 
and a virtual "sorry" message if they are not allowed to ride. Also 
prompting the user to enter their name and then using that name 
in the virtual ticket or "sorry" message.

Finally, added some basic error handling to the program, such as checking for invalid 
input (e.g. non-numeric input for ages and heights) and displaying an error message if 
invalid input is detected.
"""