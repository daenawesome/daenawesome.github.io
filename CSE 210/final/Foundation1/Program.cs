using System;
using System.Collections.Generic;

// The program creates a collection of videos with associated comments and displays information about each video, 
// including its title, author, length, number of comments, and the comments themselves.

class Video
{
    public string Title { get; set; } // Property to store the title of the video
    public string Author { get; set; } // Property to store the author of the video
    public int Length { get; set; } // Property to store the length of the video in seconds
    public List<Comment> Comments { get; set; } // Property to store a list of comments on the video

    public int GetNumberOfComments() // Method to get the number of comments on the video
    {
        return Comments.Count;
    }
}

class Comment
{
    public string CommenterName { get; set; } // Property to store the name of the commenter
    public string CommentText { get; set; } // Property to store the text of the comment
}

class Program
{
    static void Main(string[] args)
    {
        List<Video> videos = new List<Video>(); // Create a list to store the videos

        // Create and add videos
        Video video1 = new Video // Create an instance of Video class
        {
            Title = "Video 1", // Set the title of the video
            Author = "Author 1", // Set the author of the video
            Length = 120, // Set the length of the video
            Comments = new List<Comment> // Create a list of comments for the video
            {
                new Comment { CommenterName = "User1", CommentText = "Great video!" }, // Add a comment to the list
                new Comment { CommenterName = "User2", CommentText = "I learned a lot." },
                new Comment { CommenterName = "User3", CommentText = "Nice work!" }
            }
        };
        videos.Add(video1); // Add the video to the list of videos

        Video video2 = new Video
        {
            Title = "Video 2",
            Author = "Author 2",
            Length = 180,
            Comments = new List<Comment>
            {
                new Comment { CommenterName = "User1", CommentText = "Awesome video!" },
                new Comment { CommenterName = "User2", CommentText = "Very informative." }
            }
        };
        videos.Add(video2);

        Video video3 = new Video
        {
            Title = "Video 3",
            Author = "Author 3",
            Length = 90,
            Comments = new List<Comment>
            {
                new Comment { CommenterName = "User1", CommentText = "Loved it!" }
            }
        };
        videos.Add(video3);

        // Display information for each video
        foreach (Video video in videos)
        {
            Console.WriteLine("Title: " + video.Title); // Print the title of the video
            Console.WriteLine("Author: " + video.Author); // Print the author of the video
            Console.WriteLine("Length: " + video.Length + " seconds"); // Print the length of the video
            Console.WriteLine("Number of Comments: " + video.GetNumberOfComments()); // Print the number of comments on the video

            Console.WriteLine("Comments:"); // Print a heading for the comments
            foreach (Comment comment in video.Comments) // Iterate through the comments of the video
            {
                Console.WriteLine("- " + comment.CommenterName + ": " + comment.CommentText); // Print the commenter name and comment text
            }

            Console.WriteLine(); 
        }

        Console.ReadLine(); 
    }
}
