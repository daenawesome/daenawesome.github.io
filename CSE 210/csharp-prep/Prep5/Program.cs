using System;

class Program {
    static void Main() {
        DisplayWelcome(); // Call DisplayWelcome function
        string name = PromptUserName(); // Call PromptUserName function and store the returned string in variable 'name'
        int number = PromptUserNumber(); // Call PromptUserNumber function and store the returned integer in variable 'number'
        int square = SquareNumber(number); // Call SquareNumber function passing the 'number' variable and store the returned integer in variable 'square'
        DisplayResult(name, square); // Call DisplayResult function passing 'name' and 'square' variables as parameters
    }

    static void DisplayWelcome() {
        Console.WriteLine("Welcome to the Program!"); // Display "Welcome to the Program!" message
    }

    static string PromptUserName() {
        Console.Write("Please enter your name: "); // Ask for user's name
        return Console.ReadLine(); // Read user's input and return as string
    }

    static int PromptUserNumber() {
        Console.Write("Please enter your favorite number: "); // Ask for user's favorite number
        return int.Parse(Console.ReadLine()); // Read user's input, parse it as integer and return
    }

    static int SquareNumber(int number) {
        return number * number; // Square the number and return as integer
    }

    static void DisplayResult(string name, int square) {
        Console.WriteLine($"\n{name}, the square of your number is {square}\n"); // Display the user's name and their squared number
    }
}
