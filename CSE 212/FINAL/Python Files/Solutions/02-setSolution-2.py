############
# Solution #
############

"""
To implement the friend suggestion feature based on shared interests, 
you can follow these steps:
"""

# 1. Define the user_database: This step is already provided in the problem statement.
user_database = {
    "Shiblon": {"music", "movies", "reading", "photography", "cooking", "painting", "hiking", "yoga", "writing", "gardening"},
    "Gadianton": {"sports", "movies", "travel", "painting", "hiking", "photography", "baking", "dancing", "volunteering", "yoga"},
    "Zoram": {"music", "movies", "gaming", "coding", "swimming", "reading", "painting", "traveling", "photography", "singing"},
    "Abinadom": {"reading", "cooking", "yoga", "writing", "gardening", "dancing", "photography", "sculpting", "meditation", "knitting"},
    "Zeezrom": {"sports", "music", "photography", "dancing", "running", "hiking", "cooking", "painting", "cycling", "yoga"},
    "Pahoran": {"cooking", "travel", "painting", "movies", "birdwatching", "scuba diving", "gardening", "photography", "hiking", "playing"},
    "Teancum": {"surfing", "pottery", "chess", "calligraphy", "archery", "salsa", "knitting", "skydiving", "origami", "woodworking"}
}

# 2. Define the `suggest_friends` function:
def suggest_friends(user_id, num_suggestions):
    # Step 3: Get the interests of the target user
    target_interests = user_database.get(user_id, set())
    # This line retrieves the interests associated with the user_id from the user_database. If the user_id is not found in the database, it returns an empty set.

    # Step 4: Calculate the intersection of interests with other users
    suggestions = []
    for user, interests in user_database.items():
        if user != user_id:
            common_interests = interests.intersection(target_interests)
            suggestions.append((user, len(common_interests)))
    # This loop iterates over each user in the user_database and calculates the intersection of their interests with the target user's interests. It appends a tuple `(user, num_common_interests)` to the `suggestions` list.

    # Step 5: Sort the suggestions based on the number of common interests using a lambda function
    suggestions.sort(key=lambda x: x[1], reverse=True)
    # This line sorts the `suggestions` list based on the second element of each tuple, which represents the number of common interests. The `reverse=True` parameter sorts the list in descending order.

    # Step 6: Extract the suggested friends from the sorted list
    suggested_friends = [user for user, _ in suggestions[:num_suggestions]]
    # This line uses a list comprehension to extract the user IDs from the sorted `suggestions` list. It only selects the desired number of suggestions specified by the `num_suggestions` parameter.

    return suggested_friends
    # Finally, the `suggest_friends` function returns the `suggested_friends` list, which contains the user IDs of the suggested friends.

# Example usage:
suggested_friends = suggest_friends("John", 3) 
print(suggested_friends) # Output:['Alex', 'Sam', 'Emma']
# In this example, the function suggests three friends for the user with the ID "John" based on their shared interests.

# Extra points
# Include your name in the database with the specified interests
user_database["Daen"] = {"birdwatching", "coding", "movies", "yoga", "painting"}
suggested_friends = suggest_friends("Daen", 5)
print(suggested_friends)
