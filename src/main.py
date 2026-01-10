from manage_books import new_list, add_book, print_books
from book import Book, Genre
from file_operations import write_file, read_file

def main():
    # book_list = new_list()
    # book = Book("Python One-Liners", "Christian Mayer", Genre.COMPUTERS, None, 9781718500501)
    # add_book(book_list, book)
    # print_books(book_list)

    # write_file(book_list, "booklist.csv")
    
    book_list = read_file("booklist.csv")
    print_books(book_list
                
                )
if __name__ == "__main__":
    main()
