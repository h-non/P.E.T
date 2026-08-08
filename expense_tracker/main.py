from database import add_expense
from datetime import datetime



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


