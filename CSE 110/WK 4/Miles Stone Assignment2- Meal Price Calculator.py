while True:
  # ask the user for the price of a child's meal
  while True:
    try:
      child_meal_price = float(input("Enter the price of a child's meal: "))
      if child_meal_price > 0:
        break
      else:
        print("Error: Please enter a valid price.")
    except ValueError:
      print("Error: Please enter a valid price.")
  
  # ask the user for the price of an adult's meal
  while True:
    try:
      adult_meal_price = float(input("Enter the price of an adult's meal: "))
      if adult_meal_price > 0:
        break
      else:
        print("Error: Please enter a valid price.")
    except ValueError:
      print("Error: Please enter a valid price.")
  
  # ask the user for the number of children
  while True:
    try:
      num_children = int(input("Enter the number of children: "))
      if num_children >= 0:
        break
      else:
        print("Error: Please enter a valid number.")
    except ValueError:
      print("Error: Please enter a valid number.")
  
  # ask the user for the number of adults
  while True:
    try:
      num_adults = int(input("Enter the number of adults: "))
      if num_adults >= 0:
        break
      else:
        print("Error: Please enter a valid number.")
    except ValueError:
      print("Error: Please enter a valid number.")
  
  # ask the user for the sales tax rate
  while True:
    try:
      sales_tax_rate = float(input("Enter the sales tax rate: "))
      if 0 <= sales_tax_rate <= 100:
        break
      else:
        print("Error: Please enter a valid sales tax rate.")
    except ValueError:
      print("Error: Please enter a valid sales tax rate.")
  
  # ask the user if they want to include drinks in the meal
  include_drinks = input("Include drinks in the meal? (y/n) ")
  
  # ask the user for the price of a drink if they want to include drinks
  if include_drinks == "y":
    while True:
      try:
        drink_price = float(input("Enter the price of a drink: "))
        if drink_price > 0:
          break
        else:
          print("Error: Please enter a valid price.")
      except ValueError:
        print("Error: Please enter a valid price.")
  else:
    drink_price = 0
  
  # ask the user if they want to include appetizers in the meal
  include_appetizers = input("Include appetizers in the meal? (y/n) ")
  
  # ask the user for the price of an appetizer if they want to include appetizers
  if include_appetizers == "y":
    while True:
      try:
        appetizer_price = float(input("Enter the price of an appetizer: "))
        if appetizer_price > 0:
          break
        else:
          print("Error: Please enter a valid price.")
      except ValueError:
        print("Error: Please enter a valid price.")
  else:
    appetizer_price = 0
    
  # ask the user if they want to include a tip in the meal
  include_tip = input("Include a tip in the meal? (y/n) ")
  
  # ask the user for the tip percentage if they want to include a tip
  if include_tip == "y":
    while True:
      try:
        tip_percentage = float(input("Enter the tip percentage: "))
        if 0 <= tip_percentage <= 100:
          break
        else:
          print("Error: Please enter a valid tip percentage.")
      except ValueError:
        print("Error: Please enter a valid tip percentage.")
  else:
    tip_percentage = 0
    
  # compute the subtotal
  subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults) + drink_price + appetizer_price
  
  # display the subtotal
  print("Subtotal: $" + str(round(subtotal, 2)))
  
  # compute the sales tax
  sales_tax = subtotal * (sales_tax_rate / 100)
  
  # display the sales tax
  print("Sales tax: $" + str(round(sales_tax, 2)))
  
  # compute the tip
  tip = subtotal * (tip_percentage / 100)
  
  # display the tip
  print("Tip: $" + str(round(tip, 2)))
  
  # compute the total price
  total_price = subtotal + sales_tax + tip
  
  # display the total price
  print("Total price: $" + str(round(total_price, 2)))
  
  # ask the user for the payment amount
  while True:
    try:
      payment = float(input("Enter the payment amount: "))
      if payment >= total_price:
        break
      else:
          print("Error: Please enter a valid payment value.")
    except ValueError:
        print("Error: Please enter a valid payment value.")
    else:
      payment = 0
  
  # compute the change
  change = payment - total_price
  
  # display the change
  print("Change: $" + str(round(change, 2)))
  
  # prompt the user to play again or exit
  play_again = input("Do you want to calculate again? (y/n) ").lower()
  if play_again != "y":
    break


"""
with input validation to ensure that the user enters valid values 
and additional features such as the option to include drinks, appetizers, 
or a tip percentage in the meal 

The program I made from the assignment asks the user to enter the price of a child's meal, the price of an adult's meal, the number of children and adults, and the sales tax rate. But I made it my own by including features that the user might also want to include, such as drinks, appetizers, and a tip. It then calculates a subtotal, sales tax, tip, and total price based on the user's inputs and displays these values to the user. 

I used a combination of while loops and try/except blocks to handle errors and ensure that the user enters valid input. There are also if-else statements to handle the inclusion of drinks, appetizers, and a tip in the final calculation. It has an outer loop that continues indefinitely, so the user can input multiple sets of data without having to restart the program. 
"""