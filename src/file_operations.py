import sys
from book import Book, Genre
from manage_books import new_list, parse_genre


def write_file(book_list, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for book in book_list:
                f.write(book.to_string())
                f.write("\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Input file not found")
    except Exception as e:
        print(f"An error occured: {e}")
    
    book_list = parse_file(content)
    return book_list

def parse_file(content):
    book_list = new_list()
    lines = content.split("\n")
    for line in lines:
        if line == "":
            continue
        title, author, genre_text, upc, isbn = line.split(",")

        genre = parse_genre(genre_text)
        
        book = Book(title, author, genre, upc, isbn)
        book_list.append(book)
    
    return book_list


