# First ask them for the initial number
number = int(input("Please type a positive number: "))

# Check if it's negative, if so, enter the loop and keep going
# as long as it is negative.
while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")


# For this example, I could have asked them the first question before the loop
# as I did in the other example, but instead, because the question is identical
# to the one that I'll ask in the loop, I'm going to change the code so
# that it waits until its inside the loop to ask for the first time. In order
# to do this, I need to define my variable before the list and assign it
# to something that will allow it to enter the loop the first time. In my case,
# I choose "", but it could have been anything other than "yes".
answer = ""

while answer != "yes":
    # This could be written as: 'while answer == "no":'
    # The difference would be how it treats other words, besides yes and no
    answer = input("May I have a piece of candy? ")

print ("Thank you.")
