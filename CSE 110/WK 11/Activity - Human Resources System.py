# Open the HR System file
with open("hr_system.txt", "r") as file:
    # Read through the file line by line
    for line in file:
        # Display the whole line
        print(line)
        # Split the line into parts
        parts = line.split()
        # Display only the name
        print("Name: " + parts[0])
        # Get the name and job title
        name = parts[0]
        job_title = parts[2]
        # Display the name and job title
        print("Name: " + name + ", Title: " + job_title)



"""
The first line opens the file "hr_system.txt" in "read" mode and assigns it to the variable "file".
The for loop iterates through each line of the file.
The first print statement displays the whole line.
The line.split() method splits the line into parts using the space as a delimiter and assigns the list of parts to the variable "parts".
The second print statement displays only the name from the parts list.
Then it gets the name and job title from parts list and assigns them to variables.
The last print statement displays the name and job title by concatenating the variables.

Please note that the above code is just an example and you may need to adjust it according to your specific requirements and the structure of your data file.
"""