############
# Solution #
############

"""
We can implement the stack data structure using a list in Python.
The undo_stack and redo_stack in the TextEditor class will be instances
of the Stack class. The insert operation will append the new text to
the text string and push the previous text onto the undo stack. The delete
operation will remove the last 'num_chars' characters from the text and push
the deleted text onto the undo stack. The undo operation will pop the last
operation from the undo stack and perform the reverse operation. The redo
operation will pop the last operation from the redo stack and perform the operation.
"""

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty list to store stack items

    def push(self, item):
        self.items.append(item)  # Add an item to the top of the stack

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()  # Remove and return the top item from the stack

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]  # Return the top item from the stack without removing it

    def is_empty(self):
        return len(self.items) == 0  # Check if the stack is empty


class TextEditor:
    def __init__(self):
        self.text = ""  # Initialize an empty string to store the text
        self.undo_stack = Stack()  # Create a stack for undo operations
        self.redo_stack = Stack()  # Create a stack for redo operations

    def insert(self, new_text):
        self.undo_stack.push(self.text)  # Push the current text to the undo stack
        self.text += new_text  # Append the new text to the existing text

    def delete(self, num_chars):
        deleted_text = self.text[-num_chars:]  # Retrieve the last num_chars characters from the text
        self.undo_stack.push(deleted_text)  # Push the deleted text to the undo stack
        self.text = self.text[:-num_chars]  # Remove the last num_chars characters from the text

    def undo(self):
        operation = self.undo_stack.pop()  # Pop the last operation from the undo stack
        if operation is not None:
            self.redo_stack.push(self.text)  # Push the current text to the redo stack
            self.text = operation  # Set the current text to the previous operation

    def redo(self):
        operation = self.redo_stack.pop()  # Pop the last operation from the redo stack
        if operation is not None:
            self.undo_stack.push(self.text)  # Push the current text to the undo stack
            self.text = operation  # Set the current text to the redo operation


# Test the TextEditor
editor = TextEditor()
editor.insert("Hello,")
editor.insert(" World!")
print(editor.text)  # Output: Hello, World!

editor.delete(6)
print(editor.text)  # Output: Hello

editor.undo()
print(editor.text)  # Output: Hello, World!

editor.redo()
print(editor.text)  # Output: Hello!









