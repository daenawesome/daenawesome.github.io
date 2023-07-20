using System;
using System.Collections.Generic;

public class Resume
{
    // member variables
    private string _name;
    private List<Job> _jobs;

    // constructor
    public Resume(string name)
    {
        _name = name;
        _jobs = new List<Job>();
    }

    // method to add a job to the list
    public void AddJob(Job job)
    {
        _jobs.Add(job);
    }

    // Display method
    public void Display()
    {
        Console.WriteLine($"Name: {_name}");
        Console.WriteLine("Jobs:");
        foreach (var job in _jobs)
        {
            job.Display();
        }
    }
}

// The code also initializes the List object in the constructor of the Resume class, ensuring that it's always available and doesn't need to be manually created. 
// This is a good way to avoid null reference exceptions that can occur if the list isn't initialized.
// I also made use of a foreach loop to iterate over the list of jobs, which is more concise and easier to read than using a for loop with an index variable.