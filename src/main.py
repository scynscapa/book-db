from manage_books import new_list, add_book_to_list, print_books, parse_genre
from book import Book, Genre
from file_operations import write_file, read_file

def main():
    filename = "booklist.csv"

    # main loop
    book_list = new_list()
    while True:
        user_input = input("\nAction? (list, save, load, add, quit)\n")

        match user_input:
            case "quit":
                break
            case "exit":
                break
            case "list":
                print_books(book_list)
            case "load":
                book_list = read_file(filename)
                print(f"{len(book_list)} book(s) loaded")
            case "save":
                write_file(book_list, filename)
                print(f"Wrote {len(book_list)} book(s) to file {filename}")
            case "add":
                title = input("Title: ")
                author = input("Author: ")
                genre_text = input("Genre: ")
                upc = input("UPC: ")
                if not upc:
                    upc = None
                    isbn = input("ISBN: ")
                else:
                    isbn = None
                
                genre = parse_genre(genre_text)

                new_book = Book(title, author, genre, upc, isbn)
                add_book_to_list(book_list, new_book)


if __name__ == "__main__":
    main()
