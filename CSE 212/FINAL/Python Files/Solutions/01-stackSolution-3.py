############
# Solution #
############

"""
First, define the `Stack` class with the `push`, `pop`, and `is_empty` methods. 
Implement the `push` method to add an item to the stack's list of items. 
Next, implement the `pop` method to remove and return the last item from the stack's list, checking if the list is empty beforehand. 
Then, implement the `is_empty` method to check if the stack is empty by examining the size of the items list. 
Moving on to the `reverse_words_in_phrase` function, start by creating an empty string called `reversed_phrase` to store the reversed words. 
Create an instance of the `Stack` class called `word_stack`. Split the input `phrase` into a list of words. 
Iterate over each word, pushing each character onto `word_stack`. Create an empty string called `reversed_word` to store the reversed word. 
While `word_stack` is not empty, pop each character and append it to `reversed_word`. Append the `reversed_word` to `reversed_phrase`, adding a space after it. 
Finally, return the `reversed_phrase` string, excluding the trailing space.
"""

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store the items in the stack

    def push(self, item):
        self.items.append(item)  # Add the item to the top of the stack

    def pop(self):
        if not self.is_empty():  # Check if the stack is not empty
            return self.items.pop()  # Remove and return the topmost item from the stack
        else:
            return None  # If the stack is empty, return None

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty


def reverse_words_in_phrase(phrase):
    words = phrase.split()  # Split the phrase into a list of words
    reversed_words = []  # Initialize an empty list to store the reversed words
    stack = Stack()  # Create a new instance of the Stack class

    # Iterate over each word in the list
    for word in words:  
        for char in word:  # Iterate over each character in the word
            stack.push(char)  # Push each character onto the stack
        
        # Initialize an empty string to store the reversed word
        reversed_word = ''  
        while not stack.is_empty():  # While the stack is not empty
            reversed_word += stack.pop()  # Pop each character from the stack and append it to the reversed word
        
        # Add the reversed word to the list of reversed words
        reversed_words.append(reversed_word)  

    # Join the reversed words with a space in between to form the reversed phrase
    reversed_phrase = ' '.join(reversed_words)  
    return reversed_phrase


# Test the code
phrase = "flow maws speed did mood"
reversed_phrase = reverse_words_in_phrase(phrase)
print(reversed_phrase)

