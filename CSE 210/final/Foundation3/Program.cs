using System;
using System.IO;
using System.Collections.Generic;

// Modified Version to show creativity and exceed requirements now reads data (Event details) from a text file

// Address class to encapsulate the address details
public class Address
{
    public string Street { get; set; }
    public string City { get; set; }
    public string State { get; set; }
    public string Country { get; set; }

    public Address(string street, string city, string state, string country)
    {
        Street = street;
        City = city;
        State = state;
        Country = country;
    }

    public override string ToString()
    {
        return $"{Street}, {City}, {State}, {Country}";
    }
}

// Base Event class
public class Event
{
    private string eventTitle;
    private string eventDescription;
    private DateTime eventDate;
    private TimeSpan eventTime;
    private Address eventAddress;

    public Event(string title, string description, DateTime date, TimeSpan time, Address address)
    {
        eventTitle = title;
        eventDescription = description;
        eventDate = date;
        eventTime = time;
        eventAddress = address;
    }

    public string GetStandardDetails()
    {
        return $"Event Title: {eventTitle}\n" +
               $"Description: {eventDescription}\n" +
               $"Date: {eventDate.ToShortDateString()}\n" +
               $"Time: {eventTime}\n" +
               $"Address: {eventAddress}";
    }

    public virtual string GetFullDetails()
    {
        return GetStandardDetails();
    }

    public string GetShortDescription()
    {
        string eventType = GetType().Name;
        eventType = System.Text.RegularExpressions.Regex.Replace(eventType, "(\\B[A-Z])", " $1"); // Add spaces before capital letters
        return $"Type: {eventType}\n" +
               $"Event Title: {eventTitle}\n" +
               $"Date: {eventDate.ToShortDateString()}";
    }


    public string GetEventTitle()
    {
        return eventTitle;
    }
}

// Lecture Event derived class
public class LectureEvent : Event
{
    private string speaker;
    private int capacity;

    public LectureEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                        string speaker, int capacity)
        : base(title, description, date, time, address)
    {
        this.speaker = speaker;
        this.capacity = capacity;
    }

    public override string GetFullDetails()
    {
        return $"{base.GetFullDetails()}\n" +
               $"Type: Lecture Event\n" +
               $"Speaker: {speaker}\n" +
               $"Capacity: {capacity}";
    }
}

// Reception Event derived class
public class ReceptionEvent : Event
{
    private string rsvpEmail;

    public ReceptionEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                          string rsvpEmail)
        : base(title, description, date, time, address)
    {
        this.rsvpEmail = rsvpEmail;
    }

    public override string GetFullDetails()
    {
        return $"{base.GetFullDetails()}\n" +
               $"Type: Reception Event\n" +
               $"RSVP Email: {rsvpEmail}";
    }
}

// Outdoor Gathering Event derived class
public class OutdoorGatheringEvent : Event
{
    private string weatherForecast;

    public OutdoorGatheringEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                                 string weatherForecast)
        : base(title, description, date, time, address)
    {
        this.weatherForecast = weatherForecast;
    }

    public override string GetFullDetails()
    {
        return $"{base.GetFullDetails()}\n" +
               $"Type: Outdoor Gathering Event\n" +
               $"Weather Forecast: {weatherForecast}";
    }
}

class Program
{
    static void PrintAllEvents(List<Event> events)
    {
        // Print all events with their details
        Console.WriteLine("All Events:");
        Console.WriteLine("------------------------------------------------------------------------------");
        foreach (Event ev in events)
        {
            Console.WriteLine("Event Details:");
            Console.WriteLine("------------------------------------------------------------------------------");
            Console.WriteLine("Standard Details:\n" + ev.GetStandardDetails());
            Console.WriteLine("\nFull Details:\n" + ev.GetFullDetails());
            Console.WriteLine("\nShort Description:\n" + ev.GetShortDescription());
            Console.WriteLine("------------------------------------------------------------------------------");
        }
        Console.WriteLine("------------------------------------------------------------------------------");
        Console.WriteLine();
    }

    static void Main(string[] args)
    {
        // Read event data from file
        string[] eventData = File.ReadAllLines("events.txt");

        // Initialize event list and title list
        List<Event> events = new List<Event>();
        List<string> eventTitles = new List<string>();

        // Initialize variables
        Event currentEvent = null;
        string eventType = null;
        string eventTitle = null;
        string eventDescription = null;
        DateTime eventDate = DateTime.MinValue;
        TimeSpan eventTime = TimeSpan.Zero;
        Address eventAddress = null;
        string speaker = null;
        int capacity = 0;
        string rsvpEmail = null;
        string weatherForecast = null;

        // Process each line of event data
        foreach (string line in eventData)
        {
            if (line.StartsWith("Type: "))
            {
                eventType = line.Substring(6);
            }
            else if (line.StartsWith("Event Title: "))
            {
                eventTitle = line.Substring(13);
                eventTitles.Add(eventTitle);
            }
            else if (line.StartsWith("Description: "))
            {
                eventDescription = line.Substring(13);
            }
            else if (line.StartsWith("Date: "))
            {
                DateTime.TryParse(line.Substring(6), out eventDate);
            }
            else if (line.StartsWith("Time: "))
            {
                TimeSpan.TryParse(line.Substring(6), out eventTime);
            }
            else if (line.StartsWith("Address: "))
            {
                string[] addressData = line.Substring(9).Split(',');
                eventAddress = new Address(addressData[0].Trim(), addressData[1].Trim(),
                                           addressData[2].Trim(), addressData[3].Trim());
            }
            else if (line.StartsWith("Speaker: "))
            {
                speaker = line.Substring(9);
            }
            else if (line.StartsWith("Capacity: "))
            {
                int.TryParse(line.Substring(10), out capacity);
            }
            else if (line.StartsWith("RSVP Email: "))
            {
                rsvpEmail = line.Substring(12);
            }
            else if (line.StartsWith("Weather Forecast: "))
            {
                weatherForecast = line.Substring(19);
            }
            else if (line == "--- END ---")
            {
                // Create event instance based on the event type
                switch (eventType)
                {
                    case "Lecture Event":
                        currentEvent = new LectureEvent(eventTitle, eventDescription, eventDate, eventTime,
                                                        eventAddress, speaker, capacity);
                        break;
                    case "Reception Event":
                        currentEvent = new ReceptionEvent(eventTitle, eventDescription, eventDate, eventTime,
                                                          eventAddress, rsvpEmail);
                        break;
                    case "Outdoor Gathering Event":
                        currentEvent = new OutdoorGatheringEvent(eventTitle, eventDescription, eventDate, eventTime,
                                                                 eventAddress, weatherForecast);
                        break;
                    default:
                        Console.WriteLine($"Unknown event type: {eventType}");
                        break;
                }

                // Add event to the list
                if (currentEvent != null)
                {
                    events.Add(currentEvent);
                }

                // Reset variables for the next event
                currentEvent = null;
                eventType = null;
                eventTitle = null;
                eventDescription = null;
                eventDate = DateTime.MinValue;
                eventTime = TimeSpan.Zero;
                eventAddress = null;
                speaker = null;
                capacity = 0;
                rsvpEmail = null;
                weatherForecast = null;
            }
        }

        // Print the available event titles with numbers
        Console.WriteLine("Available Event Titles:");
        for (int i = 0; i < eventTitles.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {eventTitles[i]}");
        }

        // Prompt the user to choose an event title by number
        Console.WriteLine("\nPlease enter the number of the event title to print its details (or enter 'all' to print all events, or 'quit' to exit):");
        string userInput = Console.ReadLine();
        Console.Clear();

        // Process user input
        while (!userInput.Equals("quit", StringComparison.OrdinalIgnoreCase))
        {
            if (userInput.Equals("all", StringComparison.OrdinalIgnoreCase))
            {
                // Print details of all events
                PrintAllEvents(events);
            }
            else
            {
                // Parse user input as a number
                if (int.TryParse(userInput, out int eventNumber))
                {
                    // Check if the event number is within the valid range
                    if (eventNumber > 0 && eventNumber <= eventTitles.Count)
                    {
                        // Get the corresponding event title
                        string chosenEventTitle = eventTitles[eventNumber - 1];

                        // Find the event with the chosen title
                        Event chosenEvent = events.Find(eventObj => eventObj.GetEventTitle().Equals(chosenEventTitle, StringComparison.OrdinalIgnoreCase));

                        // Print the event details if found, otherwise display an error message
                        if (chosenEvent != null)
                        {
                            Console.WriteLine("------------------------------------------------------------------------------");
                            Console.WriteLine("Event Details:");
                            Console.WriteLine("------------------------------------------------------------------------------");
                            Console.WriteLine("Standard Details:\n" + chosenEvent.GetStandardDetails());
                            Console.WriteLine("\nFull Details:\n" + chosenEvent.GetFullDetails());
                            Console.WriteLine("\nShort Description:\n" + chosenEvent.GetShortDescription());
                            Console.WriteLine("------------------------------------------------------------------------------");
                            Console.WriteLine("------------------------------------------------------------------------------");
                        }
                        else
                        {
                            Console.WriteLine("Invalid event title. Please choose an event from the available list.");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Invalid event number. Please choose a number from the available list.");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input. Please choose below");
                }
            }

            Console.WriteLine();
            // Print the available event titles with numbers
            Console.WriteLine("Available Event Titles:");
            for (int i = 0; i < eventTitles.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {eventTitles[i]}");
            }

            // Prompt the user to choose another event title or quit
            Console.WriteLine("\nPlease enter the number of the event title to print its details (or enter 'all' to print all events, or 'quit' to exit):");
            userInput = Console.ReadLine();
            Console.Clear();
        }

        Console.WriteLine("Program closed.");
    }
}
