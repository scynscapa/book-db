from enum import Enum

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

class Book():
    def __init__(self, title, author, genre, upc = None, isbn = None):
        self.title = title
        self.author = author
        self.upc = upc
        self.isbn = isbn
        self.genre = genre

    def __repr__(self):
        return f'"{self.title}", {self.author}, -{self.genre.value}'
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        if self.title == other.title and self.author == other.author and self.upc == other.upc and self.genre == other.genre:
            return True
        return False