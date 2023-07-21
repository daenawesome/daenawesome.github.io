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
reads through the file line by line using a 'for' loop. For each line, it first removes any 
leading and trailing whitespace using the 'strip()' method. Then it splits the line into parts 
using the 'split()' function, which takes a separator as an argument. In this case, the separator 
is a single space (" "). Then it gets the name, ID number, job title, and salary by assigning 
them to their corresponding variables. Next, it calculates the paycheck amount by dividing the 
salary by 24 (assuming paid twice a month). It then checks if the employee is an engineer by 
comparing their job title to the string "Engineer". If they are an engineer, it adds $1000 bonus 
to the paycheck. Finally, it displays the name, ID number, job title, and paycheck amount using 
the 'print()' function with string formatting.

paycheck amounts are displayed with two decimal places using the ':.2f' format specifier.
"""