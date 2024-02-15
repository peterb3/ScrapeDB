from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Stock
# from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URI)

# Session = sessionmaker(bind=engine)


# def recreate_database():
#     Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
