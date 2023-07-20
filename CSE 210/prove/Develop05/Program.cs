using System;

class Program
{
  // Main method that gets executed when the program starts
  static void Main(string[] args)
  {
    // Display a welcome message
    DisplayWelcomeMessage();
    
    // initialize the choice variable to -1
    int choice = -1;

    // Create a new instance of the Game class
    Game game = new Game();
    do // start a loop that runs until the user chooses to quit
    {
      // Display the current points
      Console.WriteLine($"You currently have {game.getPoints()} points");
      
      ShowMenu();
      Console.Write("Please Type The Number Corresponding With Your Choice: ");
      
      // Read user input
      ConsoleKeyInfo input = Console.ReadKey();
      
      // try to parse the input as an integer & Check if the input is a valid integer
      if (int.TryParse(input.KeyChar.ToString(), out choice))
      {
        // switch on the user's choice
        switch (choice)
        {

          // if the choice is 1, call the Create method on the game object
          case 1:
              game.Create();
              break;

          // if the choice is 2, call the View method on the game object
          case 2:
              game.View();
              break;

          // if the choice is 3, call the Save method on the game object
          case 3:
              game.Save();
              break;

          // if the choice is 4, call the Load method on the game object
          case 4:
              game.Load();
              break;

          // if the choice is 5, call the Progress method on the game object
          case 5:
              game.Progress();
              break;

          // if the choice is 0, display the end message and exit the loop
          case 0:
              DisplayEndMessage();
              break;

          // if the choice is anything else, clear the console and display an error message
          default:
              Console.Clear();
              Console.WriteLine("Please Select a correct value");
              break;
        }
      }
      else
      {
          // if the input could not be parsed as an integer, clear the console and display an error message
          Console.Clear();
          Console.WriteLine("Please Select a correct value");
      }
    } while (choice != 0);
  }

  // method which displays a welcome message to the user
  static void DisplayWelcomeMessage()
  {
    Console.WriteLine("Welcome to the Gamification Program!");
  }

  // method which clears the console and displays a goodbye message to the user
  static void DisplayEndMessage()
  {
    Console.Clear();
    Console.WriteLine("Till Next Time, Bye!");
  }

  // method which displays the menu options to the user
  static void ShowMenu()
  {
    Console.Write(@"
    Menu Options :
      1) Create new Goal
      2) View Goals
      3) Save Goals
      4) Load Goals
      5) Record Progress
      0) Quit

    ");
  }

}
