from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker



engine = create_engine("sqlite:///dataBase/expenses.db")
Base = declarative_base()


class Expenses(Base):

     __tablename__ = "expenses"

     id = Column(Integer, primary_key = True)

     amount = Column(Float)
     category = Column(String)
     description = Column(String)
     date = Column(Date)



Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
