import sqlite3
from employee import Employee
import pandas as pd
conn = sqlite3.connect("employee.db")
cur = conn.cursor()


# Method for creating employee's table
def create_table():
    with conn:
        cur.execute("""
            CREATE TABLE employee (
                ID INTEGER KEY Not Null,
                First_name VARCHAR(40),
                Middle_name VARCHAR(40),
                Surname VARCHAR(40),
                Email VARCHAR(30),
                Balance INTEGER(14)
            )
        """)


#  Using pandas to view the database
def pandas_view():
    df = pd.read_sql_query("""
        SELECT *
        FROM employee
    """, conn, index_col='ID')
    print(df)


#  Using sqlite to view the database
def sql_view():
    cur.execute("""
            SELECT * 
            FROM employee
    """)
    for i in iter(cur.fetchall()):
        print(i)


#  Creating employees
emp1 = Employee(7, "Alani", "Tijani", "Olaseun", 1829)
emp2 = Employee(8, "Gbedebo", "ogundepo", "kolawole", 39202)
emp3 = Employee(9, "Kudabo", "seatin", "mustapha", 441302)

# Employee.insert(conn, cur, emp1, emp2, emp3)
# Employee.update(conn, cur, "Ademuyiwa", "Muyideen")
# Employee.delete(conn, cur, "Muyideen")
# conn.commit()

pandas_view()
conn.close()
