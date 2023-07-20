using System;

class Program
{
    static void Main(string[] args)
    {
        List<Shape> shapesList = new List<Shape>();

        //Create a Square instance,
        Square my_square = new Square("Purple", 2);
        shapesList.Add(my_square);

        //Create a Rectangle instance,
        Rectangle my_rectangle = new Rectangle("Green", 3, 4);
        shapesList.Add(my_rectangle);

        //Create a Circle instance,
        Circle my_circle = new Circle("Black", 5);
        shapesList.Add(my_circle);

        foreach (Shape shape in shapesList)
        {
            string color = shape.GetColor();
            double area = shape.GetArea();
            Console.WriteLine($"The area of the {color} {shape.GetType()} : {area}.");
        }
    }
}