import sqlite3 

# connect 
'''
It is used to build connection between database and pyhthon.
it will create one if it does not exists.
'''
conn= sqlite3.connect("student.db")

#cursor 
'''
Cursor is used to execute SQL commands
'''
cursor=conn.cursor()

cursor.execute("""
          create table if not exists students(
            id integer primary key autoincrement,
            name text,
            age integer,
            grade text
            )
            """)

# conn.commit()

# cursor.execute("""
#         insert into students (name,age,grade)
#         values(?,?,?)
#                 """,("Aadi",19,"a+"))
# conn.commit()
conn.commit()


studata=[
    ("Aditya",19,"A+"),
    ("Aayush",18,'A+'),
    ("Bob",17,"B"),
    ("Charlie",22,"B+"),
    ("Jay",21,"O"),
    ("Aman",19,"C")
]

# cursor.executemany(
#     """
#     insert into students (name,age,grade) values(?,?,?)
#     """,studata
# )
# conn.commit()


# cursor.execute("""
#         select * from students;
# """
# )

rows = cursor.fetchall() # fetching all the data
# rows = cursor.fetchone() # fetching one row of data
# rows = cursor.fetchmany(n) # fetching n number of row of data

# for i in rows:
#     print(i)


#### Update

# cursor.execute(
#     """
#     Update students 
#     set grade = ?
#     where name = ?
#     """,("B","Aayush")
# )


# cursor.execute(
#     """
#     delete from students
#     where id =?
#     """,("1")
# )

# name = input("Enter name to delete")

# cursor.execute(
#     """
#     delete from students
#     where name =?
#     """,(name,)
# )
cursor.execute("""
        select * from students 
        where name ="Aman"
"""
)
rows = cursor.fetchall() # fetching all the data
for i in rows:
    print(i)

conn.commit()
conn.close()