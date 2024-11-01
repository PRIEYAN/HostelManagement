import sqlite3

# Connect to the SQLite database (or create it)
connect = sqlite3.connect('login.db')
cursor = connect.cursor()

# Drop the table if it exists
cursor.execute('DROP TABLE IF EXISTS people')

# Create the table with username, email, and password
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        username TEXT,
        email TEXT,
        password TEXT
    )
''')

# Open the data file and read its contents
with open('data.txt', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        # Strip whitespace and split the line into components
        username, email, password = line.strip().split(', ')
        # Insert the data into the people table
        cursor.execute('INSERT INTO people (username, email, password) VALUES (?, ?, ?)', (username, email, password))

connect.commit()
connect.close()


#this thing should not be in the public hosting server,, this is to convert the given txt file to database..