import psycopg2

conn = psycopg2.connect(
                        database='python_connect', user='postgres',
                        password='root', host='localhost', port='5432'
                    ) # 127.0.0.1

cur = conn.cursor()
# cur.execute('''
# CREATE TABLE student(
#     id serial primary key,
#     name varchar(100) not null,
#     age int
# );''')

# cur.execute('''
# INSERT INTO student(
# name, age)
# VALUES('Nazgul', 22), ('Baitik', 23);
# ''')

cur.execute('''
SELECT * FROM student;''')
# students = cur.fetchall()
students = cur.fetchone()
students = cur.fetchone()
print(students)
# for student in students:
#     print("id", student[0])
#     print("name", student[1])
#     print("age", student[2])
#     print()
conn.commit()
conn.close()


