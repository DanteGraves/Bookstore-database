# Import section.
import sqlite3

# Create function to enter new book detais into database.
def enter_book():

    '''Request details from user and stores data to database'''

    try:

        id = int(input("Enter book ID [eg. 3001]: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        qty = int(input("Enter quantity: [eg. 40]"))
    
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
            conn.commit()

        # Confirmation message.    
        print("Book added successfully!")

    except ValueError:
        print("Invalid input. Please try again.")


# Create function to update book details
def update_book():

    '''Request book ID from user to call book details from database,
    Request new data from user, 
    update previously stored data to new input data.'''

    try:

        id = int(input("Enter the ID of the book to update: "))
    
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM book WHERE id = ?', (id,))
            book = c.fetchone()
        
            if book:

                print(f"Current title: {book[1]}")
                new_title = input("Enter new title (leave blank to keep current): ")

                print(f"Current author: {book[2]}")
                new_author = input("Enter new author (leave blank to keep current): ")

                print(f"Current quantity: {book[3]}")
                new_qty = input("Enter new quantity (leave blank to keep current): ")

                new_title = new_title if new_title else book[1]
                new_author = new_author if new_author else book[2]
                new_qty = int(new_qty) if new_qty else book[3]
            
                c.execute('UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?', (new_title, new_author, new_qty, id))
                conn.commit()
                print("Book updated successfully!")

            # Error message if no book is found in database.    
            else:
                print("Book not found!")

    except ValueError:
        print("Invalid input. Please try again.")


# Create function to delete book details from database.
def delete_book():

    '''Request book ID from user, Search database for book  
    and delete all corrosponding data from database.'''

    try:

        id = int(input("Enter the ID of the book to delete [eg. 3001]: "))
    
        with sqlite3.connect('ebookstore.db') as conn:
            c = conn.cursor()
            c.execute('DELETE FROM book WHERE id = ?', (id,))
            conn.commit()

        # Confirmation message.
        print("Book deleted successfully!")

    except ValueError:
        print("Invalid input. Please try again.")


# Create function to search for books in database.
def search_books():

    '''Request title or author from user,
    search database and display all matching book details.'''

    search_term = input("Enter the title or author to search for: ")
    
    with sqlite3.connect('ebookstore.db') as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM book WHERE title LIKE ? OR author LIKE ?', ('%' + search_term + '%', '%' + search_term + '%'))
        books = c.fetchall()
        
        if books:
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")

        # Error message if no books are found.        
        else:
            print("No books found!")


# Create main menu function.
def main():

    while True:

        print("\nBookstore Management System")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        
        choice = input("Please enter your choice to continue: ")
        
        if choice == '1':
            enter_book()

        elif choice == '2':
            update_book()

        elif choice == '3':
            delete_book()

        elif choice == '4':
            search_books()

        elif choice == '0':

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Call menu function.
if __name__ == "__main__":
    main()

# End code   