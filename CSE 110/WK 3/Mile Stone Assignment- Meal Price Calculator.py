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

# compute the subtotal
subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)

# display the subtotal
print("Subtotal: $" + str(round(subtotal, 2)))

# compute the sales tax
sales_tax = subtotal * (sales_tax_rate / 100)

# display the sales tax
print("Sales tax: $" + str(round(sales_tax, 2)))

# compute the total price
total_price = subtotal + sales_tax

# display the total price
print("Total price: $" + str(round(total_price, 2)))

# ask the user for the payment amount
payment = float(input("Enter the payment amount: "))

# compute the change
change = payment - total_price

# display the change
print("Change: $" + str(round(change, 2)))
