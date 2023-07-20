//Creating the class and setting up the inheritance relationship.
public class WritingAssignment : Assignment
{
    //Adding the member variables
    private string _title;

    // setting up the constructor
    public WritingAssignment(string studentName, string topic, string title): base(studentName, topic)
    {
        _title = title;
    }

    //Adding the GetWritingInformation() method
    public string GetWritingInformation()
    {
        return $"{_title} by {GetStudentName()}";
    }
}