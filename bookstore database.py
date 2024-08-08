import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()

# Create the book table
c.execute('''
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    qty INTEGER
)
''')

# Populate the table with initial data
books = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]

c.executemany('INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', books)

# Commit the changes and close the connection
conn.commit()
conn.close()



