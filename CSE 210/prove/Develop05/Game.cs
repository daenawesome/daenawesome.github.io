using System.Collections.Generic;
using System.IO;

public class Game
{
  // Fields, a list to hold all the goals created
  List<Goal> _goals = new List<Goal>();
  private int _points;

  // Constructor to initialize the _points variable
  public Game()
  {
    _points = 0;
  }

  // Getter method for _points field
  public int getPoints()
  {
    return _points;
  }

  // Method to add points to _points field with an optional bonus value
  public void AddPoints(int points, int bonus = 0)
  {
      _points += points + bonus;
  }

  // Method to create a new goal 
  public void Create()
  {
    Console.Clear();
    Console.WriteLine(@"
    Create a Goal
        The type of goals are:
          1) Simple Goal
          2) Eternal Goal
          3) CheckList Goal

        ");
    Console.Write("Which type of goal would you want to create? ");
    var keyInfo = Console.ReadKey(); // Get the user's input
    int goalType;
    
    // Parse the input into an integer
    if (int.TryParse(keyInfo.KeyChar.ToString(), out goalType))
    {
      switch (goalType)
      {
        case 1:
          Console.Clear();
          Console.WriteLine("For a Simple Goal");
          Goal simple = new Goal();
          AddGoal(simple);
          break;
        case 2:
          Console.Clear();
          Console.WriteLine("For a Eternal Goal");
          EternalGoal eternal = new EternalGoal();
          AddGoal(eternal);
          break;
        case 3:
          Console.Clear();
          Console.WriteLine("For a CheckList Goal");
          CheckListGoal check = new CheckListGoal();
          AddGoal(check);
          break;
        default:
          Console.WriteLine("Please Select a Correct Goal type");
          break;
      }
    }
  }

  // Private helper method to add a goal to _goals list
  private void AddGoal(Goal goal)
  {
    _goals.Add(goal);
    Console.WriteLine("Goal created!");
    Console.Write("Going back to Main Menu");
    
    // pause the console for 3 seconds to allow the user to read the message
    System.Threading.Thread.Sleep(3000);
    Console.Clear();
  }

  // Method to view all goals
  public void View()
  {
      Console.Clear();
      Console.WriteLine("The goals are:");
      
      // check if there are any goals in the list
      if (_goals.Count == 0)
      {
          Console.WriteLine("   No goals found.");
      }
      else
      {
          // Display all goals with its index
          for (int i = 0; i < _goals.Count(); i++)
          {
              Console.WriteLine($"{i + 1}. {_goals[i].Display()}");
          }
      }
      Console.WriteLine();
  }

  // Method to update progress on a goal
  public void Progress()
  {
      if (_goals.Count == 0)
      {
          Console.Clear();
          Console.WriteLine("There are no goals to update progress on.");
          return;
      }
  
      View();
      Console.WriteLine("");
      Console.WriteLine("Which goal have you completed?: ");
      Console.Write(">> ");
      int goalIndex = int.Parse(Console.ReadLine()) - 1;
  
      if (_goals[goalIndex].GetAchievement())
      {
          Console.WriteLine("This goal has already been marked off.");
      }
      else
      {
          // Add points to _points field and mark the goal as complete
          AddPoints(_goals[goalIndex].completionEvent());
          Console.WriteLine("Goal updated!");
          Console.WriteLine($"Congratulations! You Earned {_goals[goalIndex].completionEvent()} Points!!");
      }
  
      Console.Write("Going back to Main Menu");
      // pause the console for 3 seconds to allow the user to read the message
      System.Threading.Thread.Sleep(3000);
      Console.Clear();
  }

  public void Save()
  {
      Console.Clear();
      if (_goals.Count == 0)
      {
          Console.WriteLine("There are no goals to save.");
          return;
      }

      Console.WriteLine("Type file name (with .txt extension): ");
      Console.Write(">> ");
      
      // Read the file name input from the user
      string filename = $"data\\{Console.ReadLine()}";
      
      // Check if the "data" directory exists, if not create it
      if (!Directory.Exists("data"))
      {
          Directory.CreateDirectory("data");
      }

      // Create a new StreamWriter to write the goals to the file
      using (StreamWriter outputFile = new StreamWriter(filename))
      {
          // Write the total points to the first line of the file
          outputFile.WriteLine($"{_points}");
          // Write each goal's information to subsequent lines of the file
          for (int i = 0; i < _goals.Count(); i++)
          {
              outputFile.WriteLine($"{_goals[i].Stringify()}");
          }
      }
      Console.WriteLine("Goals Saved");
      Console.Write("Going back to Main Menu");
      // pause the console for 3 seconds to allow the user to read the message
      System.Threading.Thread.Sleep(3000);
      Console.Clear();
  }

  // a method to load goals from a file
  public void Load()
  {
    Console.Clear();
    try
    {
      // Get a list of all files with .txt extension in the "data" directory
      string[] dirs = Directory.GetFiles(@"data\", "*.txt");
      
      // Display the list of files to choose from
      for (int i = 0; i < dirs.Length; i++)
      {
        Console.WriteLine($"{i + 1}. {dirs[i]}");
      }
      Console.WriteLine("Choose the file to load:");
      Console.Write(">> ");
      int fileIndex = int.Parse(Console.ReadLine());
      
      // Check if the selected file exists
      if(dirs[fileIndex-1] != null){
        string filename = dirs[fileIndex-1] ;
        // Read all lines from the selected file
        string[] lines = File.ReadAllLines(filename);
        // Extract the first line which contains the total points
        string first = lines.First();
        lines = lines.Except(new string[] { first }).ToArray();
        // Clear the existing goals list
        _goals.Clear();
        // Set the total points from the first line
        _points = int.Parse(first);
        
        // Iterate over each line of the file
        foreach (string line in lines)
        {
          // Split the line into parts using the delimiter "|*|"
          string[] parts = line.Split("|*|");
          
          // Check the type of goal based on the first part
          if(parts[0] == "Goal"){
            // If it's a regular Goal, create a new Goal object and add it to the goals list
            _goals.Add(new Goal(parts[1],parts[2],int.Parse(parts[3]), bool.Parse(parts[4])) );
          }else if(parts[0] == "EternalGoal"){
            // If it's an EternalGoal, create a new EternalGoal object and add it to the goals list
            _goals.Add(new EternalGoal(parts[1],parts[2],int.Parse(parts[3])));
          }else if(parts[0] == "CheckListGoal"){
            // If it's a CheckListGoal, create a new CheckListGoal object and add it to the goals list
            _goals.Add(new CheckListGoal(parts[1],parts[2],int.Parse(parts[3]), int.Parse(parts[4]), int.Parse(parts[5]) , int.Parse(parts[6])   ));
          }
        }
      }
    }
    // Catch any exceptions that occur during the file reading and loading process
    catch (Exception e)
    {
        Console.WriteLine("The process failed: {0}", e.ToString());
    }
    Console.WriteLine();
    Console.WriteLine("Goals Loaded");
    Console.Write("Going back to Main Menu");
    // pause the console for 3 seconds to allow the user to read the message
    System.Threading.Thread.Sleep(3000);
    Console.Clear();
  }

}