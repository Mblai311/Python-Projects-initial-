class Bank:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount


user = input('Please enter you name:')
bank = Bank(user)
while True:
    print(f'Hello {bank.name}!! Welcome to the bank!')
    entry = input('''Please select an option
    1. Balance
    2. Deposit''')
    if entry == '1':
        print(bank.balance)
    elif entry == '2':
        deposit = float(input('Enter an amount to deposit..'))
        bank.deposit(deposit)
