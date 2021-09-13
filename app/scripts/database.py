import sqlite3

conn = sqlite3.connect("/Users/iv-ivan/Desktop/other/bookcrossing2/app/mydatabase.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS books
                  (title text)
               """)

books = [('Tolstoy',)]

cursor.executemany("INSERT INTO books VALUES (?)", books)
conn.commit()