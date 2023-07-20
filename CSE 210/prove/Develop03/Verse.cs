using System;
using System.Collections.Generic;

public class Verse
{
    private string reference; // The reference of the verse, e.g. "John 3:16"
    private List<Word> words; // A list of words in the verse

    public Verse(string reference, string text)
    {
        this.reference = reference;
        words = new List<Word>(); // Initialize an empty list of words
        foreach (string word in text.Split(' ')) // Split the input text into words
        {
            words.Add(new Word(word)); // Add each word to the list of words
        }
    }

    public void HideRandomWords(int numWordsToHide)
    {
        List<int> visibleIndices = new List<int>(); // Initialize a list of visible word indices
        for (int i = 0; i < words.Count; i++)
        {
            if (!words[i].IsHidden()) // If the word is not already hidden
            {
                visibleIndices.Add(i); // Add the index of the word to the list of visible indices
            }
        }
        if (visibleIndices.Count > 0) // If there are visible words to hide
        {
            Random random = new Random(); // Initialize a random number generator
            for (int i = 0; i < numWordsToHide; i++)
            {
                int indexToHide = visibleIndices[random.Next(visibleIndices.Count)]; // Choose a random visible index to hide
                words[indexToHide].Hide(); // Hide the word at the chosen index
                visibleIndices.Remove(indexToHide); // Remove the hidden word index from the list of visible indices
                if (visibleIndices.Count == 0) // If there are no more visible words
                {
                    break; // Exit the loop
                }
            }
        }
    }

    public bool IsFullyHidden()
    {
        foreach (Word word in words) // Loop through all words in the verse
        {
            if (!word.IsHidden()) // If a word is not hidden
            {
                return false; // The verse is not fully hidden
            }
        }
        return true; // All words are hidden, so the verse is fully hidden
    }

    public override string ToString()
    {
        string output = reference + ": "; // Start the output string with the reference
        foreach (Word word in words) // Loop through all words in the verse
        {
            output += word.ToString() + " "; // Add the string representation of the word to the output string, followed by a space
        }
        return output; // Return the output string
    }

    public void ShuffleWords()
    {
        Random random = new Random(); // Initialize a random number generator
        words = words.OrderBy(x => random.Next()).ToList(); // Shuffle the list of words using the random number generator
    }
}
