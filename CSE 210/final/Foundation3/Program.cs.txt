using System;

// The program creates instances of different types of events (lecture, reception, outdoor gathering) and generates 
// marketing messages with standard details, full details, and short descriptions for each event.

// Address class to encapsulate the address details
public class Address
{
    public string Street { get; set; }
    public string City { get; set; }
    public string State { get; set; }
    public string Country { get; set; }

    // Constructor to initialize address details
    public Address(string street, string city, string state, string country)
    {
        Street = street;
        City = city;
        State = state;
        Country = country;
    }

    // Override the ToString() method to provide a string representation of the address
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

    // Constructor to initialize event details
    public Event(string title, string description, DateTime date, TimeSpan time, Address address)
    {
        eventTitle = title;
        eventDescription = description;
        eventDate = date;
        eventTime = time;
        eventAddress = address;
    }

    // Get the standard details of the event
    public string GetStandardDetails()
    {
        return $"Event Title: {eventTitle}\n" +
               $"Description: {eventDescription}\n" +
               $"Date: {eventDate.ToShortDateString()}\n" +
               $"Time: {eventTime}\n" +
               $"Address: {eventAddress}";
    }

    // Get the full details of the event
    public virtual string GetFullDetails()
    {
        return GetStandardDetails();
    }

    // Get a short description of the event
    public string GetShortDescription()
    {
        return $"Type: {GetType().Name}\n" +
               $"Event Title: {eventTitle}\n" +
               $"Date: {eventDate.ToShortDateString()}";
    }
}

// Lecture Event derived class
public class LectureEvent : Event
{
    private string speaker;
    private int capacity;

    // Constructor to initialize lecture event details
    public LectureEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                        string speaker, int capacity)
        : base(title, description, date, time, address)
    {
        this.speaker = speaker;
        this.capacity = capacity;
    }

    // Override the GetFullDetails() method to include lecture event details
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

    // Constructor to initialize reception event details
    public ReceptionEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                          string rsvpEmail)
        : base(title, description, date, time, address)
    {
        this.rsvpEmail = rsvpEmail;
    }

    // Override the GetFullDetails() method to include reception event details
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

    // Constructor to initialize outdoor gathering event details
    public OutdoorGatheringEvent(string title, string description, DateTime date, TimeSpan time, Address address,
                                 string weatherForecast)
        : base(title, description, date, time, address)
    {
        this.weatherForecast = weatherForecast;
    }

    // Override the GetFullDetails() method to include outdoor gathering event details
    public override string GetFullDetails()
    {
        return $"{base.GetFullDetails()}\n" +
               $"Type: Outdoor Gathering Event\n" +
               $"Weather Forecast: {weatherForecast}";
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Create event instances
        var lectureEvent = new LectureEvent("CSE 210 Deep Dive", "Exploring the latest advancements in Programming Classes",
                                            new DateTime(2023, 5, 30), new TimeSpan(15, 0, 0),
                                            new Address("123 Main Street", "New York", "NY", "USA"),
                                            "John Doe", 100);

        var receptionEvent = new ReceptionEvent("Networking Mixer", "Join us for an evening of networking and fun!",
                                                new DateTime(2023, 6, 15), new TimeSpan(18, 30, 0),
                                                new Address("456 Elm Street", "Los Angeles", "CA", "USA"),
                                                "rsvp@example.com");

        var outdoorEvent = new OutdoorGatheringEvent("Summer Picnic", "Enjoy a day of outdoor activities and delicious food!",
                                                      new DateTime(2023, 7, 10), new TimeSpan(11, 0, 0),
                                                      new Address("789 Oak Street", "San Francisco", "CA", "USA"),
                                                      "Sunny skies");

        // Generate marketing messages for each event
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("LECTURE EVENT");
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("Standard Details:\n" + lectureEvent.GetStandardDetails());
        Console.WriteLine("\nFull Details:\n" + lectureEvent.GetFullDetails());
        Console.WriteLine("\nShort Description:\n" + lectureEvent.GetShortDescription());
        Console.WriteLine("");
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("RECEPTION EVENT");
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("Standard Details:\n" + receptionEvent.GetStandardDetails());
        Console.WriteLine("\nFull Details:\n" + receptionEvent.GetFullDetails());
        Console.WriteLine("\nShort Description:\n" + receptionEvent.GetShortDescription());
        Console.WriteLine("");
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("OUTDOOR GATHERING EVENT");
        Console.WriteLine("-----------------------------------------");
        Console.WriteLine("Standard Details:\n" + outdoorEvent.GetStandardDetails());
        Console.WriteLine("\nFull Details:\n" + outdoorEvent.GetFullDetails());
        Console.WriteLine("\nShort Details:\n" + outdoorEvent.GetShortDescription());

        Console.ReadLine();
    }
}
