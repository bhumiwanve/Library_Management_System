books = {
    "Python Basics": "Available",
    "Data Structures": "Available",
    "Computer Networks": "Available",
    "Database Management": "Available",
    "Operating Systems": "Available"
}


def show_books():
    print("\n===== Library Books =====")

    for book, status in books.items():
        print(book, "-", status)


def add_book():
    book = input("Enter book name: ")

    if book in books:
        print("Book already exists.")
    else:
        books[book] = "Available"
        print("Book added successfully.")


def search_book():
    book = input("Enter book name to search: ")

    if book in books:
        print("Book found.")
        print("Status:", books[book])
    else:
        print("Book not found.")


def issue_book():
    book = input("Enter book name to issue: ")

    if book not in books:
        print("Book not found.")
    elif books[book] == "Issued":
        print("Book is already issued.")
    else:
        books[book] = "Issued"
        print("Book issued successfully.")


def return_book():
    book = input("Enter book name to return: ")

    if book not in books:
        print("Book not found.")
    elif books[book] == "Available":
        print("Book is already available.")
    else:
        books[book] = "Available"
        print("Book returned successfully.")


while True:

    print("\n===== Library Management System =====")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")