grade = int(input("Please enter your grade percentage: "))

# Determine letter grade
letter = ""
if grade >= 90:
  letter = "A"
elif grade >= 80:
  letter = "B"
elif grade >= 70:
  letter = "C"
elif grade >= 60:
  letter = "D"
else:
  letter = "F"

# Determine sign
sign = ""
if letter != "A" and letter != "F":
  if grade % 10 >= 7:
    sign = "+"
  elif grade % 10 < 3:
    sign = "-"

# Print letter grade with sign
print(f"Your letter grade is {letter}{sign}.")

# Determine if the user passed the course
if grade >= 70:
  print("Congratulations, you passed the course!")
else:
  print("Keep trying, you'll pass next time.")
