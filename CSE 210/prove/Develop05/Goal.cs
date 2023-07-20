public class Goal
{
  protected string _name; // The name of the goal
  protected string _description; // A short description of the goal
  protected int _points; // The number of points associated with the goal
  protected bool _achievement; // A flag indicating whether the goal has been achieved

  // Constructor to create a new goal object from user input
  public Goal(){
    Console.WriteLine("What is the name of your goal? ");
    Console.Write(">> ");
    string name = Console.ReadLine();
    Console.WriteLine();
    Console.WriteLine("What is the short description of it? ");
    Console.Write(">> ");
    string description = Console.ReadLine();
    
    // Variable for storing the points associated with the goal
    int points;
    bool isValidInput = false;
    do
    {
        Console.WriteLine();
        Console.WriteLine("What is the amount of points associated with this goal? ");
        Console.Write(">> ");
        string pointsInput = Console.ReadLine();
        // Parse the input to an integer
        isValidInput = int.TryParse(pointsInput, out points);
        if (!isValidInput)
        {
            Console.WriteLine("Invalid input. Please enter a valid integer value.");
        }
    } while (!isValidInput);

     // Set the values of the object based on the user input
    _name = name;
    _description = description;
    _points = points;
    _achievement = false;
  }

  // Constructor to create a goal object with pre-defined properties
  public Goal(string name, string description, int points)
  {
    _name = name;
    _description = description;
    _points = points;
    _achievement = false;
  }

  // Constructor to create a goal with pre-defined properties including achievement status
  public Goal(string name, string description, int points, bool achievement)
  {
    _name = name;
    _description = description;
    _points = points;
    _achievement = achievement;
  }

  // Getter method for the name of the goal
  public string GetName()
  {
    return _name;
  }

  // Setter method for the name of the goal
  public void SetName(string name)
  {
    _name = name;
  }

  // Getter method for the short description of the goal
  public string GetDescription()
  {
    return _description;
  }

  // Setter method for the short description of the goal
  public void SetDescription(string description)
  {
    _description = description;
  }

  // Getter method for the number of points associated with the goal
  public int GetPoints()
  {
    return _points;
  }

  // Setter method for the number of points associated with the goal
  public void SetPoints(int points)
  {
    _points = points;
  }

  // Getter method for the achievement flag of the goal
  public virtual bool GetAchievement()
  {
    return _achievement;
  }

  // Setter method for the achievement flag of the goal
  public virtual void SetAchievement(bool achievement)
  {
    _achievement = achievement;
  }

  // Method to be called when the goal is completed, returns the number of points associated with the goal
  public virtual int completionEvent(){
    // Method to handle completion of the goal
    SetAchievement(true);
    return GetPoints();
  }

  // Method to display the goal's details
  public virtual string Display()
  {
    string type;
    if (this.GetType() == typeof(EternalGoal))
    {
        type = "Eternal: ";
    }
    else if (this.GetType() == typeof(CheckListGoal))
    {
        type = "Checklist: ";
    }
    else
    {
        type = "Simple: ";
    }
    return $"[{(GetAchievement()?'X':' ')}]{type}{_name} - ({_description}) [{_points} points]";

  }

  // Method to convert the goal's properties into a string representation
  public virtual string Stringify(){
    return $"{GetType()}|*|{GetName()}|*|{GetDescription()}|*|{GetPoints()}|*|{GetAchievement()}" ;
  }

}