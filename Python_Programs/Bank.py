class BankAccount:
	def __init__(self, holder, balance=0.0):
		self.account_number = ''
		self.holder = holder
		self.balance = balance if balance >= 0 else 0

	def generate_account_number(self):
		try:
			while True:
				ac = int(input("Enter a account number : "))
				if str(ac) in accounts['saving'] or str(ac) in accounts['current']:
					print("Account number already exists Please select other account number")
					continue
				break
			self.account_number = str(ac)
			print(f"Successfully generated account no : {self.account_number}")
		except Exception as e:
			print(f"Invalid Input!!! Please Try Again.")
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
		interest = (self.balance * year * self.interest_rate) / 100
		print(f"Calculated interest: {interest}")
		return interest

	def apply_interest(self, year):
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
            
def menu_show():
	print("\n!!!!!! Welcome to the Bank !!!!!!")
	print("1. Create Savings Account")
	print("2. Create Current Account")
	print("3. Deposit Amount")
	print("4. Withdraw Amount")
	print("5. Check Balance")
	print("6. Calculate Interest (Savings Account Only)")
	print("7. Apply Interest (Savings Account Only)")
	print("8. Withdraw with Overdraft (Current Account Only)")
	print("9. Exit")

def create_saving_account():
	try:
		holder = str(input("Enter holder name: "))
		if holder.isalpha():
			pass
		else:
			print("Please Try Again Holder name can not be number")
			return
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

def create_current_account():
	try:
		holder = str(input("Enter holder name: "))
		if holder.isalpha():
			pass
		else:
			print("Please Try Again Holder name can not be number")
			return
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

def deposit_amount():
	current = False
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['saving']:
			if str(ac) not in accounts['current']:
				print("Account No is incorrect!!! Please Try Again.")
				return
			current = True
		if current:
			obj = accounts['current'][str(ac)]
		else:
			obj = accounts['saving'][str(ac)]
		amount = int(input("Enter amount do you want deposit : "))
		obj.deposit(amount)
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

def withdraw_amount():
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['saving']:
			print("Account No is incorrect!!! Please Try Again")
			return
		obj = accounts['saving'][str(ac)]
		amount = int(input("Enter amount do you want withdraw : "))
		obj.withdraw(amount)
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

def check_balance():
	current = False
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['saving']:
			if str(ac) not in accounts['current']:
				print("Account No is incorrect!!! Please Try Again.")
				return
			current = True
		if current:
			obj = accounts['current'][str(ac)]
		else:
			obj = accounts['saving'][str(ac)]
		obj.display_balance()
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

def calculate_interest():
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['saving']:
			print("Account No is incorrect!!! Please Try Again")
			return
		obj = accounts['saving'][str(ac)]
		year = int(input("Enter time / years for apply interest : "))
		obj.calculate_interest(year)
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

def apply_interest():
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['saving']:
			print("Account No is incorrect!!! Please Try Again")
			return
		obj = accounts['saving'][str(ac)]
		year = int(input("Enter time / years for apply interest : "))
		obj.apply_interest(year)
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

def withdraw_with_overdraft():
	try:
		ac = int(input("Enter account number: "))
		if str(ac) not in accounts['current']:
			print("Account No is incorrect!!! Please Try Again")
			return
		obj = accounts['current'][str(ac)]
		amount = int(input("Enter amount do you want withdraw : "))
		obj.withdraw(amount)
	except ValueError:
		print("Invalid Input!!! Please Try Again.")

# Example Usage
if __name__ == "__main__":
	accounts = {'saving': {}, 'current': {}}
	while True:
		menu_show()
		try:
			choice = int(input("Enter your choice :"))
			if choice == 1:
				create_saving_account()
			elif choice == 2:
				create_current_account()
			elif choice == 3:
				deposit_amount()
			elif choice == 4:
				withdraw_amount()
			elif choice == 5:
				check_balance()
			elif choice == 6:
				calculate_interest()
			elif choice == 7:
				apply_interest()
			elif choice == 8:
				withdraw_with_overdraft()
			elif choice == 9:
				break
			else:
				print("Invalid choice!!! Please Try Again.")
		except ValueError:
			print("Invalid Input !!! Please Try Again.")