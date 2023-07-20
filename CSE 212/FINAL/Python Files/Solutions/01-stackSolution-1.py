############
# Solution #
############

"""
We can solve this problem using a stack. Whenever we encounter an opening parenthesis,
we push it onto the stack. If we encounter a closing parenthesis, we check if the stack
is empty. If it is empty, it means the parentheses are not balanced, so we return False.
Otherwise, we pop an opening parenthesis from the stack, indicating that we have found
a matching pair. At the end, if the stack is empty, it means all parentheses are balanced.
"""

def is_balanced(parentheses):
    # Initialize an empty stack to store opening parentheses
    stack = []

    # Iterate through each character in the input parentheses string
    for char in parentheses:
        # If the character is an opening parenthesis '(', push it onto the stack
        if char == '(':
            stack.append(char)
        # If the character is a closing parenthesis ')'
        elif char == ')':
            # Check if the stack is empty, which means there is no corresponding opening parenthesis
            if len(stack) == 0:
                return False
            # Pop the topmost opening parenthesis from the stack, as it has found a corresponding closing parenthesis
            stack.pop()

    # After iterating through all characters, check if the stack is empty
    # If it's empty, that means all opening parentheses have their corresponding closing parentheses
    # If it's not empty, there are some unbalanced parentheses
    return len(stack) == 0

# Test the function
print(is_balanced("((()))"))  # Output: True
print(is_balanced("()()()"))  # Output: True
print(is_balanced("((())"))   # Output: False
