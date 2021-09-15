class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f' account owner : {self.name } \n Account Balance: Rp. {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print(f'deposit accepted {amount}')

    def withdrawal(self, wd_amount):
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            print('withdrawal processed')
        else:
            print('insufficient fund')


account_fredy = Account('fredy', 100)

account_joe = Account('Joe')

print(account_joe)


account_fredy.deposit(20)

print(account_fredy)

account_fredy.withdrawal(150)

print(account_fredy)