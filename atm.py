class atm:

    def __init__(self, user):
        self.transaction = ''
        self.user = user
        self.balance = 0

    def deposit(self, amount):

        self.balance = self.balance + amount
        newtransaction = f'{self.user} deposited ${amount}: Total ${self.balance}'
        self.transaction = self.transaction + newtransaction + '\n'
        return newtransaction
    
    def check_withdraw(self, amount):

        if self.balance - amount < 0:
            print("invalid amount, you're poor")
        
        else:
            return True

    def withdraw(self, amount):

        if self.check_withdraw(amount) ==  True:
            self.balance = self.balance - amount
            newtransaction = f'{self.user} withdrew ${amount}: Total ${self.balance}'
            self.transaction = self.transaction + newtransaction + '\n'
            newtransaction
    
    def print_transactions(self):
    
        print(self.transaction)


user1 = atm('jayson')

checklist = ['check balance','deposit','withdraw','transactions','stop']
print('Welcome to Louizos Finacial!')
# response = input('Are you a new user')
# if response == 'No':
#     username = input('What is your name')
#     newuser = atm(response)
# if response == 'Yes':
#     pass
    
# else:
    # pass
while True:
    
    check = input('check balance/deposit/withdraw/transactions/stop?').lower()
    
    if check not in checklist:
        print('invalid response')
    
    if check == 'check balance':
        print(f'${user1.balance}')
    
    elif check == 'deposit':
        amount = input('How much will you deposit today?')
        amount = int(amount)
        user1.deposit(amount)
    
    elif check == 'withdraw':
        amount = input('How much would you like to withdraw?')
        amount = int(amount)
        user1.withdraw(amount)
    
    elif check == 'transactions':
        user1.print_transactions()
    
    elif check == 'stop':
        user1.print_transactions()
        print('Have a nice day!')
        break

    check = input('would you like to make another transaction y/n:')
    
    if check == 'no' or check == 'stop' or check == 'n':
        user1.print_transactions()
        print('Have a nice day!')
        break

    