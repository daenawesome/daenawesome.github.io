using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main(string[] args)
    {
        // create a list to hold the scriptures
        List<Scripture> scriptures = new List<Scripture>();

        // get all text files in current directory with extension .txt
        string[] files = Directory.GetFiles(".", "*.txt");

        // if no files found, display a message and return
        if (files.Length == 0)
        {
            Console.WriteLine("No text files found in current directory.");
            return;
        }

        // display a list of files and prompt the user to choose one
        Console.WriteLine("Select a file to load:");
        for (int j = 0; j < files.Length; j++)
        {
            Console.WriteLine($"{j + 1}. {Path.GetFileName(files[j])}");
        }
        Console.Write(">> ");
        int fileIndex = int.Parse(Console.ReadLine()) - 1;

        // if the user entered an invalid selection, display a message and return
        if (fileIndex < 0 || fileIndex >= files.Length)
        {
            Console.WriteLine("Invalid selection.");
            return;
        }

        // read the selected file
        string[] lines = File.ReadAllLines(files[fileIndex]);
        int i = 0;
        while (i < lines.Length)
        {
            string line = lines[i].Trim();
            if (line.StartsWith("#"))
            {
                // if the line starts with #, it is a scripture reference
                string reference = line.Substring(1).Trim();
                List<string> texts = new List<string>();
                i++;
                while (i < lines.Length && !lines[i].StartsWith("#"))
                {
                    // add each line of text to the texts list
                    texts.Add(lines[i].Trim());
                    i++;
                }
                // create a new scripture object with the reference and texts, and add it to the scriptures list
                scriptures.Add(new Scripture(reference, texts.ToArray()));
            }
            else
            {
                // if the line doesn't start with #, skip it
                i++;
            }
        }

        // create a Random object to generate random numbers
        Random random = new Random();

        // display a menu to choose the difficulty level
        Console.Clear();
        Console.WriteLine("Select a difficulty level:");
        Console.WriteLine("1. Easy (1 hidden word per verse)");
        Console.WriteLine("2. Medium (3 hidden words per verse)");
        Console.WriteLine("3. Hard (5 or more hidden words per verse)");
        Console.Write(">> ");
        int difficulty = int.Parse(Console.ReadLine());

        // determine the number of words to hide based on the difficulty level
        int wordsToHide = 1;
        if (difficulty == 2)
        {
            wordsToHide = 3;
        }
        else if (difficulty == 3)
        {
            wordsToHide = 5;
        }

        // loop indefinitely
        while (true)
        {
            Console.WriteLine();
            Console.WriteLine("Do you want to shuffle the scripture verse before displaying it? (y/n)");
            Console.Write(">> ");
            string shuffleInput = Console.ReadLine();
            while (shuffleInput.ToLower() != "y" && shuffleInput.ToLower() != "n")
            {
                Console.WriteLine("Invalid input. Please enter 'y' or 'n'.");
                Console.Write(">> ");
                shuffleInput = Console.ReadLine();
            }
            bool shuffle = (shuffleInput.ToLower() == "y");
    
            Scripture scripture = scriptures[random.Next(scriptures.Count)];
    
            if (shuffle)
            {
                foreach (Verse verse in scripture.GetVerses())
                {
                    verse.ShuffleWords();
                }
            }

            // loop until all the words in the current scripture are hidden
            while (!scripture.IsFullyHidden())
            {
                // print the current scripture with hidden words
                scripture.Print();
                Console.WriteLine();

                // prompt the user to input their choice
                Console.WriteLine("Press enter to continue, type 'quit' to exit, or type 'shuffle' to shuffle the words.");
                Console.Write(">> ");
                string input = Console.ReadLine();

                // if the user enters 'quit', exit the program
                if (input.ToLower() == "quit")
                {
                    return;
                }
                // if the user enters 'shuffle', shuffle the words in each verse of the scripture and reprint it
                else if (input.ToLower() == "shuffle")
                {
                    shuffle = true;
                    foreach (Verse verse in scripture.GetVerses())
                    {
                        verse.ShuffleWords();
                    }
                }
                // if the user enters anything else, hide a random number of words and reprint the scripture
                else
                {
                    shuffle = false;
                    scripture.HideRandomWords(wordsToHide);
                }
            }

            // clear the console screen to prepare for displaying the next scripture and display a message to congratulate the user
            Console.Clear();
            Console.WriteLine("Nice Work on: " + scripture.GetReference());
            Console.WriteLine("Press enter to proceed to the next scripture or type 'quit' to exit.");
            Console.Write(">> ");
            string endInput = Console.ReadLine();
            if (endInput.ToLower() == "quit") // if the input is "quit", exit the program using the return statement.
            {
                return;
            }

            

        }
    }

}



