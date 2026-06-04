class BankAccount:
    def __init__(self,ower,balance):
        self.ower=ower
        self._log=[]
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        self._log.append(f'+ {amount}')
    def get_balance(self):
        return self.__balance
acc=BankAccount('alice',5000)
acc.deposit(1000)
print(acc.ower)
print(acc._log)
print(acc.get_balance())
print(acc._BankAccount__balance)
