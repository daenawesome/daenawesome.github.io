//In a new file, create the Square class.this class inherits from the 'Shape' class.
public class Square : Shape
{
    //Create the _side attribute as a private member variable.
    private double _side;
   
    //Create a constructor that accepts the color and the side, and then call the base constructor with the color.
    public Square(string color, double side) : base (color)
    {
        _side = side;
    }
   
    //Override the GetArea()
    public override double GetArea()
    {
        return _side * _side;
    }
}