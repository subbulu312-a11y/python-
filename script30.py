class BankAccount:
    def __init__(self,account_number:str,initial_balance:float=0.0):
        self.account_number = account_number
        self.__balance = float(initial_balance)
    def get_balance(self)->float:
        return self.__balance
    def deposit(self,amount:float)->None:
        if amount<=0:
            print("error:deposit amount must be positive")
            return
        self.__balance += amount
        print(f"deposited ${amount:.2f}. new balance:${self.__balance:.2f}")
    def withdraw(self,amount:float)->None:
        if amount<=0:
            print("error:withdraw amount must be positive")
            return
        if amount>self.__balance:
            print(f"transaction denied:insufficient funds.current balance is ${self.__balance:.2f}")
            return
        self.__balance -= amount
        print(f"withdrew ${amount:.2f}. new balance:${self.__balance:.2f}")
my_account=BankAccount("ABC132",500.0)
print(f"Account created. initial Balance:${my_account.get_balance():.2f}")
my_account.withdraw(150.0)
my_account.deposit(-50.0)
my_account.deposit(50.0)