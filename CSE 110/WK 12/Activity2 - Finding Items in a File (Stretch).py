volume = input("Which volume of scripture would you like to learn about? (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price) ")
with open("books_and_chapters.txt") as f:
  max_chapters = 0
  max_book = ""
  for line in f:
    book, chapters, scripture_type = line.strip().split(":")
    if scripture_type == volume:
      if int(chapters) > max_chapters:
        max_chapters = int(chapters)
        max_book = book
  print(f"The largest number of chapters in the {volume} is {max_chapters} in the book of {max_book}")
