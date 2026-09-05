class BankAccount:
    bank_name="LIS BANK"
    total_accounts=0
    def __init__(self,owner, balance=0, count=0):
        self.owner=owner
        self.balance=balance
        self.count=count
        BankAccount.total_accounts+=1
        pass
    def deposite(self,amount):
        if amount <=0:
            print("Amount must in positive")
        else:
            self.balance+=amount
        print(f"Current banlance = {self.balance} ")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance!! ")
        else:
            self.balance-=amount
        print(f"Current banlance = {self.balance} ")
    @classmethod
    def increment_count(cls):
        cls.total_accounts=cls.total_accounts+1
        print(f"totol account= {cls.total_accounts}")
    
    def balance_check(self):
        if self.balance<0:
            print("Insufficient Balance!! ")
        else:
            print(f"Current banlance = {self.balance} ")
    

acc=BankAccount("arpit",1000)
acc.deposite(500)
acc.withdraw(1200)
acc.increment_count()
acc2=BankAccount("arna",5)
acc2.withdraw(200)
acc2.increment_count()
print(acc.bank_name)


print(f"{acc.owner}'s transaction count: {acc.count}")
print(f"{acc2.owner}'s transaction count: {acc2.count}")


acc.balance_check()
