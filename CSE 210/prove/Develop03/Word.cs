using System;

public class Word
{
    private string value;
    private bool hidden;

    // Constructor for the Word class
    public Word(string value)
    {
        this.value = value;
        hidden = false;
    }

    // Getter method for the value of the word
    public string GetValue()
    {
        return value;
    }

    // Getter method for the hidden status of the word
    public bool IsHidden()
    {
        return hidden;
    }

    // Hides the word if it is not already hidden
    public void Hide()
    {
        if (!hidden)
        {
            hidden = true;
        }
    }

    // Reveals the word if it is hidden
    public void Reveal()
    {
        if (hidden)
        {
            hidden = false;
        }
    }

    // Returns a string representation of the word, either the word or its hidden status
    public override string ToString()
    {
        if (hidden)
        {
            // If the word is hidden, return underscores instead of the word
            return new string('_', value.Length);
        }
        else
        {
            // Otherwise, return the word itself
            return value;
        }
    }
}
