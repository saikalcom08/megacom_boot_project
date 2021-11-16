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

class Subject(Model):
    name = CharField(max_length=100)
    student_id = ForeignKeyField(StudentInfo, on_delete='CASCADE')

    class Meta:
        database = db
        db_table = 'subject'

db.connect()
db.create_tables([StudentInfo, Subject])

# StudentInfo.create(grade='12b', kpi=90) # 1

# Subject.create(name='Algebra', student_id=1)
# Subject.create(name='Biology', student_id=2)

# a = Subject(name='Biology', student_id=1)
# a.save
# a = Subject(name='Biology', student_id=2)
# a.save()

# q = StudentInfo.delete().where(StudentInfo.id == 2)
# q.execute()

# q = Subject.update({Subject.name: "Geometry"}).where(Subject.id==4)
# q.execute()

# row = Subject.get()
# print(row.name, row.student_id, row.id)

# row = StudentInfo.select.all()
# print(row.grade, row.kpi)

qs = StudentInfo.select(StudentInfo.grade, StudentInfo.kpi, Subject.name).join(Subject)
print(qs)
for q in qs:
    print("grade: {} kpi: {} name: {}".format(q.grade, q.kpi, q.subject.name))