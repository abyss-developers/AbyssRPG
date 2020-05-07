import sqlite3
from main import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees(first, last, pay) VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay,})


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

def ifexisting(emp):
    c.execute("""SELECT last FROM employees""")
    print(emp.last)
    print(c.fetchall)
    for i in c.fetchall():
        if i == emp.last:
            print("yes")
        else:
            print("fail")


# c.execute("""CREATE TABLE employees (id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, pay INTEGER)""")

conn.commit()

x = input("user")
y = input("pass")
z = input("pay")

emp = Employee(x, y, z)
#c.execute("INSERT INTO employees(first, last, pay) VALUES (:first, :last, :pay)", {'first': "jason", 'last': "zhou", 'pay': "10000000"})

conn.commit()
ifexisting(emp)


conn.close