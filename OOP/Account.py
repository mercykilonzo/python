
from datetime import datetime

class Transaction:
    def __init__(self, narration, amount,transactiontype):
        self.date = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transactiontype = transactiontype
       
class Account:
    account_number_counter = 101020
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self.__account_number = Account.account_number_counter
        self.transactions = []
        self.loan = 0
        self.frozen = False
        self.minimum_balance = 0
        self.is_closed = False


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(Transaction(narration = "You have deposited",amount = amount,transactiontype = "Deposit"))
        return f"Dear customer you have deposit {amount},your new balance is {self.__balance}. "

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(Transaction(narration = "You have withdrawn",amount = -amount,transactiontype = "Withdrawal"))
        return self.__balance

    def get_balance(self):
        return sum(t.amount for t in self.transactions)

    def transfer(self, amount,account_owner):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(Transaction("Transferred to another account",-amount,"transfer"))
            return f"Transferred {amount} to {account_owner}.Your new balance {self.get_balance()}"

    def view_account_details(self):
        return f"Name: {self.name}, Account No: {self.__account_number}, Balane {self.get_balance()}"

    def get_account_number(self):
        return self.__account_number 
    
    def account_statement(self):
        print("Account statement")
        for deposit in self.deposits:
            print(f"Deposit: {deposit}")
        for withdrawal in self.withdrawals:
            print(f"Withdrwal: {withdrawal}")   

    def statement(self):
        print("Account Statement:")
        for t in self.transactions:
            print(f"{t.date} - {t.narration} - {t.amount}")
        print(f"Your balance is {self.get_balance()}")

    def calculate_loan_limit(self):
        limit = sum(t.amount for t in self.transactions)    
        return limit//3
    def request_loan(self,amount):
        limit = calculate_loan_limit()
        if amount > limit:
            return f"Your cannot get loan for {amount}. Your loan limit is {limit}" 
        else:
            return f"Your have received a {amount} loan."       
   
    def repay_loan (self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= amount
            return f"You have repaid your loan, your new loan debt is {self.loan}"        

    
    def account_owner(self,newOwner):
        self.name = newOwner

    def min_balance(self, amount):
        if amount>=0:
            self.minimum_balance = amount
            return f"Your account minumum is {self.minimum_balance}"
        
    def apply_interest(self):
        interest = self.loan * 0.05
        self.loan += interest
        return f"Your interest is {interest} and total {self.loan}"
    def freeze(self):
        self.frozen = True
        return f"Account has been frozen for security reason"
    def un_freeze(self):
        self.frozen = False
        return f"Account has been unfrozen"
    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan = 0
        self.min_balance = 0
        return f"Your account has been closed"

 










    