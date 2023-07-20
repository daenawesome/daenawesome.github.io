//In a new file, create the Shape class.
public abstract class Shape
{
    //Add the color member variable
    private string _color;
    
    //Create a constructor that accepts the color and set its.
    public Shape(string color)
    {
        _color = color;
    }
    
    //a getter and setter for the color member variable.
    public string GetColor()
    {
        return _color;
    }
    
    public void SetColor(string color)
    {
        _color = color;
    }
    
    //Create method for GetArea().
    public abstract double GetArea();
}