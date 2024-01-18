# #inheritance
class Account:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount") 
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawl ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid withdraw amount or insufficient balance.")
class SavingsAccount(Account):        
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest_amount=self.balance*self.interest_rate
        print(f"Interest calculated:${interest_amount}")
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self,amount):
        if amount>0 and amount<=(self.balance+self.overdraft_limit):
           print(f"Withdrawl ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid balance amount or insufficient funds (including overdraft).")

savings_acc = SavingsAccount(account_number="SA123", account_holder="John Doe", balance=1000, interest_rate=0.05)
savings_acc.deposit(500)
savings_acc.calculate_interest()
savings_acc.withdraw(200)
current_acc = CurrentAccount(account_number="CA456", account_holder="Jane Doe", balance=1500, overdraft_limit=500)
current_acc.deposit(200)
current_acc.withdraw(2000)

# #library
class library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]
    def display_books(self,books):
        self.books.append(books)
        self.no_of_books=len(self.books)
        
    def info(self):
        print(f"The library has {self.no_of_books} books.The Books are:")
        for book in self.books:
            print(book)
# class library1(library):
obj=library()
obj.display_books("book1")
obj.display_books("book2")
obj.display_books("book3")
obj.display_books("book4")
obj.info()


class person:
    company_name="apple"
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print(f"{self.name} is {self.age} years old and he/she is {self.gender} and works in {self.company_name}")
emp1=person("Harry",23,"Male")
emp1.age=89
emp1.company_name="tesla"
emp1.info()

class student:
    company_name="Tesla"
    def info(self):
        print(f"The name of the person is {self.name}  and works in {self.company_name}")
    def change_c_name(cls,new_c_name):
        cls.company_name=new_c_name
a=student()
a.name="PAPA"
a.company_name="PARIS"
a.change_c_name("porshe")
a.info()












