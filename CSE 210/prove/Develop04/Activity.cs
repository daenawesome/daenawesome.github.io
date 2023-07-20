class Activity
{
  // Constant strings to represent different animations
  protected const string ANIMATION_SPINNER = "spinner";
  protected const string ANIMATION_COUNTDOWN = "countdown";
  protected const string ANIMATION_PAUSE = "pause";

  // Properties
  protected string _activityName;
  protected string _activityDescription;
  public int _duration;

  // Constructors
  public Activity(){
    _activityName = "Activity";
    _activityDescription = "This activity can help you to take more time to be mindful";
  }

  // Constructor with activity name and description parameters
  public Activity(string activityName, string activityDescription){
    _activityName = activityName;
    _activityDescription = activityDescription;
  }
  
  // This method is called when the activity is started.
  // It prompts the user for the duration of the activity and then starts the activity.
  public virtual void Start()
  {
    Console.Clear();
    Console.WriteLine(@$"            Welcome to the {_activityName}!");
    Console.WriteLine();
    Console.WriteLine(_activityDescription);
    Console.WriteLine();
    // Get duration from user
    Console.WriteLine("How long would you like to use this activity for? (in seconds) : ");
    Console.Write(">> ");
    _duration = int.Parse(Console.ReadLine());
    // Start activity
    Console.Clear();
    Console.WriteLine("Get Ready...");
    Animation(ANIMATION_SPINNER);
  }

  // This method is called when the activity is completed.
  // Displays a message indicating the completion of the activity and the duration of the activity.
  public virtual void End(){
    Console.WriteLine();
    Console.WriteLine("Well Done !!");
    Animation(ANIMATION_SPINNER);

    Console.WriteLine($"You have completed another {_duration} seconds of the {_activityName} ");
    Console.WriteLine("Returning now to the Main Menu");
    Animation(ANIMATION_SPINNER);
    Console.Clear();

  }

  // This method displays an animation based on the type parameter.
  // The time parameter determines the duration of the animation.
  protected void Animation(string type, int time = 3)
  {

    // Display a pause animation
    if (type == ANIMATION_PAUSE)
    {
      Console.Write("Pause");
      for (int i = 0; i < time; i++)
      {
        Console.Write(".");
        System.Threading.Thread.Sleep(1000);
      }
      Console.WriteLine();
    }
    
    // Display a countdown animation
    else if (type == ANIMATION_COUNTDOWN)
    {

      for (int i = time; i > 0; i--)
      {
        Console.Write(i);
        Thread.Sleep(1000);
        Console.Write("\b \b");
      }

    }
   
    // Display a spinner animation
    else if(type == ANIMATION_SPINNER )
    {
      // Display a spinner animation for the specified time.
      DateTime futureTime = DateTime.Now.AddSeconds(time);
      DateTime currentTime = DateTime.Now;
      
      string spin = "|/-\\";

      do{

        // Loop through the spinner animation characters
        foreach (char item in spin)
        {
          Console.Write($"{item}");
          Thread.Sleep(500);
          Console.Write("\b \b");
        }

        // Get the current time
        currentTime = DateTime.Now;
      }while(currentTime < futureTime); // Repeat until the activity is over
      
      Console.WriteLine();
    }

  }

}