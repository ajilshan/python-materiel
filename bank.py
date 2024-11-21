class Bank():
    def __init__(self,acc,cname,balance):
        self.acc=acc
        self.cname=cname
        self.balance=balance
        self.doc="11/12/2024"
    
    def to_deposit(self):
        deposit=int(input("Enter deposit amount:"))
        afterdeposit=self.balance+deposit
        print(f"Balance: {afterdeposit}")

    def to_withdraw(self):
        withdraw=int(input("Enter withdawel amount"))
        if withdraw<self.balance:
            afterwithdraw=self.balance-withdraw
            print(f"Balance: {afterwithdraw}")
        else:
            print("Insufficiant balance")
            
    def show_balance(self):
        print(f"Balance: {self.balance}")
    def customer_details(self):
        print(f"Customer Name - {self.cname}")
        print(f"Account No. - {self.acc}")
        print(f"Balance - {self.balance}")
     
obj1=Bank("123","AJ",1000)
#obj1.to_deposit()
#obj1.to_withdraw()
#obj1.show_balance()
obj1.customer_details()

        
