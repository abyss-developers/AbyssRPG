import sqlite3

conn = sqlite3.connect("employee.db")

c = conn.cursor()

# c.execute("""CREATE TABLE employees (id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, pay INTEGER)""")

# c.execute("INSERT INTO employees(first, last, pay) VALUES ('Jason','Zhou','100000')")

conn.commit()

conn.close