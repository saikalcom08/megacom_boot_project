from peewee import *

db = PostgresqlDatabase(
                        'python_connect', user='postgres',
                        password='root', host='localhost', port='5432'
                    )
class StudentInfo(Model):
    grade = CharField(max_length=50, null=False)
    kpi = IntegerField()

    class Meta:
        database = db
        db_table = 'infostudent'

db.connect()
db.create_tables([StudentInfo])

StudentInfo.create(grade='10b', kpi=80) # 1

# a = StudentInfo(grade="11a", kpi=100) # 2
# a.save()

# q = StudentInfo.insert(grade="7a", kpi=70) # 3
# q.execute()

