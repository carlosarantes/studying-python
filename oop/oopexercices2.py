# For this challenge, create a bank account class that has two attributes:

#    owner
#    balance

# and two methods

#    deposit
#    withdraw

# As an added requirement, withdrawals may not exceed the available balance.
# instatuate your class, make several deposits and withdrawals, and test to make super
# the account can't be overdrawn.



class Account():

    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        if value <= 0:
            print('Please, provide at least 1 euro to be deposited.')
        else:
            self.balance += value 
    
    def withdraw(self, value):
        if value < 0:
            print('Please, provide a valid amount to be withdrawed (at least 1 euro)')
        elif value > self.balance:
            print(f'You only have ${self.balance} available in your account.')
        else:
            self.balance = self.balance - value

    def __str__(self) -> str:
        return f'Hello Mr.(ss) {self.owner}, you have $ {self.balance} euros.'




account = Account('Jose')

account.deposit(10)
account.deposit(75)

account.withdraw(85)

print(account)
