# Encapsulation in Programming

Encapsulation is a fundamental concept in programming that allows the important sections of a program's code to be concealed from other parts that don't need to know about them. It is similar to a secret code, where only specific portions of the program are allowed to communicate with one another while the rest are kept secret and concealed. Encapsulation is like having a locked box, where you pack items inside and lock it, ensuring that only you have access to what's inside. This concept provides several advantages, including clear separation of concerns and ease of maintenance.

## The "Word" Class Example

Let's explore an example of how encapsulation is used in a class called "Word." In this class, two private attributes, "text" and "hidden," are defined, which can only be accessed through the class's public methods. Here's the code for the "Word" class:

```csharp
public class Word
{
    private string text;
    private bool hidden;

    public Word(string text)
    {
        this.text = text;
        hidden = false;
    }

    public bool IsHidden()
    {
        return hidden;
    }

    public void Hide()
    {
        hidden = true;
    }

    public override string ToString()
    {
        if (hidden)
        {
            return "_____";
        }
        else
        {
            return text;
        }
    }
}
```

### Explanation

In the "Word" class, the internal state is encapsulated by declaring the "text" and "hidden" attributes as private. This means that these attributes cannot be accessed or modified from outside the class, providing security and protection from external interference.

The constructor of the class initializes the "text" attribute with the provided input text and sets the "hidden" attribute to false initially.

- The `Hide` method is a public method that changes the value of the "hidden" attribute to true, effectively hiding the word.
- The `IsHidden` method is also public and allows external code to query whether the word is currently hidden or not.
- The `ToString` method overrides the default behavior and uses the "hidden" attribute to either return the actual word if it's not hidden, or a series of underscores if it is hidden.

By encapsulating the internal state of the "Word" class, we ensure that only the class's public methods can interact with and modify its attributes, maintaining data integrity and providing a clean and isolated interface for other parts of the program to work with the "Word" objects.