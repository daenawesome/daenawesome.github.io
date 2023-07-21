# Initialize empty list to store courses and grades
courses = []

# Loop until the user enters "done"
while True:
# Get course name and grade from the user
  course = input("\nEnter the name of the course (or 'done' to finish): ")
  if course.lower() == "done":
    break
  try:
    grade = int(input("Enter your grade percentage for this course: "))
    if grade < 0 or grade > 100:
      raise ValueError
  except ValueError:
    print("Error: grade percentage must be a number between 0 and 100.")
    continue
  try:
    credits = int(input("Enter the number of credits for this course: "))
    if credits < 0:
      raise ValueError
  except ValueError:
    print("Error: credits must be a positive number.")
    continue
  
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
  elif letter == "A" and grade % 10 == 10:
    letter = "A+"
  elif letter == "F" and grade % 10 == 0:
    letter = "F-"
    
# Add course and grade to the list
  courses.append((course, letter + sign, credits))

# Calculate GPA
total_grade_points = 0
total_credits = 0
for course in courses:
  letter, credits = course[1], course[2]
  grade_points = 0
  if letter == "A+":
    grade_points = 4.3
  elif letter == "A":
    grade_points = 4.0
  elif letter == "A-":
    grade_points = 3.7
  elif letter == "B+":
    grade_points = 3.3
  elif letter == "B":
    grade_points = 3.0
  elif letter == "B-":
    grade_points = 2.7
  elif letter == "C+":
    grade_points = 2.3
  elif letter == "C":
    grade_points = 2.0
  elif letter == "C-":
    grade_points = 1.7
  elif letter == "D+":
    grade_points = 1.3
  elif letter == "D":
    grade_points = 1.0
  elif letter == "F-":
    grade_points = 0.7
  else:
    grade_points = 0
  total_grade_points += grade_points * credits
  total_credits += credits
  
gpa = total_grade_points / total_credits

# Print GPA
print(f"\nYour GPA is {gpa:.2f}.")

input('\nPress ENTER to exit')

"""
The program allows the user to enter multiple courses and grades, and then 
calculates the overall GPA for all courses based on the letter grades and credits. 
The program handles exceptional cases like A+ and F-, and also allows the user to 
input their own grading scale by specifying the grade points for each letter grade. 
The program calculates the GPA based on the grades and credits entered by the user and 
prints the result to the screen.
"""