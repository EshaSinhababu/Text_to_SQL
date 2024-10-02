import sqlite3

## connect with sqllite

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT); 

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Esha', 'Data Science', 'A',90)''')
cursor.execute('''Insert Into STUDENT values('Shivam', 'Buisness Analyst', 'B',100NF)''')
cursor.execute('''Insert Into STUDENT values('Kiran', 'Banking', 'C',95)''')
cursor.execute('''Insert Into STUDENT values('Trisha', 'Nurce', 'D',93)''')

data=cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()