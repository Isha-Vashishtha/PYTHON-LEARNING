# Create a Python class named Bank with the following features:The class should maintain a list of accounts. 
# Each account should be an instance of the BankAccount class with attributes such as account_number, account_holder, balance, etc
# Implement methods for adding a new account, searching for an account by account number, and transferring funds between two accounts.
# BankAccount Class:
# Attributes: account_number, account_holder, balance
# Methods: init(self, account_number, account_holder, initial_balance=0): Initializes the account with an account number, account holder name, and an optional initial balance (default is 0).
# deposit(self, amount): Deposits the specified amount into the account.
# withdraw(self, amount): Withdraws the specified amount from the account, if sufficient funds are available.
# get_balance(self): Returns the current balance of the account.
# Bank Class:
# Attributes: accounts (a list to store instances of BankAccount)
# Methods: init(self): Initializes an empty list of accounts.
# add_account(self, account): Adds a BankAccount instance to the list of accounts.
# find_account(self, account_number): Finds and returns a BankAccount instance based on the provided account number.
# transfer_funds(self, from_account_number, to_account_number, amount): Transfers funds from one account to another, updating their balances accordingly.
class BankAccount:
    def __init__(self,account_number,account_holder,initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    def deposit(self,amount):
        print("Initial Account Balances:")
        print(f"Account {self.account_number} - Balance:{self.initial_balance}")
        if amount>0:
            self.initial_balance+=amount
            print("Funds transferred successfully.")
            print("Updated Account Balances:")
            print(f"Account {self.account_number}-Balance: {self.initial_balance}")
    def withdraw(self,amount):
        if amount>0 and amount<=self.initial_balance:
            self.initial_balance-=amount
            print(f"Account {self.account_number}-Balance:{self.initial_balance}")
        else:
            print("Failed:Funds are not available.")
    def get_balance(self):
        return self.initial_balance
class Bank:
    def __init__(self):
        self.account_list=[]
    def add_account(self, account): #Adds a BankAccount instance to the list of accounts
         self.account_list.append(account)
    def find_account(self, account_number):
        for account in self.account_list:
          if account.account_number== account_number:
            return account
        return None
    def transfer_funds(self, from_account_number, to_account_number,amount):
        from_account=self.find_account(from_account_number)
        to_account=self.find_account(to_account_number)
        if from_account and to_account:
            if from_account.get_balance()>=amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print("Funds transferred successfully.")
            else:
                print("Insufficient funds in the source account.")
        else:
            print("One or both accounts not found.")
#Example usage with user input:
bank = Bank()

# Creating accounts with initial balance
num_accounts = int(input("Enter the number of accounts to create: "))
for i in range(num_accounts):
    account_number = input(f"Enter account number for Account {i + 1}: ")
    account_holder = input(f"Enter account holder name for Account {i + 1}: ")
    initial_balance = float(input(f"Enter initial balance for Account {i + 1}: "))
    new_account = BankAccount(account_number, account_holder, initial_balance)
    bank.add_account(new_account)

# Displaying initial account balances
print("\nInitial Account Balances:")
for account in bank.account_list:
    print(f"Account {account.account_number} - Balance: ${account.get_balance()}")

# Transferring funds
from_account_num = input("\nEnter source account number for fund transfer: ")
to_account_num = input("Enter destination account number for fund transfer: ")
transfer_amount = float(input("Enter the amount to transfer: "))

bank.transfer_funds(from_account_num, to_account_num, transfer_amount)

# Displaying updated account balances
print("\nUpdated Account Balances:")
for account in bank.account_list:
    print(f"Account {account.account_number} - Balance: ${account.get_balance()}")







