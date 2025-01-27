import random

class BankAccount:
    def __init__(self, holder, balance=0.0):
    	self.account_number = ''	
    	self.holder = holder
    	self.balance = balance if balance >= 0 else 0
    
    
    def generate_account_number(self):
    		for i in range(1, 11):
    			self.account_number += str(random.randrange(0,9))
    			
    def get_account_number(self):
    	return self.account_number
    
    	
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Holder: {self.holder}, Balance: {self.balance}")

class SavingAccount(BankAccount):
    def __init__(self, holder, balance=0.0, interest_rate=0.0):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate if interest_rate > 0 and interest_rate <= 100 else 10
        
	
    def calculate_interest(self, year):
        interest = (self.balance * year * self.interest_rate)/100
        print(f"Calculated interest: {interest}")
        return interest

    def apply_interest(self,year):
        interest = self.calculate_interest(year)
        self.balance += interest
        print(f"Interest applied. New balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, holder, balance=0.0, overdraft_limit=0.0):
        super().__init__(holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Exceeded overdraft limit or invalid amount.")
            
def first_menu_show():
	print("""
  First Menu------------
  1. opening New Account 
  2. existing Account
  3. exit
    	""")
    	
def second_menu_show():
	print("""
  Opening New Acccount/Second Menu----------
  1. Saving Account
  2. Current Account
  3. exit
    	     """)

def existing_second_menu():
	print("""
  Existing Account/Second Menu----------
  1. Saving Account
  2. Current Account
  3. exit
    		""")

def existing_third_menu():
	print("""
  Existing Account/saving account/Third Menu----------
  1. Display Balance
  2. Deposit
  3. Withdraw
  4. calculate interest rate
  5. apply interest rate
  6. exit
    		""")

def saving_third_menu():
	print("""
  Existing Account/saving account/Third Menu----------
  1. Display Balance
  2. Deposit
  3. Withdraw
  5. exit
    		""")

def opening_new_account():
	while True:
		second_menu_show()
		try:
			sub_choice = int(input("Enter a sub choice : "))    				
			if sub_choice == 1:
    				try:
    					holder = str(input("Enter holder name: "))
    					interest_rate = int(input("Enter interest rate(%): "))
    					balance = int(input("Enter balance amount : "))
    					SavingAccountObj = SavingAccount(holder, balance, interest_rate)
    					SavingAccountObj.generate_account_number()
    					ac = SavingAccountObj.get_account_number()
    					accounts['saving'][ac] = SavingAccountObj
    					print("account successfully created")
    					print(f"A/C NO: {ac}")
    					print(f"Name: {holder}")
    					print(f"interest rate: {accounts['saving'][ac].interest_rate}")
    					print(f"balance: {accounts['saving'][ac].balance}")
    				except ValueError:
    					print("Invalid Input!!! Please Try Again.")
			elif sub_choice == 2:
    				try:
    					holder = str(input("Enter holder name: "))
    					balance = int(input("Enter balance amount : "))
    					overdraft_limit = int(input("Enter overdraft_limit: "))		
    					CurrAccountObj = CurrentAccount(holder, balance, overdraft_limit)
    					CurrAccountObj.generate_account_number()
    					ac = CurrAccountObj.get_account_number()
    					accounts['current'][ac] = CurrAccountObj
    					print("account successfully created")
    					print(f"A/C NO: {ac}")
    					print(f"Name: {holder}")
    					print(f"overdraft limit: {accounts['current'][ac].overdraft_limit}")
    					print(f"balance: {accounts['current'][ac].balance}")
    				except ValueError:
    					print("Invalid Input!!! Please Try Again.")
			elif sub_choice == 3:
				break
			else:
				print("Invalid choice !!! Please Try Again !!!")
				continue
		except ValueError:
			print("Enter a valid input!!! Please Try Again!!!")

		
    		
    	
def existing_account():
	while True:
		existing_second_menu()
		try:
			sub_choice = int(input("Enter sub choice : "))
			if sub_choice == 1:
    				ac = int(input("Enter account number: "))
    				if str(ac) not in accounts['saving']:
    					print("Account No is incorrect!!! Please Try Again")
    					continue
    				obj = accounts['saving'][str(ac)]
    				while True:
    					existing_third_menu()
    					sub_choice = int(input("Enter choice : "))
    					if sub_choice == 1:
    						obj.display_balance()
    					elif sub_choice == 2:
    						amount = int(input("Enter amount do you want deposit : "))
    						obj.deposit(amount)
    					elif sub_choice == 3:
    						amount = int(input("Enter amount do you want withdraw : "))
    						obj.withdraw(amount)
    					elif sub_choice == 4:
    						year = int(input("Enter time / years for calculating interest : "))
    						obj.calculate_interest(year)		
    					elif sub_choice == 5:
    						year = int(input("Enter time / years for apply interest : "))
    						obj.apply_interest(year)
    					elif sub_choice == 6:
    						break
    					else:
    						print("Invalid choice!!! Please Try Again.")
			elif sub_choice == 2:
				ac = int(input("Enter account number: "))
				if str(ac) not in accounts['current']:
    					print("Account No is incorrect!!! Please Try Again")
    					continue
				obj = accounts['current'][str(ac)]
				while True:
    					saving_third_menu()
    					sub_choice = int(input("Enter choice : "))
    					if sub_choice == 1:
    						obj.display_balance()	
    					elif sub_choice == 2:
    						amount = int(input("Enter amount do you want deposit : "))
    						obj.deposit(amount)
    					elif sub_choice == 3:
    						amount = int(input("Enter amount do you want withdraw : "))
    						obj.withdraw(amount)
    					elif sub_choice == 5:
    						break
    					else:
    						print("Invalid choice!!! Please Try Again.")		
			elif sub_choice == 3:
    				break
			else:
    				print("Invalid choice!!! Please Try Again.")
    				continue
		except ValueError:
			print("Invalid Input !!! Please Try Again.")
    					
    					

    	     
# Example Usage
if __name__ == "__main__":


    accounts = {'saving':{},'current':{}}
    while True:
    	first_menu_show()
    	try:
    		choice = int(input("Enter a choice : "))
    		
    		if choice == 1:
    			opening_new_account()
    		elif choice == 2:
    			existing_account()
    		elif choice == 3:
    			break
    		else:
    			print("Invalid choice!!! Please try again.!")
    			continue
    			
    	except ValueError:
    		print("Invalid Input!!! Please Enter an integer!")
    		continue
