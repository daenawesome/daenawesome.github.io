# Create an empty list to store the shopping list items
shopping_list = []

# Instruction for the user
print("Please enter the items of the shopping list (type: 'quit' to finish)")

# Function to add a new item to the shopping list
def add_item(item):
    shopping_list.append(item)
   # print(f"{item} has been added to the shopping list.")

# Ask the user for a list of items
while True:
    item = input("Item: ")
    if item == "quit":
        break
    add_item(item)

# Print the initial shopping list
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

# Print the shopping list with indexes
print("\nThe shopping list with indexes is:")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")

# Ask the user for an index and a new item
while True:
    try:
        index = int(input("\nWhich item would you like to change? "))
        if index < 0 or index >= len(shopping_list):
            raise ValueError
        new_item = input("What is the new item? ")
        shopping_list[index] = new_item
        break
    except ValueError:
        print("Invalid index. Please enter a valid number.")

# Print the updated shopping list with indexes
print("\nThe updated shopping list with indexes is:")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")
