class Book:
    def __init__(self, title, count = 1):
        self._title = title
        self._totalCount = count
        self._borrowedCount = 0

    def AddEx(self):
        self._totalCount += 1

    def Borrow(self):
        self._borrowedCount += 1

    def Return(self):
        self._borrowedCount -= 1

    def GetBorrwedCount(self):
        return self._borrowedCount

    def GetCountInLibrary(self):
        return self._totalCount - self._borrowedCount


class Library:
    def __init__(self):
        self._books = []

    def AddBookToLibrary(self, title):
        for book in self._books:
            if book.GetTitle() == title:
                book.AddEx()
                return
        self._books.append(Book(title))

    def BorrowBook(self, title):
        for book in self._books:
            if book.GetTitle() == title:
                book.Borrow()

    def ReturnBook(self, title):
        for book in self._books:
            if book.GetTitle() == title:
                book.Return()

ourLibrary = Library()
while True:
    print("1. Lägg till ex av bok")
    print("2. Låna ut bok")
    print("3. Returnera bok")
    s = input("Välj ->")
    if s == "1":
        print("Namn på bok som köpts in")
        namn = input("->")
        ourLibrary.AddBookToLibrary(namn)
    elif s == "2":
        print("Namn på bok att låna ut")
        namn = input("->")
        ourLibrary.BorrowBook(namn)
    elif s == "3":
        print("Namn på bok att returnera")
        namn = input("->")
        ourLibrary.ReturnBook(namn)
