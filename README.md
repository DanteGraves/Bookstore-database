Bookstore Management System

Project Overview
This is a simple command-line application designed to manage a bookstore's inventory. It utilizes an SQLite database to store and manage book records, including book IDs, titles, authors, and quantities.

Features
Add New Books: Enter details for new books and add them to the database.
Update Book Details: Modify existing book information such as title, author, and quantity.
Delete Books: Remove books from the database based on their ID.
Search for Books: Search the database for specific books by various criteria.
Requirements
Python 3.x
SQLite3
Installation
Clone the repository:


Copy code
git clone https://github.com/yourusername/bookstore-management-system.git
cd bookstore-management-system
Set up the virtual environment (optional but recommended):

Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required dependencies:
There are no external dependencies, so you can skip this step unless additional features require them.

Run the database setup script:


Copy code
python bookstore\ database.py
Usage
Run the application:

Copy code
python bookstore\ program.py

Available Commands:

Add a Book: Follow the prompts to enter the ID, title, author, and quantity of the book.
Update a Book: Enter the ID of the book you want to update and follow the prompts to change its details.
Delete a Book: Provide the ID of the book you wish to delete.
Search for Books: Input search criteria to find specific books in the database.
Database Structure
Database Name: ebookstore.db
Table Name: book
Fields:
id: Unique integer identifier for each book.
title: Text field for the book's title.
author: Text field for the author's name.
qty: Integer field representing the quantity of the book available.