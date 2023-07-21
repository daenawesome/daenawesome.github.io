# Initialize lists to store account names and balances
account_names = []
account_balances = []

# Loop to ask for account name and balance
while True:
    account_name = input("What is the name of this account? ")
    if account_name == "quit":
        break
    account_balance = float(input("What is the balance? "))
    account_names.append(account_name)
    account_balances.append(account_balance)

# Loop through the lists using an index and display account names with balances
for i in range(len(account_names)):
    print(f"{account_names[i]} - ${account_balances[i]:.2f}")

# Compute and display total balance and average balance
total_balance = sum(account_balances)
average_balance = total_balance / len(account_balances)
print(f"\nTotal: ${total_balance:.2f}")
print(f"Average: ${average_balance:.2f}")


"""
creates two empty lists, one for the names of the bank accounts and one for the balances. 
Then, it enters a while loop that keeps asking the user for account names and balances until 
the user types "quit". For each account, the name and balance are added to the appropriate list. 
After the user is done entering accounts, the code enters another loop that goes through the 
lists using an index and displays the name of the account with the balance next to it. Finally, 
it computes and displays the total balance in all of the accounts and the average balance.
"""