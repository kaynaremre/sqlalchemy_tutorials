from sqlalchemy.sql import text
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


engine = create_engine('sqlite:///college.db', echo=True)
meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

conn = engine.connect()

s = text("select students.name, students.lastname from students where students.name between :x and :y")
result = conn.execute(s, x='A', y='L').fetchall()

for row in result:
    print(row)
