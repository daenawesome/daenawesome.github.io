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
print ()
# get input from the user for their favorite animal
favorite_animal = input("What is your favorite animal? ")

# if statement to check if the user's favorite animal is the same as the programmer's
if favorite_animal.lower() == "panda":
  print("That's my favorite animal too!")
else:
  print("That one is not my favorite.")

input('\nPress ENTER to exit')