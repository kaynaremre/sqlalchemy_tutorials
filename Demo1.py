from curses import echo
from sqlalchemy import create_engine

engine = create_engine("sqlite:///college.db", echo=True)