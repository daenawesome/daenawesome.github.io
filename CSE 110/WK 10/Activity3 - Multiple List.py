# Create two lists, one for the names of the bank accounts, and one for the balances
account_names = []
account_balances = []

# Instruction for the user
print("Enter the names and balances of bank accounts (type: 'quit' when done)")

# Ask the user for the name of the bank account and then for its current balance
while True:
    account_name = input("Account Name: ")
    if account_name == "quit":
        break
    account_balance = float(input("Balance: "))
    account_names.append(account_name)
    account_balances.append(account_balance)

# Loop through the lists using an index and display the name of the account with the balance next to it
print("\nAccount Information:")
for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

# Compute and display the total balance in all of the accounts and the average balance
total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances)
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")

# Determine which bank account has the highest balance and display the name and balance of that account
highest_balance = max(account_balances)
highest_index = account_balances.index(highest_balance)
print(f"Highest balance: {account_names[highest_index]} - ${highest_balance:.2f}")

# Ask the user if they want to update an account
while True:
    # Ask the user if they want to update an account
    update_account = input("Do you want to update an account? ")
    if update_account.lower() == "no":
        print("\nAccount Information:")
        for i, account in enumerate(account_names):
            print(f"{i}. {account} - ${account_balances[i]:.2f}")
        break
    elif update_account.lower() == "yes":
        # Ask the user for the index of the account to update
        update_index = int(input("What account index do you want to update? "))
        # Validate the index is within the range of existing accounts
        if update_index >= 0 and update_index < len(account_names):
            # Ask the user for the new balance
            new_balance = float(input("What is the new amount? "))
            # Validate the new balance is a positive number
            if new_balance > 0:
                # Update the balance of the selected account
                account_balances[update_index] = new_balance
                # Display the updated account information
                print("\nAccount Information:")
                for i, account in enumerate(account_names):
                    print(f"{i}. {account} - ${account_balances[i]:.2f}")
        else:
            print("Invalid account index.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


    """
    This code will run in a loop and repeatedly ask the user if they want to update an account. 
    If the user enters "yes", it will then ask the user for the index of the account they want to update, 
    validate that the index is within the range of existing accounts, and then ask for the new balance. 
    If the new balance is a positive number, it will update the selected account and display the updated 
    account information. If the user enters "no", it will break out of the loop and end the program. 
    If the user enters any other input, it will prompt them to enter either "yes" or "no". 
    
    The code also includes input validation for invalid input index or invalid input balance.
    """