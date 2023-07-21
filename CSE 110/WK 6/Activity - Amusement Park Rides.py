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

age1 = int(input("Enter the age of the first rider: "))
height1 = int(input("Enter the height of the first rider (in inches): "))

if can_ride(age1, height1):
    print("The first rider can ride the car.")
else:
    print("The first rider cannot ride the car.")

has_second_rider = input("Is there a second rider (y/n)? ")

if has_second_rider == 'y':
    age2 = int(input("Enter the age of the second rider: "))
    height2 = int(input("Enter the height of the second rider (in inches): "))
    if can_ride_with_other(age1, height1, age2, height2):
        print("The two riders can ride the car together.")
    elif can_ride_with_other_14_16(age1, age2):
        print("The two riders can ride the car together.")
    else:
        print("The two riders cannot ride the car together.")

"""
This program prompts the user for the age and height of the first rider and 
then asks whether there is a second rider. If there is a second rider, it 
prompts the user for the age and height of the second rider. It then uses the 
'can_ride' and 'can_ride_with_other' functions to determine if the riders can ride 
the car according to rules of the park.
"""