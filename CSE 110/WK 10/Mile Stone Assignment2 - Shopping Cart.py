# Create empty lists for storing the names, prices, and quantities of the items
names = []
prices = []
quantities = []

# Define a function to display the menu and get the user's choice
def display_menu():
    print("\nPlease choose an option:")
    print("1. Add a new item")
    print("2. Display the contents of the shopping cart")
    print("3. Remove an item ")
    print("4. Compute the total ")
    print("5. Quit")
    return int(input("Enter your choice: "))

# Define a function to add a new item
def add_item():
    name = input("What item would you like to add? ")
    if name in names:
        # check if item already exists in the cart
        index = names.index(name)
        print(name + " is already in the cart.")
        # ask user to update the quantity of the item
        quantity = int(input("Enter the new quantity of " + name + ": "))
        quantities[index] += quantity
        print("Quantity of " + name + " has been updated.")
    else:
        # add new item to the cart
        names.append(name)
        price = float(input("What is the price of '" + name + "'? "))
        prices.append(price)
        quantity = int(input("What is the quantity of " + name + "? "))
        quantities.append(quantity)
        print("'" + name + "' has been added to the cart.")

# Define a function to display the contents of the cart
def display_cart():
    print("The contents of the shopping cart are:")
    for i in range(len(names)):
        print(str(i + 1) + ". " + names[i] + " - $" + format(prices[i], '.2f') + " - Quantity: " + str(quantities[i]))

# Define a function to remove an item
def remove_item():
    display_cart()
    item_num = int(input("Which item would you like to remove? "))
    item_num -= 1  # convert to 0-based index
    if item_num < 0 or item_num >= len(names):
        print("Invalid choice.")
    else:
        if quantities[item_num] > 1:
            remove_quantity = int(input("Enter the quantity of " + names[item_num] + " to be removed: "))
            if remove_quantity > quantities[item_num]:
                print("Invalid quantity.")
            else:
                quantities[item_num] -= remove_quantity
                if quantities[item_num] == 0:
                    del names[item_num]
                    del prices[item_num]
                    del quantities[item_num]
                    print("Item removed.")
                else:
                    print(str(remove_quantity) + " quantities of " + names[item_num] + " has been removed.")
        else:
            del names[item_num]
            del prices[item_num]
            del quantities[item_num]
            print("Item removed.")


# Define a function to compute the total
def compute_total():
    total = sum(price*quantity for price,quantity in zip(prices, quantities))
    print("The total is $" + format(total, '.2f'))

# Main program loop
while True:
    choice = display_menu()
    if choice == 1:
        add_item()
    elif choice == 2:
        display_cart()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        compute_total()
    elif choice == 5:
        print("\nThank You, Come Again! (in an indian accent)")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


    """
    Added features:
    Allow the user to update the quantity of an item in the cart and specify the quantity of each item they want to add to the cart
        I created two new lists 'quantities' to store the quantity of each item, and in the 'add_item()' function I check if the item already 
        exists in the cart, if so I ask the user to update the quantity of the item, otherwise I add the item to the cart and ask the user 
        to enter the quantity of the item. In the 'display_cart()' function, I display the quantity of each item next to the name and price 
        and in the 'compute_total()' function, I compute the total by multiplying the price and quantity of each item and summing them up.
    
    Items displayed when removing an item and a feature that prompts the user to enter the quantity of an item they want to remove
        I added a check inside the 'remove_item()' function that checks if the item to be removed has more than 1 quantity. If it does, it prompts 
        the user to enter the quantity of the item they want to remove, then check if the entered quantity is valid (less than or equal to the 
        item's quantity in the cart). If it is, it subtracts the entered quantity from the item's quantity in the cart, if the item's quantity 
        becomes zero, it removes the item from the cart.
        Also, I added a check for the index of the item to be removed, to make sure that the index is within the bounds of the current list, 
        if the index is outside the bounds of the list, it will display a message informing the user that they have made an invalid choice.
    """