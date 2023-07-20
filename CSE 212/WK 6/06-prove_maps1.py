"""
CSE212 
(c) BYU-Idaho
06-Prove

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

#############
# Problem 1 #
#############

class Translator:
    """
    This class provides the capability of a translator. A
    Python Dictionary is used to keep track of the mapping
    of words from one language to another language. You should
    assume that there is only one translation for every
    word (and vice versa).
    """

    def __init__(self):
        """
        Initialize the Python Dictionary to store word mappings
        """
        self.words = dict()

    def add_word(self, from_word, to_word):
        """
        Add the translation from 'from_word' to 'to_word'
        For example, in an English to German dictionary:
        my_translator.add_word("book", "buch")
        """
        self.words[from_word] = to_word

    def translate(self, from_word):
        """
        Translate a word and return the result. If the word
        cannot be translated, then "???" is returned.
        For example, in an English to German dictionary:
        german_word = my_translator.translate("book")
        """
        return self.words.get(from_word, "???")
        # if from_word in self.words:              # The `translate` function checks if the given `from_word` exists 
        #     return self.words[from_word]         # as a key in the `words` dictionary. If it does, it returns the
        # else:                                    # corresponding translation (value). Otherwise, it returns "???".
        #     return "???"

# Sample Test Cases (may not be comprehensive)
print("\n=========== PROBLEM 1 TESTS ===========")
english_to_german = Translator()
english_to_german.add_word("House", "Haus")
english_to_german.add_word("Car", "Auto")
english_to_german.add_word("Plane", "Flugzeug")
print(english_to_german.translate("Car"))  # Auto
print(english_to_german.translate("Plane"))  # Flugzeug
print(english_to_german.translate("Train"))  # ???

# In the `add_word` method, I simply add a new key-value pair to the `words` dictionary. 
# The `from_word` parameter is the word in the source language, and the `to_word` parameter is the 
# translated word in the target language.

# In the `translate` method, I use the `get` method of the dictionary to retrieve the translated 
# word corresponding to the `from_word`. If the translation is available, it will be returned. Otherwise, 
# if the translation is not found in the dictionary, the default value "???" is returned.

#############
# Problem 2 #
#############

def summarize_degrees(filename):
    """
    Read a census file and summarize the degrees (education)
    earned by those contained in the file.  The summary
    should be stored in a dictionary where the key is the
    degree earned and the value is the number of people that 
    have earned that degree.  The degree information is in
    the 4th column of the file.  There is no header row in the
    file.
    """
    degrees = dict()
    with open(filename) as file_in:
        for line in file_in:
            fields = line.split(",")    # Reads the file line by line and splits each line into fields using the comma as the delimiter.
    
    # ADD YOUR CODE HERE
            degree = fields[3].strip()  # Get the degree from the 4th column by removing any leading or trailing whitespace using the 'strip()' method.
            if degree in degrees:       # Checks if the degree is already present in the degrees dictionary. 
                degrees[degree] += 1    # Increment the count for an existing degree
            else:
                degrees[degree] = 1     # Initialize the count for a new degree with the count initialized to 1
                
    # Sort the degrees alphabetically
    sorted_degrees = sorted(degrees.items())
    
    # Print
    print("Sorted:")
    for degree, count in sorted_degrees:
        print(f"{degree}: {count}")
        
    return degrees

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 2 TESTS ===========")

# Alt print
degrees = summarize_degrees("census.txt")

# print(summarize_degrees("census.txt")) # You might need to add a path for the file
print("\nUnsorted:")
print(degrees)
# Results may be in a different order:
# {'Bachelors': 5355, 'HS-grad': 10501, '11th': 1175, 
# 'Masters': 1723, '9th': 514, 'Some-college': 7291, 
# 'Assoc-acdm': 1067, 'Assoc-voc': 1382, '7th-8th': 646, 
# 'Doctorate': 413, 'Prof-school': 576, '5th-6th': 333, 
# '10th': 933, '1st-4th': 168, 'Preschool': 51, 
# '12th': 433}  

#############
# Problem 3 #
#############

def is_anagram(word1, word2):
    """
    Determine if 'word1' and 'word2' are anagrams.  An anagram
    is when the same letters in a word are re-organized into a 
    new word.  A Python dictionary is used to solve the problem.

    Examples:
    is_anagram("CAT","ACT") would return True
    is_anagram("DOG","GOOD") would return False because GOOD has 2 O's

    Important Note: When determining if two words are anagrams, you
    should ignore any spaces.  You should also ignore cases.  For 
    example, 'Ab' and 'Ba' should be considered anagrams

    Reminder: You can access a letter by index in a Python string by 
    using the [] notation.
    """
    # Remove spaces and convert words to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # If the lengths are different, they cannot be anagrams
    if len(word1) != len(word2):
        return False

    # Create dictionaries to store the frequency of each letter in both words
    freq1 = {}
    freq2 = {}

    # Count the frequency of each letter in word1
    for letter in word1:
        freq1[letter] = freq1.get(letter, 0) + 1
        # if letter in freq1:
        #     freq1[letter] += 1
        # else:
        #     freq1[letter] = 1

    # Count the frequency of each letter in word2
    for letter in word2:
        freq2[letter] = freq2.get(letter, 0) + 1
        # if letter in freq2:
        #     freq2[letter] += 1
        # else:
        #     freq2[letter] = 1

    # Compare the dictionaries
    return freq1 == freq2

# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 3 TESTS ===========")
# print(is_anagram("CAT","ACT")) # True
# print(is_anagram("DOG", "GOOD")) # False
# print(is_anagram("AABBCCDD", "ABCD")) # False
# print(is_anagram("ABCCD","ABBCD")) # False
# print(is_anagram("BC","AD")) # False
# print(is_anagram("Ab","Ba")) # True
# print(is_anagram("A Decimal Point", "Im a Dot in Place"))  # True
# print(is_anagram("tom marvolo riddle", "i am lord voldemort")) # True
# print(is_anagram("Eleven plus Two", "Twelve Plus One")) # True
# print(is_anagram("Eleven plus One", "Twelve Plus One")) # False

# Alt print
print("Is Anagram?")
print(f"TRUE for: CAT & ACT" 
      if is_anagram("CAT","ACT") 
      else f"FALSE for: CAT & ACT")
print(f"TRUE for: DOG & GOOD" 
      if is_anagram("DOG", "GOOD") 
      else f"FALSE for: DOG & GOOD")
print(f"TRUE for: AABBCCDD & ABCD" 
      if is_anagram("AABBCCDD", "ABCD") 
      else f"FALSE for: AABBCCDD & ABCD")
print(f"TRUE for: ABCCD & ABBCD" 
      if is_anagram("ABCCD","ABBCD") 
      else f"FALSE for: ABCCD & ABBCD")
print(f"TRUE for: BC & AD" 
      if is_anagram("BC","AD") 
      else f"FALSE for: BC & AD")
print(f"TRUE for: Ab & Ba" 
      if is_anagram("Ab","Ba") 
      else f"FALSE for: Ab & Ba")
print(f"TRUE for: A Decimal Point & Im a Dot in Place" 
      if is_anagram("A Decimal Point", "Im a Dot in Place") 
      else f"FALSE for: A Decimal Point & Im a Dot in Place")
print(f"TRUE for: tom marvolo riddle & i am lord voldemort" 
      if is_anagram("tom marvolo riddle", "i am lord voldemort") 
      else f"FALSE for: tom marvolo riddle & i am lord voldemort")
print(f"TRUE for: Eleven plus Two & Twelve Plus One" 
      if is_anagram("Eleven plus Two", "Twelve Plus One") 
      else f"FALSE for: Eleven plus Two & Twelve Plus One")
print(f"TRUE for: Eleven plus One & Twelve Plus One" 
      if is_anagram("Eleven plus One", "Twelve Plus One") 
      else f"FALSE for: Eleven plus One & Twelve Plus One")

#############
# Problem 4 #
#############

class Maze:
    """
    Defines a maze using a dictionary.  The dictionary is provided by the
    user when the Maze object is created.  The dictionary will contain the
    following mapping:

    (x,y) : (left, right, up, down)

    'x' and 'y' are integers and represents locations in the maze.
    'left', 'right', 'up', and 'down' are boolean are represent valid directions

    If a direction is False, then we can assume there is a wall in that direction.
    If a direction is True, then we can proceed.  

    If there is a wall, then display "Can't go that way!".  If there is no wall,
    then the 'curr_x' and 'curr_y' values should be changed.
    """

    def __init__(self, maze_map):
        """
        Initialize the map. We assume that (1,1) is a valid location in
        the maze.
        """
        self.maze_map = maze_map
        self.curr_x = 1
        self.curr_y = 1

    def move_left(self):
        """
        Check to see if you can move left. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """  
        directions = self.maze_map[self.curr_x, self.curr_y] # Get the available directions from the maze map at the current position.
        if directions[0] == True:                            # Check if the "" direction is accessible
            self.curr_x -= 1                                 # Move the player one step to the ""
            print("You can move that way!")
        else:
            print("Can't go that way!")                      # "" direction is blocked

    def move_right(self):
        """
        Check to see if you can move right. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """          
        directions = self.maze_map[self.curr_x, self.curr_y]
        if directions[1] == True:
            self.curr_x += 1
            print("You can move that way!")
        else:
            print("Can't go that way!")
    
    def move_up(self):
        """
        Check to see if you can move up. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        directions = self.maze_map[self.curr_x, self.curr_y]
        if directions[2] == True:
            self.curr_y -= 1
            print("You can move that way!")
        else:
            print("Can't go that way!")
    
    def move_down(self):
        """
        Check to see if you can move down. If you can, then move. If you
        can't move, then display "Can't go that way!"
        """
        directions = self.maze_map[self.curr_x, self.curr_y]
        if directions[3] == True:
            self.curr_y += 1
            print("You can move that way!")
        else:
            print("Can't go that way!")
            
    ### Can also be written ###
    # Refactoring into a single method
    def move(self, direction):
        directions = self.maze_map[self.curr_x, self.curr_y]
        if directions[direction]:
            if direction == 0:  # Left
                self.curr_x -= 1
            elif direction == 1:  # Right
                self.curr_x += 1
            elif direction == 2:  # Up
                self.curr_y -= 1
            elif direction == 3:  # Down
                self.curr_y += 1
            print("You can move that way!")
        else:
            print("Can't go that way!")
            
    def move_left(self):
        self.move(0)

    def move_right(self):
        self.move(1)

    def move_up(self):
        self.move(2)

    def move_down(self):
        self.move(3)
    ### Can also be written ###
    
    def show_status(self):
        print("Current location (x={}, y={})".format(self.curr_x, self.curr_y))

# Sample Test Cases (may not be comprehensive) 
map =  {(1,1) : (False, True, False, True),
        (1,2) : (False, True, True, False),
        (1,3) : (False, False, False, False),
        (1,4) : (False, True, False, True),
        (1,5) : (False, False, True, True),
        (1,6) : (False, False, True, False),
        (2,1) : (True, False, False, True),
        (2,2) : (True, False, True, True),
        (2,3) : (False, False, True, True),
        (2,4) : (True, True, True, False),
        (2,5) : (False, False, False, False),
        (2,6) : (False, False, False, False),
        (3,1) : (False, False, False, False),
        (3,2) : (False, False, False, False),
        (3,3) : (False, False, False, False),
        (3,4) : (True, True, False, True), 
        (3,5) : (False, False, True, True),
        (3,6) : (False, False, True, False),
        (4,1) : (False, True, False, False),
        (4,2) : (False, False, False, False),
        (4,3) : (False, True, False, True),
        (4,4) : (True, True, True, False),
        (4,5) : (False, False, False, False),
        (4,6) : (False, False, False, False),
        (5,1) : (True, True, False, True),
        (5,2) : (False, False, True, True),
        (5,3) : (True, True, True, True),
        (5,4) : (True, False, True, True),
        (5,5) : (False, False, True, True),
        (5,6) : (False, True, True, False),
        (6,1) : (True, False, False, False),
        (6,2) : (False, False, False, False),
        (6,3) : (True, False, False, False),
        (6,4) : (False, False, False, False),
        (6,5) : (False, False, False, False),
        (6,6) : (True, False, False, False)}

print("\n=========== PROBLEM 4 TESTS ===========")
maze = Maze(map)
maze.show_status() # Should be at (1,1)
maze.move_up() # Error, Moving up it's a wall
maze.move_left() # Error, Moving left it's a wall
maze.move_right() # Move right from (1,1) to (2,1)
maze.move_right() # Error moving right to (2,3) blocked
maze.move_down() # Move down from (2,1) to (2,2)
maze.move_down() # Move down from (2,2) to (2,3)
maze.move_down() # Move down from (2,3) to (2,4)
maze.move_right() # Move right from (2,4) to (3,4)
maze.move_right() # Move right from (3,4) to (4,4)
maze.move_up() # Move up from (4,4) to (4,3)
maze.move_right() # Move right from (4,3) to (5,3)
maze.move_down() # Move down from (5,3) to (5,4)
maze.move_left() # Move left from (5,4) to (4,4)
maze.move_down() # Error moving down to (4,5) blocked
maze.move_right() # Move right from (4,4) to (5,4)
maze.move_down() # Move down from (5,4) to (5,5)
maze.move_down() # Move down from (5,5) to (5,6)
maze.move_right() # Move right from (5,6) to (6,6)
maze.show_status() # Should be at (6,6)

#############
# Problem 5 #
#############

import requests  

def earthquake_daily_summary():
   
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary

    # ADD YOUR CODE HERE
    
    # Header
    print("Earthquake Locations                                | Magnitude   |")
    print("-------------------------------------------------------------------")

    # Iterate over each earthquake and print location and magnitude
    for earthquake in data['features']:
        # Extract the place and magnitude attributes from the earthquake properties
        place = earthquake['properties']['place']
        mag = earthquake['properties']['mag']
        # print(f"{place} - Mag {mag}")
        print(f"{place.ljust(52)}| {str(mag).rjust(11)} |") # used ljust & rjust for alignment, str(mag) to convert to string

# Sample Test Cases (may not be comprehensive) 
print("\n========================= PROBLEM 5 TESTS =========================")  
earthquake_daily_summary()

# Sample output from the function.  Number of earthquakes, places, and magnitudes will vary.

# 1km NE of Pahala, Hawaii - Mag 2.36
# 58km NW of Kandrian, Papua New Guinea - Mag 4.5
# 16km NNW of Truckee, California - Mag 0.7
# 9km S of Idyllwild, CA - Mag 0.25
# 14km SW of Searles Valley, CA - Mag 0.36
# 4km SW of Volcano, Hawaii - Mag 1.99