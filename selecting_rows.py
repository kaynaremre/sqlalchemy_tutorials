from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

#Select All students
s = students.select()

#Connect to engine
conn = engine.connect()

#Excute Query
result = conn.execute(s)

#Print Result
for row in result:
   print (row)

s = students.select().where(students.c.id>2)
result = conn.execute(s)

for row in result:
   print (row)