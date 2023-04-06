import mysql.connector

# Define database connection details
config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'example_db'
}

# Connect to the database
conn = mysql.connector.connect(**config)

# Create a cursor object to execute SQL queries
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS students
             (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age INT, email VARCHAR(255))''')

# Insert data into the table
c.execute("INSERT INTO students (name, age, email) VALUES (%s, %s, %s)", ("John", 25, "john@example.com"))
c.execute("INSERT INTO students (name, age, email) VALUES (%s, %s, %s)", ("Jane", 30, "jane@example.com"))
c.execute("INSERT INTO students (name, age, email) VALUES (%s, %s, %s)", ("Minhaj", 27, "shaikhminhaj.dev@gmail.com"))

# Commit changes to the database
conn.commit()

# Query the table and fetch results
c.execute("SELECT * FROM students")
rows = c.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the database connection
conn.close()
