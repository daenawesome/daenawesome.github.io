# ask the user for the price of a child's meal
child_meal_price = float(input("Enter the price of a child's meal: "))

# ask the user for the price of an adult's meal
adult_meal_price = float(input("Enter the price of an adult's meal: "))

# ask the user for the number of children
num_children = int(input("Enter the number of children: "))

# ask the user for the number of adults
num_adults = int(input("Enter the number of adults: "))

# ask the user for the sales tax rate
sales_tax_rate = float(input("Enter the sales tax rate: "))

# ask the user if they want to include drinks in the meal
include_drinks = input("Include drinks in the meal? (y/n) ")

# ask the user for the price of a drink if they want to include drinks
if include_drinks == "y":
  drink_price = float(input("Enter the price of a drink: "))
else:
  drink_price = 0

# ask the user if they want to include appetizers in the meal
include_appetizers = input("Include appetizers in the meal? (y/n) ")

# ask the user for the price of an appetizer if they want to include appetizers
if include_appetizers == "y":
  appetizer_price = float(input("Enter the price of an appetizer: "))
else:
  appetizer_price = 0

# ask the user if they want to include a tip in the meal
include_tip = input("Include a tip in the meal? (y/n) ")

# ask the user for the tip percentage if they want to include a tip
if include_tip == "y":
  tip_percentage = float(input("Enter the tip percentage: "))
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
payment = float(input("Enter the payment amount: "))

# compute the change
change = payment - total_price

# display the change
print("Change: $" + str(round(change, 2)))


"""
additional features such as the option to include drinks, appetizers, or a tip percentage in the meal 
"""