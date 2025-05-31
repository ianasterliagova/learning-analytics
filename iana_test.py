class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner: {self.owner}\nBalance:   ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Funds have been deposited')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('The withdrawal has been completed')
        else:
            print('Insufficient funds')
