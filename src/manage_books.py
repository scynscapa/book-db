from book import Book, Genre


def new_list():
    return list()

def add_book_to_list(book_list, book):
    book_list.append(book)

def print_books(book_list):
    # check for empty list
    if book_list == list():
        print("Empty list")

    for book in book_list:
        print(book)

def parse_genre(genre_text):
    match genre_text:
        case "Genre.SCIFI" | "Scifi":
            genre = Genre.SCIFI
        case "Genre.FANTASY" | "Fantasy":
            genre = Genre.FANTASY
        case "Genre.THRILLER" | "Thriller":
            genre = Genre.THRILLER
        case "Genre.MYSTERY" | "Mystery":
            genre = Genre.MYSTERY
        case "Genre.HORROR" | "Horror":
            genre = Genre.HORROR
        case "Genre.ROMANCE" | "Rommance":
            genre = Genre.ROMANCE
        case "Genre.YOUNGADULT" | "Young Adult":
            genre = Genre.YOUNGADULT
        case "Genre.NONFICTION" | "Nonfiction" | "Non-fiction":
            genre = Genre.NONFICTION
        case "Genre.COMPUTERS" | "Computers":
            genre = Genre.COMPUTERS
        case _:
            genre = Genre.DEFAULT
    
    return genre