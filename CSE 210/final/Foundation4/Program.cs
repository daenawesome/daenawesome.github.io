using System;
using System.Collections.Generic;
using System.IO;

// In this modified version of the code to show creativity and exceed requirements, I have added functionality to load 
// exercise data from a text file (exerciseData.txt) and authenticate the user to view their exercise data. 

// Represents an activity
class Activity
{
    private DateTime date;
    private int length;
    protected int userId;

    public Activity(DateTime date, int length, int userId)
    {
        this.date = date;
        this.length = length;
        this.userId = userId;
    }

    // Gets the user ID associated with the activity
    public int UserId
    {
        get { return userId; }
    }

    // Calculates and returns the distance covered during the activity (to be implemented by derived classes)
    public virtual double GetDistance()
    {
        return 0;
    }

    // Calculates and returns the speed of the activity (to be implemented by derived classes)
    public virtual double GetSpeed()
    {
        return 0;
    }

    // Calculates and returns the pace of the activity (to be implemented by derived classes)
    public virtual double GetPace()
    {
        return 0;
    }

    // Gets a summary of the activity (to be implemented by derived classes)
    public virtual string GetSummary()
    {
        return "";
    }

    // Gets the date of the activity
    public DateTime Date
    {
        get { return date; }
    }

    // Gets the length of the activity
    public int Length
    {
        get { return length; }
    }
}

// Represents a running activity
class Running : Activity
{
    private double distance;

    public Running(DateTime date, int length, double distance, int userId) : base(date, length, userId)
    {
        this.distance = distance;
    }

    // Calculates and returns the distance covered during the running activity
    public override double GetDistance()
    {
        return distance;
    }

    // Calculates and returns the speed of the running activity
    public override double GetSpeed()
    {
        return distance / (Length / 60.0);
    }

    // Calculates and returns the pace of the running activity
    public override double GetPace()
    {
        return Length / distance;
    }

    // Gets a summary of the running activity
    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Running ({Length} min) - Distance: {distance:F1} miles, Speed: {GetSpeed():F1} mph, Pace: {GetPace():F1} min per mile";
    }
}

// Represents a cycling activity
class Cycling : Activity
{
    private double speed;

    public Cycling(DateTime date, int length, double speed, int userId) : base(date, length, userId)
    {
        this.speed = speed;
    }

    // Calculates and returns the speed of the cycling activity
    public override double GetSpeed()
    {
        return speed;
    }

    // Calculates and returns the pace of the cycling activity
    public override double GetPace()
    {
        return 60.0 / speed;
    }

    // Gets a summary of the cycling activity
    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Cycling ({Length} min) - Speed: {speed:F1} mph, Pace: {GetPace():F1} min per mile";
    }
}

// Represents a swimming activity
class Swimming : Activity
{
    private int laps;

    public Swimming(DateTime date, int length, int laps, int userId) : base(date, length, userId)
    {
        this.laps = laps;
    }

    // Calculates and returns the distance covered during the swimming activity
    public override double GetDistance()
    {
        return laps * 50.0 / 1000.0;
    }

    // Calculates and returns the speed of the swimming activity
    public override double GetSpeed()
    {
        return GetDistance() / (Length / 60.0);
    }

    // Calculates and returns the pace of the swimming activity
    public override double GetPace()
    {
        return Length / GetDistance();
    }

    // Gets a summary of the swimming activity
    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Swimming ({Length} min) - Distance: {GetDistance():F1} km, Speed: {GetSpeed():F1} kph, Pace: {GetPace():F1} min per km";
    }
}

class Program
{
    const string AdminAuthenticationCode = "0000";

    static void Main(string[] args)
    {
        bool exitProgram = false;

        do
        {
            Dictionary<string, List<Activity>> exerciseData = LoadExerciseData("exerciseData.txt");

            DisplayUserList(exerciseData);

            string selectedUser = GetUserSelection(exerciseData);

            if (selectedUser == "Admin")
            {
                Console.Clear();
                Console.WriteLine("----------------------------------------------------------------------------------------------");
                Console.WriteLine("ADMIN AUTHENTICATION                                                                         /");
                Console.WriteLine("----------------------------------------------------------------------------------------------");

                Console.WriteLine("Please enter the authentication code:");
                string authenticationCode = Console.ReadLine();

                if (authenticationCode == AdminAuthenticationCode)
                {
                    Console.Clear();
                    Console.WriteLine("----------------------------------------------------------------------------------------------");
                    Console.WriteLine("ALL EXERCISE DATA:");
                    Console.WriteLine("----------------------------------------------------------------------------------------------");

                    foreach (var userData in exerciseData)
                    {
                        string user = userData.Key.StartsWith("User_") ? userData.Key.Substring(5) : userData.Key;
                        List<Activity> userActivities = userData.Value;

                        Console.WriteLine($"Exercise Data for User: {user}");

                        foreach (Activity activity in userActivities)
                        {
                            Console.WriteLine(activity.GetSummary());
                        }

                        Console.WriteLine();
                    }
                }
                else
                {
                    Console.WriteLine("Authentication failed. HINT: 0000.");
                }
            }
            else if (selectedUser == "Exit")
            {
                exitProgram = true;
            }
            else
            {
                List<Activity> selectedUserData = exerciseData[selectedUser];

                int userId = GetUserId(selectedUser);
                if (userId != -1)
                {
                    if (ValidateUserId(userId, exerciseData[selectedUser]))
                    {
                        string user = selectedUser.StartsWith("User_") ? selectedUser.Substring(5) : selectedUser;

                        Console.Clear();
                        Console.WriteLine($"Exercise Data for User: {user}, ID: {userId}\n");

                        foreach (Activity activity in selectedUserData)
                        {
                            Console.WriteLine(activity.GetSummary().Replace($"User_{userId}", ""));
                        }
                    }
                    else
                    {
                        Console.WriteLine("Invalid User ID.");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input. Please try again.");
                }
            }

            if (!exitProgram)
            {
                Console.WriteLine("\nPlease enter your choice:");
                Console.WriteLine("1. Go back to the main menu");
                Console.WriteLine("2. Exit the program");

                string choice = Console.ReadLine();

                if (choice == "2")
                {
                    exitProgram = true;
                }

                Console.Clear();
            }
        } while (!exitProgram);
    }

    // Loads exercise data from a text file and returns a dictionary containing the data
    static Dictionary<string, List<Activity>> LoadExerciseData(string filePath)
    {
        Dictionary<string, List<Activity>> exerciseData = new Dictionary<string, List<Activity>>();

        string[] lines = File.ReadAllLines(filePath);

        string currentUser = null;
        List<Activity> currentActivities = null;
        int currentUserId = -1;

        foreach (string line in lines)
        {
            if (line.StartsWith("User_"))
            {
                currentUser = line.Trim();
                currentActivities = new List<Activity>();
                exerciseData[currentUser] = currentActivities;
            }
            else if (line.StartsWith("ID:"))
            {
                int.TryParse(line.Substring(3).Trim(), out currentUserId);
            }
            else if (line.StartsWith("Running") || line.StartsWith("Cycling") || line.StartsWith("Swimming"))
            {
                string[] parts = line.Split(',');

                string activityType = parts[0].Trim();
                DateTime date = DateTime.Parse(parts[1].Trim());
                int length = int.Parse(parts[2].Trim());
                double value = double.Parse(parts[3].Trim());

                Activity activity;
                if (activityType == "Running")
                {
                    activity = new Running(date, length, value, currentUserId);
                }
                else if (activityType == "Cycling")
                {
                    activity = new Cycling(date, length, value, currentUserId);
                }
                else if (activityType == "Swimming")
                {
                    activity = new Swimming(date, length, (int)value, currentUserId);
                }
                else
                {
                    continue; // Skip unknown activity types
                }

                currentActivities.Add(activity);
            }
        }

        return exerciseData;
    }

    // Displays the list of available users
    static void DisplayUserList(Dictionary<string, List<Activity>> exerciseData)
    {
        int count = 1;
        Console.WriteLine("Available Users:");
        foreach (string user in exerciseData.Keys)
        {
            string userName = user.StartsWith("User_") ? user.Substring(5) : user;
            Console.WriteLine($"{count}. {userName}");
            count++;
        }

        // Add Admin user
        Console.WriteLine($"{count}. Admin");
    }

    // Gets the user's selection from the available users
    static string GetUserSelection(Dictionary<string, List<Activity>> exerciseData)
    {
        Console.WriteLine("Please enter the number of the user to load:");
        int selection;

        while (true)
        {
            if (int.TryParse(Console.ReadLine(), out selection))
            {
                int count = 1;
                foreach (string user in exerciseData.Keys)
                {
                    if (count == selection)
                    {
                        return user;
                    }
                    count++;
                }

                // Check if the selection is for the Admin user
                if (count == selection)
                {
                    return "Admin";
                }

                Console.WriteLine("Invalid input. Please enter a valid user number:");
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid integer:");
            }
        }
    }

    // Gets the user ID for a selected user
    static int GetUserId(string selectedUser)
    {
        Console.Clear();
        Console.WriteLine($"Please enter the 4-digit User ID for {selectedUser}:");
        string userInput = Console.ReadLine();

        if (int.TryParse(userInput, out int userId))
        {
            return userId;
        }

        return -1;
    }

    // Validates the user ID by checking if it matches the user's activities
    static bool ValidateUserId(int userId, List<Activity> userActivities)
    {
        foreach (Activity activity in userActivities)
        {
            if (activity is Running)
            {
                Running runningActivity = (Running)activity;
                if (runningActivity.UserId != userId)
                {
                    return false;
                }
            }
            else if (activity is Cycling)
            {
                Cycling cyclingActivity = (Cycling)activity;
                if (cyclingActivity.UserId != userId)
                {
                    return false;
                }
            }
            else if (activity is Swimming)
            {
                Swimming swimmingActivity = (Swimming)activity;
                if (swimmingActivity.UserId != userId)
                {
                    return false;
                }
            }
        }

        return true;
    }
}
