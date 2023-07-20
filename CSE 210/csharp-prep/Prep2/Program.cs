using System;

class Program {
    static void Main(string[] args) {
        // Prompt user for grade percentage
        Console.Write("What is your grade percentage? ");
        int gradePercentage = int.Parse(Console.ReadLine());

        // Determine letter grade
        string letter = "";
        if (gradePercentage >= 90) {
            letter = "A";
        } else if (gradePercentage >= 80) {
            letter = "B";
        } else if (gradePercentage >= 70) {
            letter = "C";
        } else if (gradePercentage >= 60) {
            letter = "D";
        } else {
            letter = "F";
        }

        // Determine sign of letter grade
        string sign = "";
        int lastDigit = gradePercentage % 10;
        if (letter == "A" && lastDigit >= 7) {
            sign = "+";
        } else if (letter == "A" && lastDigit < 3) {
            sign = "-";
        } else if ((letter == "B" || letter == "C" || letter == "D") && lastDigit >= 3 && lastDigit <= 6) {
            sign = "";
        } else if (letter == "B" && lastDigit >= 7) {
            sign = "+";
        } else if (letter == "B" && lastDigit < 3) {
            sign = "-";
        } else if (letter == "F") {
            sign = "";
        }

        // Display letter grade and sign
        Console.WriteLine($"Your letter grade is {letter}{sign}.");

        // Determine if user passed or failed the class and display appropriate message
        if (gradePercentage >= 70) {
            Console.WriteLine("Congratulations! You passed the class.");
        } else {
            Console.WriteLine("Better luck next time! Keep working hard.");
        }
    }
}
