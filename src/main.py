from manage_books import new_list, add_book_to_list, print_books, parse_genre, search_by_author, search_by_genre, search_by_isbn, search_by_title, search_by_upc, sort_books
from book import Book
from file_operations import write_file, read_file

def main():
    filename = "booklist.csv"
    book_list = new_list()

    # main loop
    while True:
        user_input = input("\nAction? (list, save, load, add, sort, search, quit)\n").lower()

        match user_input:
            case "quit":
                break
            case "exit":
                break
            case "list":
                print_books(book_list)
            case "load":
                book_list = read_file(filename)
            case "save":
                write_file(book_list, filename)
            case "add":
                title = input("Title: ")
                author = input("Author: ")
                genre_text = input("Genre: ").lower()
                genre = parse_genre(genre_text)
                upc = input("UPC: ")
                if not upc:
                    upc = None
                    isbn = input("ISBN: ")
                else:
                    isbn = None
                
                new_book = Book(title, author, genre, upc, isbn)
                add_book_to_list(book_list, new_book)
            case "search":
                search_by = input("Search by (title, author, genre, upc, isbn)? ").lower()
                search_term = input("Enter search term: ").lower()
                match search_by:
                    case "title":
                        print_books(search_by_title(book_list, search_term))
                    case "author":
                        print_books(search_by_author(book_list, search_term))
                    case "genre":
                        print_books(search_by_genre(book_list, search_term))
                    case "upc":
                        print_books(search_by_upc(book_list, search_term))
                    case "isbn":
                        print_books(search_by_isbn(book_list, search_term))
                    case _:
                        print("Invalid search type")
                        continue
            case "sort":
                sort_by = input("Sort by which field? ").lower()
                book_list = sort_books(book_list, sort_by)

if __name__ == "__main__":
    main()
