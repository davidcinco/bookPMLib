import sqlite3

from numpy import number

class Load:
    def __init__(self):
        pass

    def load(self, data):
        # Placeholder for loading logic
        self.generate_database()
        self.insert_book(data)
        
    def insert_book(self, books):
        try:
            # Create a connection to the SQLite database
            conn = sqlite3.connect('./data/booksdb.db')
            
            # drop duplications and insert dataframe
            books = books.drop_duplicates(subset=['Title', 'Author'])
            books.to_sql('books', conn, if_exists='append', index=False)
            
            conn.close()
            
        except Exception as e:
            print(f"An error occurred while inserting book data: {e}")
      
    def delete_book(self, book_id):
        try:
            # Create a connection to the SQLite database
            conn = sqlite3.connect('./data/booksdb.db')
            cursor = conn.cursor()
            
            # Delete a book record from the books table based on the provided book_id
            cursor.execute('''DELETE FROM books WHERE id = ?''', (book_id,))
            
            # Commit changes and close the connection
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"An error occurred while deleting book data: {e}")
        
    def delete_all_books(self):
        try:
            # Create a connection to the SQLite database
            conn = sqlite3.connect('./data/booksdb.db')
            cursor = conn.cursor()
            
            # Delete all book records from the books table
            cursor.execute('''DELETE FROM books''')
            
            # Commit changes and close the connection
            conn.commit()
            conn.close()
            
        except Exception as e:
            print(f"An error occurred while deleting all book data: {e}")
        
    def generate_database(self):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('./data/booksdb.db')
        cursor = conn.cursor()
        
        # Create a table for books
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                height INTEGER NOT NULL,
                publisher TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()