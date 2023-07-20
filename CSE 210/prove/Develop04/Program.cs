using System;

class Program
{
    // This method displays a welcome message to the console
    static void DisplayWelcomeMessage()
    {
        Console.WriteLine("Welcome to the Mindfulness Program!");
    }

    // This method displays a good bye message to the console
    static void DisplayEndMessage()
    {
        Console.WriteLine("Till Next Time, Bye!");
        
    }

    // This method displays the menu of available activities to the console
    static void ShowMenu()
    {
        // Console.Clear();
        Console.Write(@"
            Would you like to:

            1) Start Breathing Activity
            2) Start Reflection Activity
            3) Start Listing Activity
            4) Start Reminder Activity
            5) View Log
            0) Exit and View Log

            ");
    }

    // This is the main entry point for the program
    static void Main(string[] args)
    {
        // Display a welcome message
        Console.WriteLine();
        DisplayWelcomeMessage();
        
        // create an instance of ActivityLog
        ActivityLog activityLog = new ActivityLog();

        // Initialize a variable for the user's choice
        int choice = -1;

        // Loop until the user chooses to exit
        do
        {   
            // Show the menu of available activities
            ShowMenu();

            // Prompt the user for their choice
            Console.WriteLine("Please Type The Number Corresponding With Your Choice: ");
            Console.Write(@"            >> ");

            // Read the user's choice from the console and convert it to an integer
            choice = int.Parse(Console.ReadLine());

            // Declare a variable to hold the selected activity
            Activity activity;

            // Use a switch statement to determine which activity the user selected
            switch(choice) 
            {
                // If the user chose breathing activity, create a new instance of the BreathingActivity class and start it
                case 1:
                    activity = new BreathingActivity();
                    activity.Start();
                    activityLog.LogActivity("Breathing Activity");
                    // activityLog.PrintActivityCounts();
                    break;
                
                // If the user chose reflection activity, create a new instance of the ReflectionActivity class and start it
                case 2:
                    activity = new ReflectionActivity();
                    activity.Start();
                    activityLog.LogActivity("Reflection Activity");
                    // activityLog.PrintActivityCounts();
                    break;
                
                // If the user chose listing activity, create a new instance of the ListingActivity class and start it
                case 3:
                    activity = new ListingActivity();
                    activity.Start();
                    activityLog.LogActivity("Listing Activity");
                    // activityLog.PrintActivityCounts();
                    break;
                
                // If the user chose reminder activity, create a new instance of the ReminderActivity class and start it
                case 4:
                    activity = new ReminderActivity();
                    activity.Start();
                    activityLog.LogActivity("Reminder Activity");
                    // activityLog.PrintActivityCounts();
                    break;
                
                // If the user chose to View Log, display Current Log at Header
                case 5:
                    Console.Clear();
                    activityLog.PrintActivityCounts();
                    break;
                
                // If the user chose to exit, display Log and a good bye message
                case 0:
                    Console.Clear();
                    activityLog.PrintActivityCounts(); //Prints Activity Log
                    Console.WriteLine();
                    DisplayEndMessage();
                    Console.WriteLine();
                    break;
                
                // If the user entered an invalid choice, clear the console and display an error message
                default:
                    Console.Clear();
                    Console.WriteLine("Please Select a correct value");
                    break;
            }

        } while (choice != 0); // Loop until the user chooses to exit
    }

}
