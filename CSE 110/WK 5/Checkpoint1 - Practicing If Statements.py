# get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# if/else statement to check if num1 is greater than num2
if num1 > num2:
  print("The first number is greater")
else:
  print("The first number is not greater")

# if/else statement to check if num1 is equal to num2
if num1 == num2:
  print("The numbers are equal")
else:
  print("The numbers are not equal")

# if/else statement to check if num2 is greater than num1
if num2 > num1:
  print("The second number is greater")
else:
  print("The second number is not greater")

# if/else statement to check if the numbers are both even or odd
if num1 % 2 == 0 and num2 % 2 == 0:
  print("The numbers are both even")
elif num1 % 2 == 1 and num2 % 2 == 1:
  print("The numbers are both odd")
else:
  print("The numbers are not both even or odd")

# if/else statement to check if the numbers are both positive or negative
if num1 > 0 and num2 > 0:
  print("The numbers are both positive")
elif num1 < 0 and num2 < 0:
  print("The numbers are both negative")
else:
  print("The numbers are not both positive or negative")
print()
# get input from the user for their name and favorite animal
name = input("What is your name? ")
favorite_animal = input("What is your favorite animal, {0}? ".format(name))

# if statement to check if the user's favorite animal is the same as the programmer's
if favorite_animal.lower() == "panda":
  print("{0}, that's my favorite animal too!".format(name))
else:
  print("{0}, that is not my favorite animal.".format(name))
  print("it's PANDA!")

# print ASCII art of a panda
print(r"""
            ,,,         ,,,
          ;"   ^;     ;'   ",
          ;    s$$$$$$$s     ;
          ,  ss$$$$$$$$$$s  ,'
          ;s$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$
         $$$$P""Y$$$Y""W$$$$$
         $$$$  p"$$$"q  $$$$$
         $$$$  .$$$$$.  $$$$
          $$DcaU$$$$$$$$$$
by          "Y$$$"*"$$$Y"    aka
Daen            "$b.$$"     Panda
 """)

input('\nPress ENTER to exit')

"""
The program prompts the user for two integers and compares them using if/else statements, 
printing out a message based on the comparison. It then asks the user for their name and 
favorite animal, and checks if the user's favorite animal is the same as the programmer's 
using an if statement. It also includes additional if/else statements to check if the two 
numbers are both even or odd, and if they are both positive or negative, as well as some 
ASCII art of a panda at the end.
"""