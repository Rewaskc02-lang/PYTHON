class Account:
    def __init__(self,bal,acno):
        self.balance=bal
        self.accno=acno
    def debit(self,deb):
        self.balance=self.balance-deb
    def credit(self,cred):
        self.balance=self.balance+cred
    def totalbal(self):
        print("$",self.balance ,"in account number : ",self.accno)




a=Account(100000,234567)
print(a.accno)
print(a.balance)
a.debit(1000)
a.credit(2000)
a.totalbal()