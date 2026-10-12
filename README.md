# Library Management System

A simple **Library Management System** developed in Python. This menu-driven command-line application helps manage a small collection of books by allowing users to view, add, search, issue, and return books.

## Features

- **Show Books:** Display all books and their availability status.
- **Add Book:** Add a new book to the collection and prevent duplicate titles.
- **Search Book:** Find a book by its exact title and view its status.
- **Issue Book:** Mark an available book as issued.
- **Return Book:** Mark an issued book as available again.
- **Exit:** Close the application.

## Technologies Used

- Python 3
- Python dictionaries, functions, loops, conditionals, and user input

## Project Structure

```text
Library-Management-System/
├── LibraryManagementSystem.py
├── README.md
└── requirements.txt
```

## Getting Started

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone the repository or download the files.
3. Open a terminal in the project directory.
4. Run:

```bash
python LibraryManagementSystem.py
```

On some systems, use `python3 LibraryManagementSystem.py` instead.

## How to Use

The program displays this menu:

```text
===== Library Management System =====
1. Show Books
2. Add Book
3. Search Book
4. Issue Book
5. Return Book
6. Exit
```

For example, select `4` to issue a book:

```text
Enter book name to issue: Python Basics
Book issued successfully.
```

When you show the books again, the status of `Python Basics` will be `Issued`. Select `5` and enter the same title to return it.

## Requirements

- Python 3
- No third-party Python packages required

The `requirements.txt` file is intentionally empty of package dependencies.

## Current Limitations

- Book records and statuses are stored in memory and reset when the application restarts.
- Book searches require exact, case-sensitive titles.
- The system tracks only one status per book title, not multiple copies or borrowers.

## Future Improvements

- Store book information in a file or database.
- Add borrower details and issue/return dates.
- Support multiple copies of the same title.
- Add case-insensitive search and input validation.
- Build a graphical or web-based interface.

## Learning Outcomes

This project demonstrates Python fundamentals including dictionaries, functions, conditional statements, loops, and simple status management.
