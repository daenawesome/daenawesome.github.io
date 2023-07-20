using System;
using System.Collections.Generic;

public class Scripture
{
    // private fields
    private string reference; // a string that represents the reference of the scripture
    private List<Verse> verses; // a list of Verse objects that represents the verses of the scripture

    // public properties
    public List<Verse> GetVerses() // returns the list of Verse objects
    {
        return verses;
    }

    public string GetReference() // returns the reference of the scripture
    {
        return reference;
    }

    // constructors
    public Scripture(string reference, string text) // constructor that takes a reference and a text
    {
        this.reference = reference; // sets the reference field to the given reference
        verses = new List<Verse>(); // initializes the verses list
        verses.Add(new Verse(reference, text)); // creates a new Verse object with the given reference and text, and adds it to the verses list
    }

    public Scripture(string reference, string[] texts) // constructor that takes a reference and an array of texts
    {
        this.reference = reference; // sets the reference field to the given reference
        verses = new List<Verse>(); // initializes the verses list
        for (int i = 0; i < texts.Length; i++) // iterates through each text in the texts array
        {
            verses.Add(new Verse(reference, texts[i])); // creates a new Verse object with the given reference and text, and adds it to the verses list
        }
    }

    // methods
    public void HideRandomWords(int numWordsToHide) // method that takes a number of words to hide, and hides that many words in each verse of the scripture
    {
        foreach (Verse verse in verses) // iterates through each verse in the verses list
        {
            verse.HideRandomWords(numWordsToHide); // calls the HideRandomWords method of the Verse object, passing in the numWordsToHide parameter
        }
    }

    public bool IsFullyHidden() // method that checks if all the words in all the verses of the scripture are hidden
    {
        foreach (Verse verse in verses) // iterates through each verse in the verses list
        {
            if (!verse.IsFullyHidden()) // if the verse is not fully hidden
            {
                return false; // return false
            }
        }
        return true; // if all the verses are fully hidden, return true
    }

    public void Print() // method that clears the console and prints each verse of the scripture
    {
        Console.Clear(); // clears the console
        foreach (Verse verse in verses) // iterates through each verse in the verses list
        {
            Console.WriteLine(verse.ToString()); // calls the ToString method of the Verse object, and writes the result to the console
        }
    }
}
