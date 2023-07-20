using System;

public class GuessNumberGame
{
public static void Main()
{
    Random random = new Random();

        // Generate a random number from 1 to 100
        int magicNumber = random.Next(1, 101);

        // Initialize the number of guesses to 0
        int numGuesses = 0;

        // Start a loop to play the game
        while (true)
        {
            // Get a guess from the user
            Console.Write("Enter your guess: ");
            int guess = int.Parse(Console.ReadLine());

            // Increment the number of guesses
            numGuesses++;

            // Check if the guess is correct
            if (guess == magicNumber)
            {
                Console.WriteLine("You guessed it! The magic number was {0}", magicNumber);
                Console.WriteLine("It took you {0} guesses.", numGuesses);
                break;
            }
            // If the guess is not correct, tell the user if they need to guess higher or lower
            else if (guess < magicNumber)
            {
                Console.WriteLine("Guess higher.");
            }
            else
            {
                Console.WriteLine("Guess lower.");
            }
        }

        // Ask the user if they want to play again
        Console.Write("Do you want to play again? (yes/no) ");
        string playAgain = Console.ReadLine();

        if (playAgain == "yes")
        {
            // If the user wants to play again, start a new game
            Console.WriteLine();
            magicNumber = random.Next(1, 101);
            numGuesses = 0;
            Main();
        }
        else
        {
            // If the user doesn't want to play again, exit the game
            Console.WriteLine("Thanks for playing! Goodbye.");
        }
    }
}
