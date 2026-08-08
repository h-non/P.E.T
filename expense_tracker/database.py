from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


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


def add_expense(amount, category, description, exp_date):
     session = SessionLocal()
     new_expense = Expenses(

          amount = amount,
          category = category,
          description = description,
          date = exp_date

     )


     session.add(new_expense)
     session.commit()
     session.refresh(new_expense)
     session.close()
     return new_expense


def get_expenses():
     session = SessionLocal()
     expenses = session.query(Expenses).all()
     session.close()
     return expenses

