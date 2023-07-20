//Create a new file for the MathAssignment class ; inherits from the base Assignment class
public class MathAssignment : Assignment
{
    //Adding the attributes as private member variables. 
    // _topic and _studentName are inherited from  the base class.
    private string _textbookSection;
    private string _problems;

    //Creating a constructor for your class that accepts all four parameters,
    //have it call the base class constructor to set the base class attributes that way.
    public MathAssignment(string studentName, string topic, string textbookSection, string problems) : base(studentName, topic)
    {
        _textbookSection = textbookSection;
        _problems = problems;
    }

    //Adding the GetHomeworkList() method
    public string GetHomeworkList()
    {
        return $"Section {_textbookSection} Problems {_problems}";
    }
}