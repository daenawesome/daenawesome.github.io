using System;
using System.Collections.Generic;

// Define a class named ReminderActivity to remind user in a specified time
class ReminderActivity : Activity
{
    private string _reminderMessage; // inherits from the Activity class

    // Constructor for ReminderActivity, initializes the activity name and description
    public ReminderActivity()
    {
        _activityName = "Reminder Activity";
        _activityDescription = "This activity will help you set a reminder message that will be displayed after a certain period of time.";
    }

    public override void Start()
    {
        base.Start();
        
        // Get reminder message from user
        Console.WriteLine("What would you like your reminder message to be? ");
        Console.Write(">> ");
        _reminderMessage = Console.ReadLine();
        Console.WriteLine();
        
        // Set reminder time
        Console.WriteLine("In how many seconds would you like to be reminded? ");
        Console.Write(">> ");
        int reminderTime = int.Parse(Console.ReadLine());
        Console.WriteLine();
        
        // Start reminder
        Console.WriteLine($"A reminder has been set for '{_reminderMessage}' in {reminderTime} seconds.");
        DateTime reminderEndTime = DateTime.Now.AddSeconds(reminderTime);
        while (DateTime.Now < reminderEndTime)
        {
            // Pause for one second between each iteration
            Thread.Sleep(1000);
        }
        Console.WriteLine($@"
        REMINDER FOR: 
        
            {_reminderMessage}

        ");
        
        // End activity
        base.End();
    }
}


    // Prompts the user to input a reminder message and 
    // the duration until the reminder will be displayed. 
    // It then waits for the specified duration, displays 
    // the reminder message, and ends the activity.