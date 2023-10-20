import datetime

class Book:
    def __init__(self, name, author, year, price):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
    
    def __str__(self):
        return (f'The book "{self.name}" was written by {self.author}, and it was published in { self.year }. It costs ${ self.price }.')

    def getAge(self):
        curDay = datetime.date.today()
        curYear = curDay.year
        return f'The book "{ self.name }" was published { curYear - self.year } years ago.'

book1 = Book('Holes', 'Louis Sachar', 1998, 8.99)
book2 = Book('Everything You Need To Ace Science In One Big Fat Notebook', 
    '\nWorkman Publishing', 2016, 14.49
)

print(book1)
print(book1.getAge())

print()

print(book2)
print(book2.getAge())