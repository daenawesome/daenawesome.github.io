using System;

namespace FractionClassDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create fractions using different constructors
            Fraction f1 = new Fraction();
            Fraction f2 = new Fraction(5);
            Fraction f3 = new Fraction(6, 7);

            // Get and display the values of the fractions
            Console.WriteLine(f1.GetFractionString());
            Console.WriteLine(f1.GetDecimalValue());
            Console.WriteLine(f2.GetFractionString());
            Console.WriteLine(f2.GetDecimalValue());
            Console.WriteLine(f3.GetFractionString());
            Console.WriteLine(f3.GetDecimalValue());

            // Change the values of the fractions using setters
            f1.SetNumerator(3);
            f1.SetDenominator(4);
            f2.SetDenominator(2);
            f3.SetNumerator(2);

            // Get and display the new values of the fractions
            Console.WriteLine();
            Console.WriteLine(f1.GetFractionString());
            Console.WriteLine(f1.GetDecimalValue());
            Console.WriteLine(f2.GetFractionString());
            Console.WriteLine(f2.GetDecimalValue());
            Console.WriteLine(f3.GetFractionString());
            Console.WriteLine(f3.GetDecimalValue());
        }
    }
}
