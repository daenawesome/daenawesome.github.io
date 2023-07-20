using System;
using System.Collections.Generic;

class ListingActivity : Activity // inherits from the Activity class
{
    // An array of prompts for the activity
    private string[] _prompts = new string[] {
        "Who are people that you appreciate?.",
        "What are personal strengths of yours?.",
        "Who are people that you have helped this week?.",
        "When have you felt the Holy Ghost this month?.",
        "Who are some of your personal heroes?."
    };
    
    // Constructor that sets the name and description of the activity
    public ListingActivity()
    {
        _activityName = "Listing Activity";
        _activityDescription = "This activity will help you reflect on the good things in your life by having you list as many things as you can in a certain area.";
    }

    // Overriding the Start() method from the base class
    public override void Start()
    {
        // Start activity by calling base Start() method
        base.Start();

        // Select a random prompt from the _prompts array
        Random random = new Random();
        int index = random.Next(_prompts.Length);
        string prompt = _prompts[index];

        // Create a list to store the user's responses
        List<string> answers = new List<string>();

        // Display the prompt to the user and give them a countdown before starting
        Console.WriteLine("List as many responses you can to the following prompt:");
        Console.WriteLine();
        Console.WriteLine($"\t---{prompt}---");
        Console.WriteLine();
        Console.Write("You may begin in: ");
        Animation(ANIMATION_COUNTDOWN, 3);
        Console.WriteLine();

        // Keep asking the user for responses until the duration is over
        DateTime currentTime = DateTime.Now;
        DateTime futureTime = DateTime.Now.AddSeconds(_duration);
        do {
            Console.Write(">> ");
            answers.Add(Console.ReadLine());
            Console.WriteLine();
            currentTime = DateTime.Now;
        } while (currentTime < futureTime);

        // Display the number of items the user listed
        Console.WriteLine($"You listed {answers.Count} items!");

        // End the activity by calling the base End() method
        base.End();
    }
}

