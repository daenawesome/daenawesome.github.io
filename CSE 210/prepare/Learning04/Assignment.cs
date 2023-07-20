//Creating a new file and a class for your base Assignment class.
public class Assignment
{
    //Adding the attributes as private member variables
    private string _studentName;
    private string _topic;

    //Creating a constructor for this class that receives a student name and topic and sets the member variables.
    public Assignment(string studentName, string topic)
    {
        _studentName = studentName;
        _topic = topic;
    }


    //Add the method for GetSummary() to return the student's name and the topic.
    public string GetSummary()
    {
        return _studentName + " - " + _topic;
    }

    // Getter And Setter for encapsulation
    public string GetStudentName()
    {
        return _studentName;
    }

    public string GetTopic()
    {
        return _topic;
    }

    public void setStudentName(string studentName)
    {
        _studentName = studentName ;
    }
    
    public void setTopic(string topic)
    {
        _topic = topic;
    }

    
 
}