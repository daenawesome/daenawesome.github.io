# Create empty lists for storing the names and prices of the items
names = []
prices = []

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
    names.append(name)
    price = float(input("What is the price of '" + name + "'? "))
    prices.append(price)
    print("'" + name + "' has been added to the cart.")

# Define a function to display the contents of the shopping cart
def display_cart():
    print("\nThe contents of the shopping cart are:")
    for i in range(len(names)):
        print(str(i + 1) + ". " + names[i] + " - $" + str(prices[i]))

# Define a function to remove an item 
def remove_item():
    number = int(input("Enter the number of the item you want to remove: "))
    index = number - 1
    if index >= 0 and index < len(names):
        name = names.pop(index)
        price = prices.pop(index)
        print("\n'" + name + "' has been removed from the cart.")
    else:
        print("Invalid choice. The item number is out of range.")

# Define a function to compute the total
def compute_total():
    total = sum(prices)
    print("\nThe total is $" + str(total))

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
        print("\nThank You, Come Again!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    """
    This has feature to add price, calculate price or remove an item
    """