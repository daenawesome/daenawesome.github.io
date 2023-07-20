using System;
using System.Collections.Generic;

// Define a class named ActivityLog to log activities and track their count
class ActivityLog
    {
        // Declare a private instance variable named activityCounts that will be used to store the count of each activity
        private Dictionary<string, int> activityCounts;

        // Define a constructor that initializes the activityCounts dictionary
        public ActivityLog()
        {
            activityCounts = new Dictionary<string, int>();
        }

        // Define a method named LogActivity that increments the count of a given activity name in the activityCounts dictionary
        public void LogActivity(string activityName)
        {
            // If the activity name is already in the dictionary, increment its count
            if (activityCounts.ContainsKey(activityName))
            {
                activityCounts[activityName]++;
            }
            
            // Otherwise, add the activity name to the dictionary and initialize its count to 1
            else
            {
                activityCounts.Add(activityName, 1);
            }
        }
        
        // Define a method named PrintActivityCounts that prints out the activity counts in the activityCounts dictionary
        public void PrintActivityCounts()
        {
            Console.WriteLine("For this Session you have: ");
            // Loop through each key-value pair in the activityCounts dictionary and print out the key-value pair
            foreach (KeyValuePair<string, int> activityCount in activityCounts)
            {
                Console.WriteLine($">> Completed = {activityCount.Value}: '{activityCount.Key}'");
            }
        }
    }

