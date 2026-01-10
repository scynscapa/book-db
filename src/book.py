from enum import Enum

# when adding, add to match statement in parse_file in file_operations.py
class Genre(Enum):
    SCIFI = "Science Fiction"
    FANTASY = "Fantasy"
    THRILLER = "Thriller"
    MYSTERY = "Mystery"
    HORROR = "Horror"
    ROMANCE = "Romance"
    YOUNGADULT = "Young Adult"
    NONFICTION = "Non-fiction (general)"
    COMPUTERS = "Computers"
    DEFAULT = "Default (should not see)"

class Book():
    def __init__(self, title, author, genre, upc = None, isbn = None):
        self.title = title
        self.author = author
        self.upc = upc
        self.isbn = isbn
        self.genre = genre

    # for writing to file
    def to_string(self):
        return f'{self.title}, {self.author}, {self.genre}, {self.upc}, {self.isbn}'

    def __repr__(self):
        return f'{self.title}, {self.author}, {self.genre.value}'
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        if self.title == other.title and self.author == other.author and self.upc == other.upc and self.genre == other.genre:
            return True
        return False