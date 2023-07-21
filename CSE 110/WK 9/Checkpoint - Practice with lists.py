print("Type 'end' to finnish the list. \n")

# Create an empty list to store the names of friends
friends = []

# Ask the user for the name of a friend
while True:
    friend = input("Type the name of a friend: ")
    # Check if the name is "end"
    if friend.lower() == "end":
        break
    # If the name is not "end", add it to the list of friends
    friends.append(friend)

# Display the list of friends
print("\nYour friends are:")
for friend in friends:
    print(friend)


"""
a while loop that continues to ask the user for the name of a friend, 
until the user types "end". Inside the loop, it checks if the name is "end" 
using the 'lower()' method to make the comparison case-insensitive. If the 
name is not "end", it is added to the list of friends. After the loop, the 
program uses another for loop to display each friend in the list.
"""