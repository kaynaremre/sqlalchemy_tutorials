from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine


# MetaData Object is a collection of Table objects and their associated schema constructs.
# It holds a collection of Table objects as well as an optional binding to an Engine or Connection.
meta = MetaData()

# Create an engine for database
engine = create_engine("sqlite:///college.db", echo=True)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)


meta.create_all(engine)


ins = students.insert()
ins = students.insert().values(name='Emre', lastname='Kaynar')
conn = engine.connect()
result = conn.execute(ins)

conn.execute(students.insert(), [
    {'name': 'Emre', 'lastname': 'Acir'},
    {'name': 'Eren', 'lastname': 'Mungan'},
    {'name': 'Ziya', 'lastname': 'Ercan'},
])
