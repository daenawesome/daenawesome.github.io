import time

print('Hello, please enter the required information.')

print()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email_address = input("Enter your email address: ").lower()
phone_number = input("Enter your phone number: ")
job_title = input("Enter your job title: ")
id_number = input("Enter your ID number: ")
hair_color = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")
month_started = input("Enter the month you started: ")
advanced_training = input("Have you completed advanced training (yes/no)? ")

# Format the output
output = f"\nThe ID Card is:\n\u001b[32m--------------------------------------------------\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.capitalize()}\nID: {id_number}\n\n{email_address}\n{phone_number}\n\nHair: {hair_color.capitalize():<18}Eyes: {eye_color.capitalize()}\nMonth: {month_started.capitalize():<17}Training: {advanced_training.capitalize()}\n--------------------------------------------------\u001b[0m"

# Display a loading message
print("\nLoading", end="")

# Create a loading animation
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(1)

# Display the output
print("\n" + output)

# Input to Exit
input("\nPress ENTER to exit")

"""
I used the ':<' alignment specifier in the string formatting syntax. 
The ':<' specifier left-aligns the text and pads it with spaces 
to the specified width.

For example, to left-align the 'hair_color' and 'eye_color' variables 
and pad them with spaces to a width of 18 characters Similarly, to 
left-align the 'month_started' and 'advanced_training' variables 
and pad them with spaces to a width of 17 characters

Added a loading message and creates a loading animation 
by printing dots and delaying the program for 1 second
using the time.sleep() function. Finally, it displays 
the output to the user.
"""