with open("books_and_chapters.txt") as f:
    for line in f:
        book, chapters, scripture = line.strip().split(":")
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
max_chapters = 0
with open("books_and_chapters.txt") as f:
    for line in f:
        _, chapters, _ = line.strip().split(":")
        chapters = int(chapters)
        if chapters > max_chapters:
            max_chapters = chapters
print(max_chapters)
max_chapters = 0
max_book = ""
with open("books_and_chapters.txt") as f:
    for line in f:
        book, chapters, _ = line.strip().split(":")
        chapters = int(chapters)
        if chapters > max_chapters:
            max_chapters = chapters
            max_book = book
print(max_book)
