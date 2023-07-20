# Abstraction in Programming

Abstraction, as I understand it, refers to the process of simplifying something by ignoring certain details. Imagine a toy car with several switches and buttons. Some of them are necessary to get the car moving, while others are only for aesthetic purposes. It is simpler to operate the car if we simply pay attention to the important buttons and ignore the rest. This makes it simpler to comprehend a program's actions without becoming bogged down in its complex operations. It's like putting together a puzzle by focusing only on the big pieces first and then adding the small ones later. And understanding this can make code more modular, easier to understand and modify, and can lead to better performance.

## Abstraction in the Journal Program

A great example of abstraction in my Journal program is the creation of the Journal class, which manages the collection of entries. The class provides a simple interface for users to add entries to the journal, display entries, and save and load entries from a file, without requiring knowledge of the underlying list of Entry objects. Particularly, the `AddEntry`, `DisplayEntries`, `SaveToFile`, and `LoadFromFile` methods. These methods provide a high-level interface for users to interact with the journal, without needing to know how the methods are implemented.

## Abstraction in Displaying Moods

A further example is the `DisplayEntries` method, which converts the `Mood` property of each `Entry` object to a word for display, using a switch statement. This allows the user to view the mood of each entry without needing to know that the mood is stored as a number. This abstraction makes the code easier to read and understand and allows for easier modification in the future.

## Abstracting Adding Entries

Another example is the `AddEntry()` method. This method takes an `Entry` object as input and adds it to the `entries` list. Other parts of the program can call this method to add an entry without needing to know how the `entries` list is implemented or managed. Similarly, the `DisplayEntries()` method abstracts away the details of how the entries are formatted for display, allowing other parts of the program to simply call this method to display the entries.