The provided program is an event management system that allows users to store and manage different types of events. It demonstrates the use of inheritance in object-oriented programming.

Here's an explanation of the modified program's components and how inheritance is used:

1. Address Class:
   - This class represents the address details of an event. It has properties for street, city, state, and country.
   - The class has a constructor to initialize the address details.
   - The `ToString()` method is overridden to provide a formatted string representation of the address.

2. Event Class (Base Class):
   - This is the base class for all types of events.
   - It has private fields for event title, event description, event date, event time, and event address.
   - The class has a constructor to initialize the common event details.
   - It provides methods to get standard details, full details, short description, and the event title.
   - The `GetFullDetails()` method is marked as `virtual` to allow derived classes to override it and provide additional details specific to each event type.
   - The `GetShortDescription()` method formats and returns a short description of the event.

3. LectureEvent Class (Derived from Event):
   - This class represents a lecture event, which is a specific type of event.
   - It extends the base Event class and adds additional fields for speaker and capacity.
   - The class has a constructor to initialize the lecture event details.
   - The `GetFullDetails()` method is overridden to include the lecture-specific details in addition to the base event details.

4. ReceptionEvent Class (Derived from Event):
   - This class represents a reception event, which is another specific type of event.
   - It extends the base Event class and adds an additional field for RSVP email.
   - The class has a constructor to initialize the reception event details.
   - The `GetFullDetails()` method is overridden to include the reception-specific details in addition to the base event details.

5. OutdoorGatheringEvent Class (Derived from Event):
   - This class represents an outdoor gathering event, which is another specific type of event.
   - It extends the base Event class and adds an additional field for weather forecast.
   - The class has a constructor to initialize the outdoor gathering event details.
   - The `GetFullDetails()` method is overridden to include the outdoor gathering-specific details in addition to the base event details.

6. Program Class:
   - This class contains the main entry point of the program.
   - It includes a static method `PrintAllEvents()` to print the details of all events in the provided list.
   - In the `Main()` method, the program reads event data from a file and processes each line to create instances of different event types.
   - The program stores the created events in a list and also keeps track of event titles.
   - It prompts the user to choose an event title or "all" to print the details of a specific event or all events, respectively.
   - Based on the user input, it retrieves the chosen event from the list and displays its details using the appropriate methods.
   - The program continues to prompt the user until the user inputs "quit" to exit the program.

Inheritance is used in this program to create a hierarchy of event classes. The base `Event` class provides common properties and methods that are shared among all events. Derived classes such as `LectureEvent`, `ReceptionEvent`, and `OutdoorGatheringEvent` inherit from the base class and extend it with additional properties and methods specific to their respective event types. This inheritance relationship allows the program to handle different event types in a unified manner while providing flexibility to customize behavior and details based on the specific event type.