using System;
using System.Collections.Generic;

// The program creates instances of different activities (running, cycling, swimming) with specific 
// details (date, length, distance/speed/laps) and displays a summary of each activity including the date, 
// duration, and relevant information such as distance, speed, and pace.

class Activity
{
    private DateTime date; // Stores the date of the activity
    private int length; // Stores the duration of the activity in minutes

    public Activity(DateTime date, int length)
    {
        this.date = date;
        this.length = length;
    }

    public virtual double GetDistance()
    {
        return 0; // Base implementation returns 0 distance
    }

    public virtual double GetSpeed()
    {
        return 0; // Base implementation returns 0 speed
    }

    public virtual double GetPace()
    {
        return 0; // Base implementation returns 0 pace
    }

    public virtual string GetSummary()
    {
        return ""; // Base implementation returns an empty summary
    }

    public DateTime Date
    {
        get { return date; }
    }

    public int Length
    {
        get { return length; }
    }
}

class Running : Activity
{
    private double distance; // Stores the distance covered during running in miles

    public Running(DateTime date, int length, double distance) : base(date, length)
    {
        this.distance = distance;
    }

    public override double GetDistance()
    {
        return distance; // Returns the distance covered during running
    }

    public override double GetSpeed()
    {
        return distance / (Length / 60.0); // Calculates the speed in miles per hour
    }

    public override double GetPace()
    {
        return Length / distance; // Calculates the pace in minutes per mile
    }

    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Running ({Length} min) - Distance: {distance:F1} miles, Speed: {GetSpeed():F1} mph, Pace: {GetPace():F1} min per mile";
        // Returns a formatted summary of the running activity including the date, duration, distance, speed, and pace
    }
}

class Cycling : Activity
{
    private double speed; // Stores the speed during cycling in miles per hour

    public Cycling(DateTime date, int length, double speed) : base(date, length)
    {
        this.speed = speed;
    }

    public override double GetSpeed()
    {
        return speed; // Returns the speed during cycling
    }

    public override double GetPace()
    {
        return 60.0 / speed; // Calculates the pace in minutes per mile
    }

    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Cycling ({Length} min) - Speed: {speed:F1} mph, Pace: {GetPace():F1} min per mile";
        // Returns a formatted summary of the cycling activity including the date, duration, speed, and pace
    }
}

class Swimming : Activity
{
    private int laps; // Stores the number of laps swam during swimming

    public Swimming(DateTime date, int length, int laps) : base(date, length)
    {
        this.laps = laps;
    }

    public override double GetDistance()
    {
        return laps * 50.0 / 1000.0; // Calculates the distance covered during swimming in kilometers
    }

    public override double GetSpeed()
    {
        return GetDistance() / (Length / 60.0); // Calculates the speed in kilometers per hour
    }

    public override double GetPace()
    {
        return Length / GetDistance(); // Calculates the pace in minutes per kilometer
    }

    public override string GetSummary()
    {
        return $"{Date.ToString("dd MMM yyyy")} Swimming ({Length} min) - Distance: {GetDistance():F1} km, Speed: {GetSpeed():F1} kph, Pace: {GetPace():F1} min per km";
        // Returns a formatted summary of the swimming activity including the date, duration, distance, speed, and pace
    }
}

class Program
{
    static void Main(string[] args)
    {
        List<Activity> activities = new List<Activity>();

        // Create activities
        Running runningActivity = new Running(new DateTime(2022, 11, 3), 30, 3.0);
        Cycling cyclingActivity = new Cycling(new DateTime(2022, 11, 3), 30, 6.0);
        Swimming swimmingActivity = new Swimming(new DateTime(2022, 11, 3), 30, 20);

        // Add activities to the list
        activities.Add(runningActivity);
        activities.Add(cyclingActivity);
        activities.Add(swimmingActivity);

        // Display summaries
        foreach (Activity activity in activities)
        {
            Console.WriteLine(activity.GetSummary());
        }
    }
}
