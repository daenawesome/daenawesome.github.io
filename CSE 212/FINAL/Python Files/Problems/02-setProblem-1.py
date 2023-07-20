###########
# Problem #
###########

"""
Word Analysis
You are given a function called `count_unique_words(text)` that takes a string `text` as input. 
The function analyzes the text and returns the following information about the words in the text:
- The number of unique words
- The number of duplicate words
- The number of non-unique words (total words minus unique words)

Implement the `count_unique_words(text)` function to correctly analyze the text and return the required information.
Additionally, you need to test the function using the provided `scripture_text` and print the following:
- The number of unique words
- The number of duplicate words
- The number of non-unique words
- The total number of words (sum of unique, duplicate, and non-unique words)

Note:
The function should consider words as case-insensitive. For example, "Hello" and "hello" should be treated as the same word.
The order of the words does not matter.
The same word appearing multiple times should be counted only once.A word is defined as a continuous sequence of alphabetic characters (a-z, A-Z). Any non-alphabetic character should be considered as a word separator.
You must use a set data structure to store the unique words encountered in the text file.
Implement the function efficiently, considering large text files.
Your solution should use set methods extensively to solve this problem.
"""

def count_unique_words(text):
    # Implement your solution here
    pass

# Test the function with the following text
scripture_text = """
After I had retired to the place where I had previously designed to go, having looked around me, and finding myself alone, I kneeled down and began to offer up the desires of my heart to God. I had scarcely done so, when immediately I was seized upon by some power which entirely overcame me, and had such an astonishing influence over me as to bind my tongue so that I could not speak. Thick darkness gathered around me, and it seemed to me for a time as if I were doomed to sudden destruction.
But, exerting all my powers to call upon God to deliver me out of the power of this enemy which had seized upon me, and at the very moment when I was ready to sink into despair and abandon myself to destruction—not to an imaginary ruin, but to the power of some actual being from the unseen world, who had such marvelous power as I had never before felt in any being—just at this moment of great alarm, I saw a pillar of light exactly over my head, above the brightness of the sun, which descended gradually until it fell upon me.
It no sooner appeared than I found myself delivered from the enemy which held me bound. When the light rested upon me I saw two Personages, whose brightness and glory defy all description, standing above me in the air. One of them spake unto me, calling me by name and said, pointing to the other—This is My Beloved Son. Hear Him!
My object in going to inquire of the Lord was to know which of all the sects was right, that I might know which to join. No sooner, therefore, did I get possession of myself, so as to be able to speak, than I asked the Personages who stood above me in the light, which of all the sects was right (for at this time it had never entered into my heart that all were wrong)—and which I should join.
I was answered that I must join none of them, for they were all wrong; and the Personage who addressed me said that all their creeds were an abomination in his sight; that those professors were all corrupt; that: "they draw near to me with their lips, but their hearts are far from me, they teach for doctrines the commandments of men, having a form of godliness, but they deny the power thereof." 
He again forbade me to join with any of them; and many other things did he say unto me, which I cannot write at this time. When I came to myself again, I found myself lying on my back, looking up into heaven. When the light had departed, I had no strength; but soon recovering in some degree, I went home. And as I leaned up to the fireplace, mother inquired what the matter was. I replied, "Never mind, all is well—I am well enough off." I then said to my mother, "I have learned for myself that Presbyterianism is not true." It seems as though the adversary was aware, at a very early period of my life, that I was destined to prove a disturber and an annoyer of his kingdom; else why should the powers of darkness combine against me? Why the opposition and persecution that arose against me, almost in my infancy?
"""

unique_count, duplicate_count, non_unique_count = count_unique_words(scripture_text)
print("Number of unique words:", unique_count)
print("Number of duplicate words:", duplicate_count)
print("Number of non-unique words:", non_unique_count)
print("Total number of words:", unique_count + duplicate_count + non_unique_count)

# Hint:
# You can use the `splitlines()` method to split the text into lines 
# and the `split()` method to split each line into words. 
# Keep track of the unique and duplicate words using sets, 
# and calculate the word counts accordingly.
