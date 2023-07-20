Abstraction is being used in the program to hide the implementation details and only expose the necessary information and functionality to interact with the videos and comments. The program uses classes and properties to abstract the data and behaviors related to videos and comments.

1. Video Class:
The Video class represents a video object and provides the following abstractions:
- Properties: The class has properties such as Title, Author, Length, and Comments. These properties encapsulate the data related to a video and provide a way to access and manipulate that data without exposing the internal details. The properties are used to abstract the video's attributes.

- GetNumberOfComments() Method: This method abstracts the behavior of counting the number of comments on a video. Instead of directly accessing the Comments list and getting its count, this method provides a way to retrieve the number of comments without exposing the internal implementation details. It encapsulates the logic of counting the comments and provides a higher-level abstraction.

2. Comment Class:
The Comment class represents a comment object and provides the following abstractions:
- Properties: The class has properties such as CommenterName and CommentText, which encapsulate the data related to a comment. These properties abstract the comment's attributes and provide a way to access and modify the comment data.

3. Program Class:
The Program class is the entry point of the program and demonstrates the usage of the abstractions provided by the Video and Comment classes. It creates a list of Video objects and adds videos with associated comments to the list.

The program then iterates through the list of videos and displays information about each video using the abstractions:
- The program accesses the video properties (Title, Author, Length) to display information about the video. It does not directly access the internal fields or implementation details of the Video class, which are hidden by the abstraction of properties.
- The program calls the GetNumberOfComments() method on each video to retrieve the number of comments. This method provides an abstraction for counting comments, and the program does not need to directly manipulate the Comments list or its count.

Furthermore, the program uses nested iterations to display the comments for each video. It iterates through the comments list of each video and accesses the CommenterName and CommentText properties of each comment to display the commenter's name and the comment text. Again, the program does not directly manipulate the internal details of the Comment class; it abstracts the comment data through properties.

The program utilizes abstraction by encapsulating data and behaviors related to videos and comments in classes and properties. It provides a higher-level interface for interacting with videos and comments, hiding the implementation details and making the code more modular, maintainable, and reusable.