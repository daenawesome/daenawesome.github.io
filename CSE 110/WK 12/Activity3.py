def get_books_by_volume(volume):
    with open("books_and_chapters.txt") as f:
        books = []
        for line in f:
            book, chapters, scripture_type = line.strip().split(":")
            if scripture_type == volume:
                books.append((book, chapters))
        return books

def get_books_by_volume_sorted(volume):
    books = get_books_by_volume(volume)
    return sorted(books)

volume = input("Which volume of scripture would you like to learn about? (Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price) ")

if volume not in ["Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", "Pearl of Great Price"]:
    print("Invalid volume, please try again.")
else:
    print("Books in the", volume + ":")
    books = get_books_by_volume_sorted(volume)
    for book in books:
        print(f"Book: {book[0]}, Chapters: {book[1]}")

"""
  I created two new functions 'get_books_by_volume' and 'get_books_by_volume_sorted'. The first function 'get_books_by_volume' takes a 
  volume as input and returns the books in the respective volume with the number of chapters. The second function 'get_books_by_volume_sorted' 
  takes the volume as input and returns the books in the respective volume in alphabetical order with the number of chapters. At the end, we 
  ask the user for the volume, check if the input is valid or not and if the input is valid, we call the function 'get_books_by_volume_sorted' or 'get_books_by_volume'
"""