import sqlite3

## connect with sqllite

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT); 

"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Arjun', 'Engineering', 'A', 87)''')
cursor.execute('''Insert Into STUDENT values('Divya', 'Marketing', 'B', 85)''')
cursor.execute('''Insert Into STUDENT values('Rahul', 'Finance', 'C', 78)''')
cursor.execute('''Insert Into STUDENT values('Priya', 'Medicine', 'A', 92)''')
cursor.execute('''Insert Into STUDENT values('Amit', 'Computer Science', 'B', 88)''')
cursor.execute('''Insert Into STUDENT values('Neha', 'Arts', 'C', 80)''')
cursor.execute('''Insert Into STUDENT values('Vinay', 'Management', 'D', 76)''')
cursor.execute('''Insert Into STUDENT values('Pooja', 'Law', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Saurabh', 'Economics', 'B', 82)''')
cursor.execute('''Insert Into STUDENT values('Nisha', 'Psychology', 'C', 84)''')
cursor.execute('''Insert Into STUDENT values('Ravi', 'History', 'D', 81)''')
cursor.execute('''Insert Into STUDENT values('Ankita', 'Biology', 'A', 93)''')
cursor.execute('''Insert Into STUDENT values('Karan', 'Physics', 'B', 87)''')
cursor.execute('''Insert Into STUDENT values('Sneha', 'Chemistry', 'C', 79)''')
cursor.execute('''Insert Into STUDENT values('Vivek', 'Statistics', 'D', 77)''')
cursor.execute('''Insert Into STUDENT values('Meena', 'Journalism', 'A', 95)''')
cursor.execute('''Insert Into STUDENT values('Tushar', 'Sociology', 'B', 83)''')
cursor.execute('''Insert Into STUDENT values('Ritika', 'Political Science', 'C', 86)''')
cursor.execute('''Insert Into STUDENT values('Gaurav', 'Accounting', 'D', 88)''')
cursor.execute('''Insert Into STUDENT values('Isha', 'Environmental Science', 'A', 91)''')
cursor.execute('''Insert Into STUDENT values('Manoj', 'Pharmacy', 'B', 89)''')
cursor.execute('''Insert Into STUDENT values('Vandana', 'Design', 'C', 81)''')
cursor.execute('''Insert Into STUDENT values('Nikhil', 'Linguistics', 'D', 80)''')
cursor.execute('''Insert Into STUDENT values('Akash', 'Business Administration', 'A', 94)''')
cursor.execute('''Insert Into STUDENT values('Shweta', 'Philosophy', 'B', 86)''')
cursor.execute('''Insert Into STUDENT values('Mahesh', 'Geography', 'C', 82)''')
cursor.execute('''Insert Into STUDENT values('Rani', 'Mathematics', 'D', 78)''')
cursor.execute('''Insert Into STUDENT values('Siddharth', 'Anthropology', 'A', 92)''')
cursor.execute('''Insert Into STUDENT values('Preeti', 'Physics', 'B', 88)''')
cursor.execute('''Insert Into STUDENT values('Deepak', 'Zoology', 'C', 83)''')
cursor.execute('''Insert Into STUDENT values('Aarav', 'Botany', 'D', 85)''')
cursor.execute('''Insert Into STUDENT values('Geeta', 'Information Technology', 'A', 96)''')
cursor.execute('''Insert Into STUDENT values('Sameer', 'Electronics', 'B', 84)''')
cursor.execute('''Insert Into STUDENT values('Ananya', 'Architecture', 'C', 81)''')
cursor.execute('''Insert Into STUDENT values('Rakesh', 'Public Administration', 'D', 89)''')
cursor.execute('''Insert Into STUDENT values('Ruchi', 'Music', 'A', 91)''')
cursor.execute('''Insert Into STUDENT values('Sumit', 'Fine Arts', 'B', 87)''')
cursor.execute('''Insert Into STUDENT values('Harsha', 'Film Studies', 'C', 79)''')
cursor.execute('''Insert Into STUDENT values('Jyoti', 'Theatre', 'D', 82)''')


data=cursor.execute(''' Select * from STUDENT''')

for row in data:
    print(row)


connection.commit()
connection.close()
