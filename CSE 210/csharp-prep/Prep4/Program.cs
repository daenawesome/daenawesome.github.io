// Import the necessary libraries
using System;
using System.Collections.Generic;

class MainClass {
    public static void Main (string[] args) {
        // Create an empty list to store the numbers
        List<int> numbers = new List<int>();

        // Ask the user for a number
        while (true) {
            try {
                Console.Write("Enter a number, type 0 when finished: ");
                int number = int.Parse(Console.ReadLine());
                if (number == 0) {
                    break;
                }
                numbers.Add(number);
            } catch (FormatException) {
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }
        }

        // Ask the user for the sort order
        Console.Write("Enter 'asc' for ascending order or 'desc' for descending order: ");
        string sort_order = Console.ReadLine().ToLower();

        // Sort the numbers based on the sort order provided
        if (sort_order == "asc") {
            numbers.Sort();
        } else if (sort_order == "desc") {
            numbers.Sort((a, b) => b.CompareTo(a));
        } else {
            Console.WriteLine("Invalid input. Defaulting to ascending order.");
            numbers.Sort();
        }

        // Compute the sum of the numbers
        int total = 0;
        foreach (int number in numbers) {
            total += number;
        }

        // Compute the average of the numbers
        double average = (double) total / numbers.Count;

        // Find the maximum number
        int maximum = numbers[numbers.Count - 1];

        // Find the smallest positive number
        int smallest_positive = int.MaxValue;
        foreach (int number in numbers) {
            if (number > 0 && number < smallest_positive) {
                smallest_positive = number;
            }
        }

        // Print the results
        Console.WriteLine("\nThe sum is: " + total);
        Console.WriteLine("The average is: " + average);
        Console.WriteLine("The largest number is: " + maximum);
        Console.WriteLine("The smallest positive number is: " + smallest_positive);
        Console.WriteLine("The sorted list is: " + string.Join(", ", numbers));
        Console.WriteLine();

    }
}

/*
I have added input validation to ensure that the user enters only valid numbers.
Also, I have added feature to allow the user to specify if they want the numbers sorted in ascending or descending order, if the user enters invalid input for the sort order, the program defaults to ascending order.
And added error message handling for invalid input, it will print an error message "Invalid input. Please enter a valid number." if the user enters an invalid input.
*/