from book import Book, Genre


def new_list():
    return list()

def add_book(book_list, book):
    book_list.append(book)

def print_books(book_list):
    for book in book_list:
        print(book)

