using System;

class Program
{
    static void Main(string[] args)
    {
        // Create two Job instances
        Job job1 = new Job("Microsoft", "Software Engineer", 2019, 2022);
        Job job2 = new Job("Apple", "Manager", 2022, 2023);


        // Create a Resume instance and add the two jobs to it
        Resume myResume = new Resume("Allison Rose");
        myResume.AddJob(job1);
        myResume.AddJob(job2);

        // Display the resume
        myResume.Display();
    }
}

// It's generally considered best practice to use properties instead of public fields to encapsulate data, as it allows to control access and behavior more effectively.
