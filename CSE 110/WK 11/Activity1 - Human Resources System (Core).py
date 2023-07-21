# Open the HR System file
with open("hr_system.txt", "r") as file:
    # Read through the file line by line
    for line in file:
        # Display the whole line
        print(line)
        # Split the line into parts
        parts = line.split(" ")
        # Display only the name
        print("Name: " + parts[0])
        # Get the name and the job title, and display them
        name = parts[0]
        title = parts[2]
        print("Name: " + name + ", Title: " + title)


"""
same but written diff
"""