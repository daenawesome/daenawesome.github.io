# Initialize lists to store names and balances of bank accounts
account_names = []
account_balances = []

# Instruction for the user
print("Enter the names and balances of bank accounts (type: 'quit' when done)")

while True:
    # Ask for the name of the account
    account_name = input("What is the name of this account? ")
    # Check if user wants to quit
    if account_name.lower() == "quit":
        break
    # Ask for the balance of the account
    while True:
        try:
            account_balance = float(input("What is the balance? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Append the name and balance to the appropriate lists
    account_names.append(account_name)
    account_balances.append(account_balance)

# Display the account information
print("\nAccount Information:")
for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

# Compute and display the total balance and average balance
total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances)
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")

# Determine and display the account with the highest balance
highest_index = account_balances.index(max(account_balances))
highest_account = account_names[highest_index]
highest_balance = account_balances[highest_index]
print(f"Highest balance: {highest_account} - ${highest_balance:.2f}")

# Ask the user if they want to update an account
while True:
    update_response = input("\nDo you want to update an account? ")
    if update_response.lower() == "no":
        print("\nAccount Information:")
        for i in range(len(account_names)):
            print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
        break
    elif update_response.lower() == "yes":
        while True:
            try:
                account_index = int(input("What account index do you want to update? "))
                if account_index >= 0 and account_index < len(account_names):
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Ask the user for the new balance
        while True:
            try:
                new_balance = float(input("What is the new amount? "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Update the account balance
        account_balances[account_index] = new_balance
        # Display the updated account information
        print("\nAccount Information:")
        for i in range(len(account_names)):
            print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


    """
    Added:
     input validation and error handling 
    """