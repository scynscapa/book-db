from book import Book, Genre


def new_list():
    return list()

def add_book_to_list(book_list, book):
    book_list.append(book)

def print_books(book_list):
    # check for empty list
    if book_list == list() or not book_list:
        print("No books found")
        return

    for book in book_list:
        print(book)
        print("----------------------")

def parse_genre(genre_text):
    match genre_text:
        case "Genre.SCIFI" | "scifi" | "science fiction":
            genre = Genre.SCIFI
        case "Genre.FANTASY" | "fantasy":
            genre = Genre.FANTASY
        case "Genre.THRILLER" | "thriller":
            genre = Genre.THRILLER
        case "Genre.MYSTERY" | "mystery":
            genre = Genre.MYSTERY
        case "Genre.HORROR" | "horror":
            genre = Genre.HORROR
        case "Genre.ROMANCE" | "rommance":
            genre = Genre.ROMANCE
        case "Genre.YOUNGADULT" | "young adult":
            genre = Genre.YOUNGADULT
        case "Genre.NONFICTION" | "nonfiction" | "non-fiction":
            genre = Genre.NONFICTION
        case "Genre.COMPUTERS" | "computers":
            genre = Genre.COMPUTERS
        case _:
            genre = Genre.DEFAULT
    return genre

def list_genres():
    print("Valid Genres:")
    print("-------------")
    for genre in Genre:
        if genre is not Genre.DEFAULT:
            print(genre.value)

def search_by_author(book_list, search):
    return_list = list()
    for book in book_list:
        if search in book.author.lower():
            return_list.append(book)
    return return_list

def search_by_title(book_list, search):
    return_list = list()
    for book in book_list:
        if search in book.title.lower():
            return_list.append(book)
    return return_list

def search_by_genre(book_list, search):
    return_list = list()
    genre = parse_genre(search)
    if genre == Genre.DEFAULT:
        print("Invalid genre")
        list_genres()
        return
    for book in book_list:
        if genre == book.genre:
            return_list.append(book)
    return return_list

def search_by_upc(book_list, search):
    return_list = list()
    for book in book_list:
        if search in book.upc:
            return_list.append(book)
    return return_list

def search_by_isbn(book_list, search):
    return_list = list()
    for book in book_list:
        if search in book.isbn:
            return_list.append(book)
    return return_list

def sort_books(book_list, sort_by):
    match sort_by:
        case "author":
            sorted_books = sorted(book_list, key = lambda book: book.author.split()[-1])
            return sorted_books            
        case "title":
            sorted_books = sorted(book_list, key = lambda book: book.title)
            return sorted_books
        case "genre":
            sorted_books = sorted(book_list, key = lambda book: book.genre.value)
            return sorted_books
        case "isbn":
            sorted_books = sorted(book_list, key = lambda book: book.isbn)
            return sorted_books
        case "upc":
            sorted_books = sorted(book_list, key = lambda book: book.upc)
            return sorted_books
        case _:
            return book_list