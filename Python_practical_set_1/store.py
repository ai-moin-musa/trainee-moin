
class store:
	
	def __init__(self):
		self.shelves = {}
	
	def get_shelf_count(self):
		return len(self.shelves)
		
	def add_shelf_to_the_store(self,shelf_name,shelf_object):
		self.shelves[shelf_name] = shelf_object
	
	def display_all_shelves(self):
		return [key for key in self.shelves.keys()]
	
		
class shelf:
	
	def __init__(self,shelf_name):
		self.products = {}
		self.shelf_name = shelf_name
	
	def get_product_count(self):
		return len(self.products)
	
	def add_product_to_the_shelf(self,product_name,product_object):
		self.products[product_name] = product_object
	
	def update_sale_price_on_shelf(self,margin):
		for value in self.products.values():
			value.update_sale_price(margin)
			
	def get_min_max_sale_price(self):
		min_max_values_of_product_on_shelf = {}
		for product in products.values():
			min_value_product = product.get_min(self)
			max_value_produdt = product.get_max(self)
			min_max_values_of_product_on_shelf[product.product_name] = [min_value_product,max_value_product]
		return min_max_values_of_product_on_shelf
	
	def avg_cost_sale_based_on_month(self,month):
		avg_cost_of_products = []
		avg_sale_of_products = []
		for product in products.values():
			avg_cost_of_products.append(product.get_avg_cost_by_month(month))
			avg_sale_of_products.append(product.get_sale_cost_by_month(month))
			
		avg_cost_of_shelf = (sum(avg_cost_of_products)/len(avg_cost_of_products))
		avg_sale_of_shelf = (sum(avg_sale_of_products)/len(avg_sale_of_products))
		
		return avg_cost_of_shelf,avg_sale_of_shelf
		
	
	def profit(self,month):
		profit = []
		for product in products.values():
			profit.append(product.get_profit_by_month(month))
		return sum(profit)
			
		
class product:
	
	def __init__(self,product_name):
		self.product_name = product_name
		self.category = ''
		self.month_cp_sp = {}

		
	def set_category(category):
		self.category = category
		
	def set_cost_price(self,month,cp,margin):
		self.month_cp_sp[month]= {'cp':[],'sp':[]}
		self.month_cp_sp[month]['cp'].extend(cp)
		self.month_cp_sp[month]['sp'] = [(price + (price*margin)/100) for price in cp] 	
		print(self.month_cp_sp[month]['cp'])
		
	def get_sale_price(self,month):
		return self.month_cp_sp[month][sp]
	
	def get_cost_price(self,month):
		return self.month_cp_sp[month][cp]

	#method to update sale price with a given percentage.
	
	def update_sale_price(self,new_margin):
		self.month_cp_sp[month]['sp'] = [(price + (price*margin)/100) for price in (self.month_cp_sp[month]['cp'])]
		
	def reset_cp(self,month):
		self.month_cp_sp[month]['cp'] = [0]
		self.month_cp_sp[month]['sp'] = [0]
	
	def get_min(self):
		min_list = []
		for values in self.month_cp_sp.values():
			min_list.append(min(values['sp']))
		return min(min_list)
	
	def get_max(self):
		max_list = []
		for values in self.month_cp_sp.values():
			max_list.append(max(values['sp']))
		return max(max_list)
	
	def get_avg_cost_by_month(self,month):
		if month in self.month_cp_sp.keys():
			return (sum(self.month_cp_sp[month]['cp'])/len(self.month_cp_sp[month]['cp']))
		return 0
		
	def get_avg_sale_by_month(self,month):
		if month in self.month_cp_sp.keys():
			return (sum(self.month_cp_sp[month]['sp'])/len(self.month_cp_sp[month]['sp']))
		return 0
	
	def get_profit_by_month(self,month):
		if month in self.month_cp_sp.keys():
			profit = sum(self.month_cp_sp[month]['sp']) - sum(self.month_cp_sp[month]['cp'])
			return profit
		return 0
	
	def get_cp_sp_all_months(self):
		for month,cpsp in self.month_cp_sp.items():
			print(f"-{month}-")
			print(f"CP - {cpsp['cp']}")
			print(f"SP - {cpsp['sp']}")
		

def create_a_new_shelf(shelf_name):
	shelf1 = shelf(shelf_name) 
	print("shelf created...")  
	return shelf1
	
def create_a_new_product(product_name):
	product1 = product(product_name)
	return product1
	

def continueOrNotWithMessage(message):
    while True:
        try:
            choice = str(input(f"Do you want to {message}? (y/n): "))
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")


#excution starting from here.....
if __name__ == "__main__" :
	print("Welcome.................")
	mystore = store()
	
	while True:
		
		print("""
	operations on....
	1. Shelf 
	2. Product
	3. methods
	4. exit
	5. display
		""")
		try:
			choice = int(input("enter choice : "))
		except ValueError:
			print("Invalid Input!!! Please Try again")
			continue
		
		if choice == 1:
			
			while True:
				print("""
			1. add shelf
			2. display shelves
			3. exit
			""")
				try:
					sub_choice = int(input("enter choice : "))
				except ValueError:
					print("Invalid Input!!! Please Try again")
					continue
				if sub_choice == 1:
					while True:
						shelf_name = input("enter a shelf name : ")
						shelf_obj = create_a_new_shelf(shelf_name)
						mystore.add_shelf_to_the_store(shelf_name,shelf_obj)
						print(mystore.display_all_shelves())
						corn = continueOrNotWithMessage("add another shelf")
						if corn:
							continue
						else:
							break
	
				elif sub_choice == 2:
					print(mystore.display_all_shelves())
					
				elif sub_choice == 3:
					break
				else:
					print("Invalid choice!!! Please Try again...")
		elif choice == 2:
			while True:
				print("""
			1. add product
			2. display products with shelves
			3. exit
			""")
				try:
					sub_choice = int(input("enter choice : "))
				except ValueError:
					print("Invalid Input!!! Please Try again")
					continue
				if sub_choice == 1:
					while True:
						product_name = input("enter a product name : ")
						
						print(mystore.display_all_shelves())
						selected_shelf = input("Select Shelf for product : ")
						
						if selected_shelf not in mystore.shelves.keys():
							print("Invalid input!!! please Try again")
							break
						
						product_obj = create_a_new_product(product_name)
						shelf_obj = mystore.shelves[selected_shelf]
						shelf_obj.add_product_to_the_shelf(product_obj.product_name,product_obj)
						print("Added product to the shelf")
						while True:
							print("---adding cost price with month----")
							month = str(input("Enter month: "))
							cp = list(map(int,input("Enter cost price seperated by space : ").split(" ")))
							margin = int(input("Enter margin for sale price % :"))
							product_obj.set_cost_price(month,cp,margin)
							print("added cost price to the product by month")
							corn = continueOrNotWithMessage("add another month cost price")
							if corn:
								continue
							else:
								break
						
						corn = continueOrNotWithMessage("add another product")
						if corn:
							continue
						else:
							break
				elif sub_choice == 2:
					for shelf_name,shelf_obj in mystore.shelves.items():
						print(f"{shelf_name} --> ",end="")
						for product_name,product_obj in shelf_obj.products.items():
							print(f"{product_name}",end=" ")
						print("\n")
						
				elif sub_choice == 3:
					break
				
				else:
					print("Invalid choice!!! Please Try Again!!!")
				
				
		elif choice == 3:
			print("""
			1. update the sale price with a given percentage.
			2. update the sale price for a given shelf with a given percentage.
			
			""")
		elif choice == 4:
			break
		elif choice == 5:
			for shelf_name,shelf_obj in mystore.shelves.items():
				print(f"{shelf_name} --> ",end="")
				for product_name,product_obj in shelf_obj.products.items():
					print(f"{product_name}",end="\n")
					product_obj.get_cp_sp_all_months()
					
				print("\n")
		else:
			print("Invalid choice!!! Please Try again")
			continue
			
			
		
	
	


	
	



