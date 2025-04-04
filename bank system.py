class Bank:
    def __init__(self,aco_no,name,balance):
        self .ac_no = aco_no
        self.name=name
        self.balance=balance
        
    def debit(self, amt):
        if amt<self.balance:
            self.balance -=amt
            print(f"{amt} has been debited. New balance is: {self.balance}")
        else:
            print("Insufficient balance for this debit operation.")
    
    def credit (self,amt):
        self.balance+=amt
        
        print(f"{amt}has been credited. New balance is: {self.balance}")
        
    def show_balance(self):
        print(f"Customer: {self.name},Account number:{self.ac_no},Balance :{self.balancce}")
 
account=Bank("12567", "Vaishnavi", 30000)


while True:
    print("\nChoose an option:")
    print("1. Credit")
    print("2. Debit")
    print("3. Show Balance")
    print("4. Exit")
    
    choice = int(input("Enter your choice(1/2/3/4)"))
    
    if choice ==1 :
        amt= float(input("Enter amount to credit:"))
        account.credit(amt)
    elif choice==2:
        amt = float(input("Enter amount to debit:"))
        account.debit(amt)
    elif choice ==3:
        account.show_balance()
    elif choice==4:
        print("thank you for using banking system. ")
        break
        
    else:
        print("Invalid choice.Please try again.")
    
   
        
        
        
