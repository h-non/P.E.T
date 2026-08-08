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

def inputexp():
     
     amnt = input("Enter the expended amount: ")
     try:
          amnt = float(amnt)
     except ValueError:
          print("Amount must be a number.")
          return

     catg = input("Enter the category of this expense: ")
     desc = input("Enter the description of this expense: ")

     dat = input("Enter the date of the expense (YYYY-MM-DD) or leave blank for todays' date: ")

     if dat.strip() == "":
          expdat = datetime.today().date()
     else:
          try:
               expdat = datetime.strptime(dat,"%Y-%m-%d").date()
          except ValueError:
               print("Date must be inputed as Year-month-day format.")

               return

     expense = add_expense(amnt,catg,desc,expdat)
     print(f"Added expense: {expense.amount}$ in {expense.category} on {expense.date}")






