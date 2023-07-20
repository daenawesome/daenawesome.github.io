// Define a public class named EternalGoal that derives from the Goal class
public class EternalGoal : Goal
{
  // Define a default constructor that calls the base class constructor
  public EternalGoal() : base()
  {

  }

  // Define a constructor that takes in a name, description, and points and calls the base class constructor with those values
  public EternalGoal(string name, string description, int points) : base(name, description, points)
  {

  }

  // Override the base class method GetAchievement, which returns false
  public override bool GetAchievement()
  {
    return false;
  }
  
  // Override the base class method SetAchievement, which sets the private _achievement field to false
  public override void SetAchievement(bool achievement)
  {
    _achievement = false;
  }

  // Override the base class method completionEvent, which calls SetAchievement with false and returns the value of GetPoints
  public override int completionEvent(){
    SetAchievement(false);
    return GetPoints();
  }
}

/*** 
The `EternalGoal` class is a subclass of the `Goal` class, which represents a type of goal that is never considered "complete" or "achieved." 
An `EternalGoal` object cannot be marked as achieved and always returns false for `GetAchievement()`.

The `EternalGoal` class overrides the `SetAchievement()` method to always set the `_achievement` field to false, 
and the `completionEvent()` method to always call `SetAchievement(false)` and return the number of points associated with the goal.
***/
