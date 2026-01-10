from manage_books import new_list, add_book
from book import Book, Genre

def main():
    book_list = new_list()
    book = Book("Python One-Liners", "Christian Mayer", Genre.COMPUTERS, None, 9781718500501)
    add_book(book_list, book)

    for b in book_list:
        print(b)
    return

if __name__ == "__main__":
    main()
