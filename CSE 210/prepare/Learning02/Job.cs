using System;

public class Job
{
    // member variables
    private string _company;
    private string _jobTitle;
    private int _startYear;
    private int _endYear;

    // constructor
    public Job(string company, string jobTitle, int startYear, int endYear)
    {
        _company = company;
        _jobTitle = jobTitle;
        _startYear = startYear;
        _endYear = endYear;
    }

    // Display method
    public void Display()
    {
        Console.WriteLine($"{_jobTitle} ({_company}) {_startYear}-{_endYear}");
    }
}
