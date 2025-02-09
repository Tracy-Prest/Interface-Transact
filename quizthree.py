# basic banking system
class BankAccount():
    def __init__(self, acc_number, accholder_name, balance = 0.0):
        self.acc_number =acc_number
        self.accholder_name = accholder_name
        self.balance = balance
    # methods
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited. Your balance is {self.balance}")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount > self.balance:
                print("Insufficient funds")
        elif amount <= 0:
                print("Please enter a valid amount")
        else:
                self.balance -= amount
                print(f"{amount} withdrawn. Your current balance is {self.balance}")

    
    def check_balance(self):
        print(f"Your balance is {self.balance}")

# account creation
    def create_account():
        acc_name = input("Enter account name: \n").lower()
        acc_number = int(input("Enter account number: \n"))
        return BankAccount(acc_name, acc_number)

    
    def close():
        print("Account closed")
        exit()

while True:
    user = input("Do you want to create an account? (yes or no)\n").lower()
    if user == "yes":
       myacc = BankAccount.create_account()

    elif user == "no":
         input("Enter your account details: \n")  # should be able to search if acoount exist

       
    else:
        print("Please enter a valid option")
        continue

    
    print("""
        1. Deposit Money.
        2. Withdraw Money.
        3. Check Balance.
        4. Exit.
           """)
        
    entry = input("Choose the actions you want to perform:")

    if entry == "1":
          amount = float(input("Enter the amount you want to deposit: "))
          myacc.deposit(amount)
    elif entry == "2":
          amount = float(input("Enter the amount you want to withdraw: "))
          myacc.withdraw(amount)
    elif entry == "3":
         myacc.check_balance()
    elif entry == "4":
         myacc.close()
   
    another_action = input("Do you want to perform another action?:  \n")
    if another_action == "no":
         break
     


        
# else: 
#  print("Invalid option. Please try again.")

    
