###########
# Problem #
###########

"""
Implement a friend suggestion feature based on shared interests.
You are tasked with implementing a friend suggestion feature for your social media application. 
The goal is to suggest friends to users based on their shared interests.
For extra points, try adding your name in the data base with the following interest "birdwatching, coding, movies, yoga, painting" and use the function to suggest 1 friend based on shared interest.
"""

# 1. Define the `user_database` dictionary
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
    # Implement your solution here
    
    # ### Instructions for the `suggest_friends` function:
    # - Step 1: Get the interests of the target user
    #     - Retrieve the interests associated with the `user_id` from the `user_database`. If the `user_id` is not found in the database, return an empty set.

    # - Step 2: Calculate the intersection of interests with other users
    #     - Iterate over each user in the `user_database` (excluding the target user) and calculate the intersection of their interests with the target user's interests.
    #     - Append a tuple `(user, num_common_interests)` to the `suggestions` list.

    # - Step 3: Sort the suggestions based on the number of common interests using a lambda function
    #     - Sort the `suggestions` list based on the second element of each tuple, which represents the number of common interests. Sort the list in descending order.

    # - Step 4: Extract the suggested friends from the sorted list
    #     - Use list comprehension to extract the user IDs from the sorted `suggestions` list.
    #     - Select only the desired number of suggestions specified by the `num_suggestions` parameter.
    
    return suggested_friends


# Example usage:
suggested_friends = suggest_friends("John", 3) 
print(suggested_friends) # Output:['Alex', 'Sam', 'Emma']
# In this example, the function suggests three friends for the user with the ID "John" based on their shared interests.
