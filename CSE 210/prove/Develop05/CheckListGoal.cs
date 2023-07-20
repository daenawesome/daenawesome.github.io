// Inheriting from the base class 'Goal'
public class CheckListGoal : Goal
{
  private int _achievementCount;
  private int _achievementGoal;
  private int _bonus;

  // Default constructor that initializes the fields by taking input from the user
  public CheckListGoal() : base()
  {
      Console.WriteLine();
      Console.WriteLine("How many times this goal needs to be accomplished for a bonus? ");
      Console.Write(">> ");
      int achievementGoal;
      // Prompt the user until a valid integer is entered
      while (!int.TryParse(Console.ReadLine(), out achievementGoal))
      {
          Console.WriteLine("Please enter a valid integer value.");
          Console.Write(">> ");
      }
      Console.WriteLine();
      Console.WriteLine("What is the bonus for accomplishing it that many times? ");
      Console.Write(">> ");
      int bonus;
      // Prompt the user until a valid integer is entered
      while (!int.TryParse(Console.ReadLine(), out bonus))
      {
          Console.WriteLine("Please enter a valid integer value.");
          Console.Write(">> ");
      }

      // Assigning values to the fields
      _bonus = bonus;
      _achievementCount = 0;
      _achievementGoal = achievementGoal;
  }

  // Constructor that takes arguments to initialize the fields
  public CheckListGoal(string name, string description, int points, int achievementGoal, int bonus) : base(name, description, points)
  {
    _bonus = bonus;
    _achievementCount = 0;
    _achievementGoal = achievementGoal;
  }

  // Constructor that takes arguments to initialize the fields
  public CheckListGoal(string name, string description, int points, int achievementCount, int achievementGoal, int bonus) : base(name, description, points)
  {
    _bonus = bonus;
    _achievementCount = achievementCount;
    _achievementGoal = achievementGoal;
  }

  // Getter method to return the current number of times the goal has been accomplished
  public int GetAchievementCount()
  {
    return _achievementCount;
  }

  // Setter method to set the number of times the goal has been accomplished
  public void SetAchievementCount(int achievementCount)
  {
    _achievementCount = achievementCount;
  }

  // Getter method to return the total number of times this goal needs to be accomplished for a bonus
  public int GetAchievementGoal()
  {
    return _achievementGoal;
  }
  
  // Setter method to set the total number of times this goal needs to be accomplished for a bonus
  public void SetAchievementGoal(int achievementGoal)
  {
    _achievementGoal = achievementGoal;
  }

  // Getter method to return the bonus awarded when the goal is accomplished 'achievementGoal' times
  public int GetBonus()
  {
    return _bonus;
  }

  // Setter method to return the bonus awarded when the goal is accomplished 'achievementGoal' times
  public void SetBonus(int bonus)
  {
    _bonus = bonus;
  }

  // Method to increment the achievement count when the goal is accomplished
  public void IncrementAchievementCount()
  {
    _achievementCount += 1;
  }

  // Overriding the completionEvent method to update the achievement count and return points and bonus if the goal is accomplished
  public override int completionEvent()
  {
      if (GetAchievementCount() < GetAchievementGoal())
      {
          // Increment the achievement count
          IncrementAchievementCount();
          // Set the achievement status based on the count
          SetAchievement(GetAchievementCount() == GetAchievementGoal());
          // If the achievement count reaches the goal, return points along with the bonus
          if (GetAchievementCount() == GetAchievementGoal())
              return GetPoints() + GetBonus(); 
          else // If the goal is not yet achieved, return only the points
              return GetPoints();
      }
      return 0; // If the achievement count has already reached the goal, return 0
  }

  public override string Display()
  {
    return $"{base.Display()} --- Currently Completed: {_achievementCount}/{_achievementGoal} & +[{_bonus}points as bonus]";
  }
  
  public override string Stringify()
  {
    return $"{GetType()}|*|{GetName()}|*|{GetDescription()}|*|{GetPoints()}|*|{GetAchievementCount()}|*|{GetAchievementGoal()}|*|{GetBonus()}";
  }

}