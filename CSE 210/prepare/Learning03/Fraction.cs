using System;

namespace FractionClassDemo
{
    public class Fraction
    {
        // Private fields to hold numerator and denominator
        private int numerator;
        private int denominator;

        // Constructors
        public Fraction()
        {
            numerator = 1;
            denominator = 1;
        }

        public Fraction(int numerator)
        {
            this.numerator = numerator;
            denominator = 1;
        }

        public Fraction(int numerator, int denominator)
        {
            this.numerator = numerator;
            this.denominator = denominator;
        }

        // Getters and setters for numerator and denominator
        public int GetNumerator()
        {
            return numerator;
        }

        public void SetNumerator(int numerator)
        {
            this.numerator = numerator;
        }

        public int GetDenominator()
        {
            return denominator;
        }

        public void SetDenominator(int denominator)
        {
            if (denominator == 0)
            {
                throw new ArgumentException("Denominator cannot be zero");
            }
            this.denominator = denominator;
        }

        // Method to return the fraction in the form "numerator/denominator"
        public string GetFractionString()
        {
            return numerator + "/" + denominator;
        }

        // Method to return the decimal value of the fraction
        public double GetDecimalValue()
        {
            return (double)numerator / denominator;
        }
    }
}
