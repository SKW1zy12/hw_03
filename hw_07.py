import sqlite3

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

def create_books_table():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER
    )
    """)
    connect.commit()
    connect.close()

def add_book(book):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Books (title, author, year) VALUES (?, ?, ?)", (book.title, book.author, book.year))
    connect.commit()
    connect.close()

def view_books():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    connect.close()
    for book in books:
        book_obj = Book(book[1], book[2], book[3])
        book_obj.display_info()

def update_book(title, new_author, new_year):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE Books SET author=?, year=? WHERE title=?", (new_author, new_year, title))
    connect.commit()
    connect.close()

def delete_book(title):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Books WHERE title=?", (title,))
    connect.commit()
    connect.close()

def main():
    create_books_table()

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть информацию о книгах")
        print("2. Добавить новую книгу")
        print("3. Обновить информацию о книге")
        print("4. Удалить книгу")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            view_books()
        elif choice == "2":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            book = Book(title, author, year)
            add_book(book)
            print("Книга добавлена.")
        elif choice == "3":
            title = input("Введите название книги, которую хотите обновить: ")
            new_author = input("Введите нового автора: ")
            new_year = input("Введите новый год издания: ")
            update_book(title, new_author, new_year)
            print("Информация о книге обновлена.")
        elif choice == "4":
            title = input("Введите название книги, которую хотите удалить: ")
            delete_book(title)
            print("Книга удалена.")
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
