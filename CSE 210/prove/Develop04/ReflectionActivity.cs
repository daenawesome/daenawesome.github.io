using System;
using System.Collections.Generic;

class ReflectionActivity : Activity // inherits from the Activity class
{
    // Array of prompts that will be randomly selected for the user to reflect on
    private string[] _prompts = new string[] {
        "Think of a time when you stood up for someone else.",
        "Think of a time when you did something really difficult.",
        "Think of a time when you helped someone in need.",
        "Think of a time when you did something truly selfless."
    };

    // Array of questions that will be presented to the user during the reflection
    private string[] _questions = new string[] {
        "Why was this experience meaningful to you?",
        "Have you ever done anything like this before?",
        "How did you get started?",
        "How did you feel when it was complete?",
        "What made this time different than other times when you were not as successful?",
        "What is your favorite thing about this experience?",
        "What could you learn from this experience that applies to other situations?",
        "What did you learn about yourself through this experience?",
        "How can you keep this experience in mind in the future?"
    };
    
    public ReflectionActivity()
    {
        // Name of the activity
        _activityName = "Reflection Activity";
        
        // Description of the activity
        _activityDescription = "This activity will help you reflect on times in your life when you have shown strength and resilience. This will help you recognize the power you have and how you can use it in other aspects of your life.";
    }

    public override void Start()
    {
        // Start activity
        base.Start();

        // Randomly select a prompt from the array of prompts
        Random random = new Random();
        int promptIndex = random.Next(_prompts.Length);
        string prompt = _prompts[promptIndex];
        
        // Print the prompt for the user to reflect on
        Console.WriteLine("Consider the following prompt \n");
        Console.WriteLine($"\t--- {prompt} ---");
        Console.WriteLine();
        
        // Wait for user input
        Console.WriteLine("When you have something in mind press enter to continue.");
        Console.ReadKey();

        // Present the array of questions to the user
        Console.WriteLine("Reflect about the following questions.");
        Console.Write("You may begin in: ");
        
        // Animate a countdown before presenting the questions
        Animation(ANIMATION_COUNTDOWN,3);
        
        // Clear the console and start presenting the questions
        Console.Clear();
        DateTime currentTime = DateTime.Now;
        DateTime futureTime = DateTime.Now.AddSeconds(_duration);

        do{
            // Randomly select a question from the array of questions
            int questionIndex = random.Next(_questions.Length);
            string question = _questions[questionIndex];

            // Present the question to the user
            Console.Write($"> {question} ");
            
            // Animate a spinner to indicate the application is working
            Animation(ANIMATION_SPINNER, 5);
            Console.WriteLine();

            // Check if the reflection period has ended
            currentTime = DateTime.Now;
        }while(currentTime < futureTime);
        
        // End the activity
        base.End();
    }
}
