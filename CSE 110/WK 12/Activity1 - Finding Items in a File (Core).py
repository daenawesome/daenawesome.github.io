with open("books_and_chapters.txt") as f:
  max_chapters = 0
  max_book = ""
  for line in f:
    book, chapters, scripture_type = line.strip().split(":")
    if scripture_type == "Old Testament":
      print(f"Scripture: {scripture_type}, Book: {book}, Chapters: {chapters}")
    if int(chapters) > max_chapters:
      max_chapters = int(chapters)
      max_book = book
  print(f"The largest number of chapters in the scripture is {max_chapters} in the book of {max_book}")

