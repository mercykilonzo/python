
class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.minimum_balance = 0
        self.is_closed = False
        

    def deposit(self,amount):
        if amount > 0:
            self.deposits.append(amount)
        totaldeposit = 0 
        for i in self.deposits:
            totaldeposit+=i
        self.balance+=totaldeposit    
                     
        return f"Dear {self.name} your balance is {totaldeposit}"

    def withdraw(self,amounts):
        if amounts > 0 and (self.balance - amounts) >= self.minimum_balance:
            self.withdrawals.append(amounts)
            self.balance = self.balance - amounts       
            return f"Dear {self.name} your balance is {self.balance}"
        
              
    def get_balance(self):
        totalwithdrawal = 0
        for i in self.withdrawals:
            totalwithdrawal+=i

        totaldeposit = 0 
        for i in self.deposits:
            totaldeposit+=i

        self.balance = totaldeposit - totalwithdrawal  
        return f"Dear {self.name}, your balance is {self.balance}"

    def transfer_funds(self,amount,target_account):
        if amount > 0 and self.balance >= amount:
            self.withdrawals(amount)
            target_account.deposit(amount)
            new_balance = self.get_balance()

             
        return f"Dear {self.name}, you transferd {amount}. Your new balance is {new_balance}"

    def request_loan (self,amount):
        if amount > 0 :
            self.loan +=amount
            return f"Your loan amount is {self.loan}"
    def repay_loan (self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= amount
            return f"You have repaid your loan, your new loan debt is {self.loan}"        

    def account_details(self):
        return f"{self.name}, your balance is {self.balance}"

    def account_owner(self,newOwner):
        self.name = newOwner

    def account_statement(self):
        print("Account statement")
        for deposit in self.deposits:
            print(f"Deposit: {deposit}")
        for withdrawal in self.withdrawals:
            print(f"Withdrwal: {withdrawal}")   

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

    def calculate_loan_limit(self):
        total.deposits = sum(self.deposits)  
        return total.deposits // 3  
    def request_loan(self,amount):
        limit = calculate_loan_limit()
        if amount > limit:
            return f"Your cannot get loan for {amount}. Your loan limit is {limit}"












   
                    

