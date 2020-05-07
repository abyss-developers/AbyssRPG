import sqlite3
from main import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees(first, last, pay) VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last,'pay': emp.pay,})


def get_emps_by_name(lastname):
    c.execute('SELECT * FROM employees WHERE last=:last', {'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("""DELETE from employees SET pay = :pay WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last})

# emp_1 = Employee('Nate','Ervin', 3)
# emp_2 = Employee('Skira','Locke', 333333)

#insert_emp(emp_1)
#insert_emp(emp_2)


# c.execute("""CREATE TABLE employees (id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, pay INTEGER)""")

#c.execute("INSERT INTO employees(first, last, pay) VALUES (?,?,?)", (emp_1.first, emp_1.last, emp_1.pay))


#conn.commit()

#c.execute('SELECT * FROM employees WHERE last=?', ('Zhou',))

#print(c.fetchall())


#print(c.fetchall())

#conn.commit()

conn.close