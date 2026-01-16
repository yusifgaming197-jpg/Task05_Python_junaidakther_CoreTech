class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
        
class Library:
    def __init__(self):
        self.books = []
        
    
    def add_book(self,book):
        self.books.append(book)
        print(f'book "{book.title}"added')
    
    def view_books(self):
        for book in self.books:
            print(f'{book.title} by {book.author}')    
            
def save_books(library):
    with open('books.txt','w') as f:
        for book in library.books:
            f.write(f'{book.title},{book.author}\n')

def load_books(llibrary):
    try :
        with open('books.txt','r') as f:
             for line in f:
                 title,author = line.strip().split(',')
                 library.add_books(Books(title,author))
     
    except FileNotFoundError:
        print('file not found')

library = Library()
load_books(library)

while True:
    print('1. Add Book')
    print('2. View Books')
    print('3. Exit')
    choice = input('Enter choice: ')

    if choice == '1':
        title = input('Enter title: ')
        author = input('Enter author: ')
        library.add_book(Books(title, author))
        save_books(library)

    elif choice == '2':
        library.view_books()

    elif choice == '3':
        break                 