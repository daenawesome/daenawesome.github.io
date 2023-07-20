# Polymorphism in Programming

Polymorphism is a crucial concept in programming that allows us to treat different objects as if they belong to the same type. This flexibility enables the creation of versatile code capable of interacting with various entities. In the context of the application developed this week, we were tasked with creating a game featuring multiple goal types, namely simple, eternal, and checklist goals, each with its unique characteristics and behavior. Utilizing polymorphism, we can handle these different goal types uniformly, simplifying code maintenance and facilitating the addition of new features.

## Implementing Polymorphism in the Game

### Inheritance and Method Override

To achieve polymorphism, we utilized inheritance, creating child classes (`EternalGoal` and `CheckListGoal`) that inherit from a parent class, `Goal`. Each child class can have its own specific properties and methods while still sharing traits with the parent class. One of the primary implementations of polymorphism is the overriding of the `Display` method in the child classes. This allows different information to be displayed depending on the type of goal:

- The `Display` method in the `CheckListGoal` class displays the list of items required to complete the goal.
- The `Display` method in the `EternalGoal` class displays a message indicating that the goal is everlasting and cannot be completed.

### Utilizing Polymorphism in the `Game` Class

Within the `Game` class, we make use of polymorphism to handle multiple goal objects stored in the `_goals` list effectively. When the `View` method is called, it iterates through the list and calls the `Display` method for each goal. This ensures that the correct information is displayed for each goal based on its type.

### Flexible `AddGoal()` Method

The `AddGoal()` method in the application takes a `Goal` object as a parameter. However, it is designed to accept any object derived from the `Goal` class due to polymorphism. As each derived goal class implements the same interface as the `Goal` class, the `AddGoal()` method can treat all these objects as if they were of type `Goal`, enhancing generality and flexibility in the code.

```csharp
private void AddGoal(Goal goal)
{
  _goals.Add(goal);
  Console.WriteLine("Goal created!");
  Console.Write("Going back to the Main Menu");
  System.Threading.Thread.Sleep(3000);
  Console.Clear();
}
```

By leveraging polymorphism in these ways, we have developed a game application that can handle diverse goal types seamlessly, promoting code reusability, maintainability, and scalability.