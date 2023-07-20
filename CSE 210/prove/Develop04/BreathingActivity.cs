using System;
using System.Collections.Generic;

// Define the BreathingActivity class that inherits from the Activity class
class BreathingActivity : Activity
{
    // Define a constructor for the BreathingActivity class
    public BreathingActivity() 
    {
        // Set the name of the activity
        _activityName = "Breathing Activity";
        // Set the description of the activity
        _activityDescription = "This activity will help you focus on your breathing and relax";
    }

    // Define the Start() method, which will be called when the activity starts
    public override void Start()
    {
        // Call the base Start() method to perform any necessary setup
        base.Start();

        // Perform the breathing activity

        // Get the current time
        DateTime currentTime = DateTime.Now;
        // Calculate the time at which the activity should end
        DateTime futureTime = DateTime.Now.AddSeconds(_duration);

        // Loop until the current time is greater than or equal to the future time
        do{
            // Print a blank line for formatting
            Console.WriteLine();
            // Prompt the user to breathe in
            Console.Write("Breathe in...");
            // Call the Animation() method to display a countdown animation
            Animation(ANIMATION_COUNTDOWN, 4);
            // Print a blank line for formatting
            Console.WriteLine();
            // Prompt the user to breathe out
            Console.Write("Breathe out...");
            // Call the Animation() method to display a countdown animation
            Animation(ANIMATION_COUNTDOWN, 6);
            // Print a blank line for formatting
            Console.WriteLine();
            // Get the current time
            currentTime = DateTime.Now;
        } while(currentTime < futureTime); // Repeat until the activity is over

        // Call the base End() method to perform any necessary cleanup
        base.End();
    }
}
