from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine


# MetaData Object is a collection of Table objects and their associated schema constructs. 
# It holds a collection of Table objects as well as an optional binding to an Engine or Connection.
meta = MetaData()

engine = create_engine("sqlite:///college.db", echo=True)

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)

meta.create_all(engine)
