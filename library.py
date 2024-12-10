class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print(f"Error: Book '{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print(f"Error: Book '{self.__title}' is not borrowed")
        
    def view_book_info(self):
        if self.__availability:
            status = "Available"
        else:
            status = "Not Available"
        print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {status}")

    def get_book_id(self):
        return self.__book_id
    
Book("101", "Python Programming", "John Doe")
Book("102", "Data Science Essentials", "Jane Smith")
Book("103", "Machine Learning", "Alan Turing")
Book("104", "Artificial Intelligence", "Marvin Minsky")
Book("105", "Deep Learning", "Yann LeCun")
Book("106", "Natural Language Processing", "Christopher Manning")
Book("107", "Statistics for Data Science,", "David C. Hsu")
Book("108", "Python for Data Analysis", "Wes McKinney")

    
def menu():
    while True:
        print("\n--- Welcome to the Library ---")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\n--- Library Books ---")
                for book in Library.book_list:
                    book.view_book_info()
            elif choice == 2:
                book_id = input("\nEnter book ID to borrow: ")
                for book in Library.book_list:
                    if book.get_book_id() == book_id:
                        book.borrow_book()
                        break
                else:
                    print("Error: Invalid Book ID.")
            elif choice == 3:
                book_id = input("\nEnter book ID to return: ")
                for book in Library.book_list:
                    if book.get_book_id() == book_id:
                        book.return_book()
                        break
                else:
                    print("Error: Invalid Book ID.")
            elif choice == 4:
                print("\nExiting the library system. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

menu()
