###########
# Problem #
###########

"""
You are implementing a text editor that supports undo and redo operations.
Implement the classes 'TextEditor' and 'Stack' to enable these operations.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Implement your solution here
        pass

    def pop(self):
        # Implement your solution here
        pass

    def peek(self):
        # Implement your solution here
        pass

    def is_empty(self):
        # Implement your solution here
        pass

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def insert(self, new_text):
        # Implement your solution here
        pass

    def delete(self, num_chars):
        # Implement your solution here
        pass

    def undo(self):
        # Implement your solution here
        pass

    def redo(self):
        # Implement your solution here
        pass

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
