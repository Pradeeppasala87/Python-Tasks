class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def display(self):
        print(self.title, self.author, self.size)

e = EBook("Python Basics", "John", "5MB")
e.display()
