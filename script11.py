class BankAccount:
    bank_name='national python bank'
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions=[]
acc1=BankAccount('alice',20000)
acc2=BankAccount('bob')
print(acc1.owner,acc1.balance)
print(acc2.owner,acc2.balance)
print(BankAccount.bank_name)