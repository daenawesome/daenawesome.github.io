using System;

class Program
{
    static void Main(string[] args)
    {
        //Create a simple assignment, call the method to get the summary, and then display it to the screen.
        Assignment first = new Assignment("Mr. Awesome-Daen Antule", "Multiplication");
        Console.WriteLine(first.GetSummary());
        Console.WriteLine();


        //creating a new MathAssignment object and set its values.
        //testing both the GetSummary() and the GetHomeworkList() methods
        MathAssignment second = new MathAssignment("Mr. Awesome-Daen Antule", "Fractions", "7.5", "42");
        Console.WriteLine(second.GetSummary());
        Console.WriteLine(second.GetHomeworkList());
        Console.WriteLine();

        // test of 'WritingAssignment' class
        WritingAssignment third = new WritingAssignment("Mr. Awesome-Daen Antule", "European History", "The Causes of World War II");
        Console.WriteLine(third.GetSummary());
        Console.WriteLine(third.GetWritingInformation());
        Console.WriteLine();

    }

}