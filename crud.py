from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Stock
from sqlalchemy.orm import sessionmaker
import psycopg2
import json

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


s = Session()

connection = psycopg2.connect(DATABASE_URI)
cursor = connection.cursor()

with open("test.json", "r") as infile:
    data = json.load(infile)

query_sql = """insert into stocks select * from json_populate_recordset (NULL::stocks, %s):"""
cursor.execute(query_sql, (json.dumps(data),))

connection.commit()
connection.close()
s.close()
