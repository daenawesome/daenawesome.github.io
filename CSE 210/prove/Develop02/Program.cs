using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace DailyJournal
{
    // Define the Entry class to store each journal entry
    class Entry
    {
        public string Prompt { get; set; }
        public string Response { get; set; }
        public DateTime Date { get; set; }
        public string Mood { get; set; }
        public int WordCount { get; set; }
    }

    // Define the Journal class to manage the collection of entries
    class Journal
    {
        private List<Entry> entries;

        // Constructor to create a new, empty journal
        public Journal()
        {
            entries = new List<Entry>();
        }

        // Add a new entry to the journal
        public void AddEntry(Entry entry)
        {
            // Count the number of words in the user's response
            int wordCount = entry.Response.Split(new char[] { ' ', '.', '?' }, StringSplitOptions.RemoveEmptyEntries).Length;

            // Set the word count in the entry object
            entry.WordCount = wordCount;
            
            entries.Add(entry); // Add the new entry to the list
        }

        // Display all the entries in the journal
        public void DisplayEntries()
        {
            foreach (var entry in entries)
            {
                // Convert the mood number to a mood word for display
                var moodWord = entry.Mood switch
                {
                    "1" => "Happy",
                    "2" => "Sad",
                    "3" => "Excited",
                    "4" => "Bored",
                    "5" => "Angry",
                    _ => "Unknown",
                };

                // Display the entry properties
                Console.WriteLine($"Mood: {moodWord}");
                Console.WriteLine($"Prompt: {entry.Prompt}");
                Console.WriteLine($"Response: {entry.Response}");
                Console.WriteLine($"Date: {entry.Date:yyyy-MM-dd HH:mm:ss}");
                Console.WriteLine($"Words: {entry.WordCount}");
                Console.WriteLine();
            }
        }

        // Save all the entries in the journal to a file
        public void SaveToFile(string filename)
        {
            char[] invalidChars = Path.GetInvalidFileNameChars(); 

            filename = filename.EndsWith(".json") ? filename : $"{filename}.json"; // Save with '.json'

            bool fileExists;
            
            do
            {
                fileExists = File.Exists(filename);

                if (fileExists)
                {
                    Console.WriteLine($"File {filename} already exists. Do you want to overwrite it? (y/n)");
                    Console.Write(">> ");
                    string input = Console.ReadLine();
                    if (input.ToLower() == "y")
                    {
                        File.Delete(filename); // Delete the existing file
                        fileExists = false;
                    }
                    else if (input.ToLower() == "n")
                    {
                        filename = GetValidFileName();
                        fileExists = File.Exists(filename);
                    }
                    else
                    {
                        Console.WriteLine("Invalid input. Please enter 'y' or 'n'");
                    }
                }
            } while (fileExists);

            if (entries?.Count == 0) // Check if there are any entries in the journal
            {
                Console.WriteLine("Journal is empty. Cannot save an empty journal.");
                return;
            }

            // Create a list of entries with the word count included
            var entriesWithWordCount = entries.Select(entry => new
            {
                Mood = entry.Mood,
                Prompt = entry.Prompt,
                Response = entry.Response,
                Date = entry.Date,
                WordCount = entry.WordCount
            }).ToList();

            var options = new JsonSerializerOptions
            {
                WriteIndented = true
            };

            string json = JsonSerializer.Serialize(entries, options);
            File.WriteAllText(filename, json);
            Console.WriteLine("Journal saved.");

            string GetValidFileName()
            {
                string newName;
                do
                {
                    Console.Clear();
                    Console.WriteLine("Enter a new file name:");
                    Console.Write(">> ");
                    newName = Console.ReadLine();

                    // Check if the file name is valid
                    if (newName.IndexOfAny(invalidChars) >= 0)
                    {
                        Console.Clear();
                        Console.WriteLine("Invalid file name. Please enter a valid file name.");
                        Console.Write(">> ");
                    }
                    else
                    {
                        newName = newName.EndsWith(".json") ? newName : $"{newName}.json";
                    }
                } while (newName.IndexOfAny(invalidChars) >= 0);

                return newName;
            }
        }


        // Load entries from a file into the journal
        public void LoadFromFile()
        {
            // Get all the files with .json extension in the current directory
            string[] files = Directory.GetFiles(".", "*.json");
            if (files.Length == 0)
            {
                Console.WriteLine("No files found.");
                Console.WriteLine();
                return;
            }

            // Display the list of files with numbers to choose from
            Console.WriteLine("Choose a file to load:");
            foreach ((string file, int index) in files.Select((file, index) => (file, index)))
            {
                Console.WriteLine($"{index+1}. {file}");
            }

            // Prompt the user for input and validate it
            Console.Write(">> ");
            string input = Console.ReadLine();
            int choice;
            while (!int.TryParse(input, out choice) || choice < 1 || choice > files.Length)
            {
                Console.WriteLine("Invalid input. Please choose a number from the list.");
                Console.Write(">> ");
                input = Console.ReadLine();
            }

            // Load the chosen file and update the list of entries
            try
            {
                string filename = files[choice-1];
                string json = File.ReadAllText(filename);
                entries = JsonSerializer.Deserialize<List<Entry>>(json);
                Console.WriteLine($"Loaded {entries.Count} entries from {filename}.");
                Console.WriteLine();
            }
            catch (IndexOutOfRangeException)
            {
                Console.WriteLine("Error: Invalid file number. Please choose a number from the list.");
                Console.WriteLine();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error loading entries: " + ex.Message);
                Console.WriteLine();
            }
        }
    }
    // Define the Program class to handle user interaction and program flow
    class Program
    {
        static void Main(string[] args)
        {
            Journal journal = new Journal();

            // Keep looping until the user chooses to exit the program
            while (true)
            {
                
                Console.WriteLine("Choose an option:");
                Console.WriteLine("1. Write a new entry");
                Console.WriteLine("2. Display the journal");
                Console.WriteLine("3. Save the journal to a file");
                Console.WriteLine("4. Load the journal from a file");
                Console.WriteLine("5. Exit");
                Console.Write(">> ");

                string choice = Console.ReadLine();
                Console.Clear();

                switch (choice)
                {
                    case "1": // Write
                        Console.Clear();
                        Entry entry = new Entry();

                        // Prompt for mood and assign corresponding prompts
                        Console.WriteLine("How are you feeling today?");
                        Console.WriteLine("1. Happy");
                        Console.WriteLine("2. Sad");
                        Console.WriteLine("3. Excited");
                        Console.WriteLine("4. Bored");
                        Console.WriteLine("5. Angry");
                        Console.Write(">> ");
                        string moodChoice = Console.ReadLine();

                        string[] prompts;
                        switch (moodChoice)
                        {
                            case "1":
                                prompts = new string[] {
                                "What was the happiest moment of your day?",
                                "Who brought a smile to your face today?",
                                "What made you feel grateful today?",
                                "What was the kindest thing someone did for you today?",
                                "What did you accomplish today that made you proud?",
                                "What was the most beautiful thing you saw today?",
                                "Who made you laugh today, and why?",
                                "What is something you're looking forward to tomorrow?",
                                "What is something that never fails to make you happy?"
                            };
                            break;
                            case "2":
                                prompts = new string[] {
                                "What was the saddest moment of your day?",
                                "What triggered your sadness today?",
                                "What can you do to make yourself feel better?",
                                "What did you wish had gone differently today?",
                                "What do you miss the most right now?",
                                "What is the best way to take care of yourself when you're feeling down?",
                                "What are some positive things you can focus on right now?",
                                "Who can you reach out to for support or comfort?",
                                "Who can you talk to for support?"
                            };
                            break;
                            case "3":
                                prompts = new string[] {
                                "What are you excited about?",
                                "What made you feel energized today?",
                                "What new opportunities came your way?",
                                "What inspired you today?",
                                "What are you grateful for today?",
                                "What new ideas or possibilities are opening up for you?",
                                "What did you learn or discover today?",
                                "How can you channel your excitement into action or progress?",
                                "What are you looking forward to?"
                            };
                            break;
                            case "4":
                                prompts = new string[] {
                                "What made you feel bored today?",
                                "What can you do to break the monotony?",
                                "What is something you've been wanting to try?",
                                "What are some new hobbies or interests you want to explore?",
                                "What is something you've been meaning to learn?",
                                "What small changes can you make to your routine to add more variety?",
                                "What kind of adventure can you go on, even if it's just in your mind?",
                                "What are some fun, silly things you can do to liven up your day?",
                                "What can you do to make your day more interesting?"
                            };
                            break;
                            case "5":
                                prompts = new string[] {
                                "What made you feel angry today?",
                                "What triggered your anger?",
                                "How did you handle your anger?",
                                "What triggered your anger, and why?",
                                "What are some healthy ways to express and release your anger?",
                                "What positive changes can you make to prevent similar situations in the future?",
                                "What are some ways to reframe the situation or see it from a different perspective?",
                                "Who can you talk to for support or guidance?",
                                "What can you do to prevent getting angry in the future?"
                            };
                            break;
                            default:
                            Console.WriteLine("Invalid choice.");
                            Console.WriteLine();
                            continue;
                        }

                        // Choose a random prompt from the list of prompts
                        Random random = new Random();
                        entry.Prompt = prompts[random.Next(prompts.Length)];

                        entry.Mood = moodChoice;

                        Console.WriteLine();
                        Console.WriteLine(entry.Prompt);
                        Console.Write(">> ");
                        entry.Response = Console.ReadLine();
                        entry.Date = DateTime.Now;
                        journal.AddEntry(entry);
                        Console.WriteLine("Entry added.");
                        Console.WriteLine();
                        break;
                    case "2": // View
                        Console.WriteLine();
                        journal.DisplayEntries();
                        Console.WriteLine();
                        break;
                    case "3": // Save
                        Console.WriteLine("Enter filename:");
                        Console.Write(">> ");
                        string filename = Console.ReadLine();
                        journal.SaveToFile(filename);
                        Console.WriteLine();
                        break;
                    case "4": // Load
                        journal.LoadFromFile();
                        break;
                    case "5": // Exit
                        Console.WriteLine("Are you sure you want to exit? (Y/N)");
                        Console.Write(">> ");
                        string exitChoice = Console.ReadLine();
                        if (exitChoice.ToLower() == "y")
                        {
                            Environment.Exit(0);
                        }
                        break;
                    default:
                        Console.WriteLine("Invalid choice.");
                        Console.WriteLine();
                        break;
                }   
            }
        }
    }
}

/* 
The program uses the System.Collections.Generic, 
System.IO, and System.Text.Json namespaces, 
which provide classes for managing collections, 
working with files, and serializing and deserializing JSON data.

Added feature:
1.	Mood category that adds a layer for even more prompts
2.	Word count info for user to track their progress in their entries
3.	Having ‘>> ’ to indicate user input

4.	Saving File:
    •	No saving of empty Journal Entry
    •	No Invalid Character for the file name
    •	Overwrite option if file name chosen is already in the directory
    •	Converts save entry as ‘.json’ format
    •	Auto ‘.json’ extension when saving

5.	Loading File:
    •	Having option to choose files available in the directory (.json files) rather than typing file name

6.	Basic input validation and error handling all over the program
 */