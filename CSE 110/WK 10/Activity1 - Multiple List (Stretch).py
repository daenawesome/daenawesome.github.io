# create empty lists for account names and balances
account_names = []
account_balances = []

# loop to ask for account name and balance
while True:
    name = input("What is the name of this account? ")
    if name == "quit":
        break
    balance = float(input("What is the balance? "))

    # add account name and balance to the lists
    account_names.append(name)
    account_balances.append(balance)

# find the highest balance and its index
highest_balance = max(account_balances)
highest_index = account_balances.index(highest_balance)
highest_name = account_names[highest_index]

# display account information
print("Account Information:")
for i in range(len(account_names)):
    print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")

# display total and average balance
total = sum(account_balances)
average = total / len(account_balances)
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

# update account loop
while True:
    update = input("Do you want to update an account? ")
    if update == "no":
        break
    elif update == "yes":
        index = int(input("What account index do you want to update? "))
        new_balance = float(input("What is the new amount? "))
        account_balances[index] = new_balance
        print("Account Information:")
        for i in range(len(account_names)):
            print(f"{i}. {account_names[i]} - ${account_balances[i]:.2f}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
