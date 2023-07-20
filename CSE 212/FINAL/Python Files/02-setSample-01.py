"""
You are working as a data analyst for a social media marketing agency. 
Your task is to analyze the followers of various social media influencers 
and identify potential collaborations for a client's new product launch. 
The influencers' followers are stored in sets, representing unique user IDs.

Your goal is to find users who are following multiple influencers, 
as they are likely to have a higher influence on social media. 
Additionally, you need to identify users who are following only one influencer, 
as they might be interested in collaborating with your client.
"""

# Define sets of followers for each influencer
Helaman_followers = {'Kishkumen486', 'Mathoni512', 'Shimnilom534', 'Chemish555'}
Alma_followers = {'Shimnilom534', 'Chemish555', 'Shemlon570', 'Aha595'}
Nephi_followers = {'Shimnilom534', 'Aha595', 'Irijah601', 'Giddianhi440'}

# Merge all followers into a single set using the union operator |
all_followers = Helaman_followers | Alma_followers | Nephi_followers

# Find the users who are following all three influencers using the intersection operator &
following_multiple = Helaman_followers & Alma_followers & Nephi_followers

# Find the users who are following only one influencer by using the symmetric difference operator ^
# and subtracting the set of users who are following multiple influencers
following_single = (Helaman_followers ^ Alma_followers ^ Nephi_followers) - following_multiple

# Print the users who are following multiple influencers
print("Users following multiple influencers:", following_multiple)

# Print the users who are following only one influencer
print("Users following only one influencer:", following_single)
