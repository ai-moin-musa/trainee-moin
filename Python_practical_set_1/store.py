
class store:
	
	def __init__(self):
		self.shelves = {}
	
	def get_shelf_count(self):
		return len(self.shelves)
		
	def add_shelf_to_the_store(self,shelf_name,shelf_object):
		self.shelves[shelf_name] = shelf_object
	
	def display_all_shelves(self):
		return [key for key in self.shelves.keys()]
	
	def display_products(self):
		for shelf_name,shelf_obj in mystore.shelves.items():
			print(f"{shelf_name} --> ",end="")
			for product_name,product_obj in shelf_obj.products.items():
				print(f"{product_name}",end=" ")
			print("\n")
		
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
		for product in self.products.values():
			min_value_product = product.get_min()
			max_value_product = product.get_max()
			min_max_values_of_product_on_shelf[product.product_name] = [min_value_product,max_value_product]
		return min_max_values_of_product_on_shelf
	
	def avg_cost_sale_based_on_month(self,month):
		avg_cost_of_products = []
		avg_sale_of_products = []
		for product in self.products.values():
			avg_cost_of_products.append(product.get_avg_cost_by_month(month))
			avg_sale_of_products.append(product.get_avg_sale_by_month(month))
			
		avg_cost_of_shelf = (sum(avg_cost_of_products)/len(avg_cost_of_products))
		avg_sale_of_shelf = (sum(avg_sale_of_products)/len(avg_sale_of_products))
		
		return avg_cost_of_shelf,avg_sale_of_shelf
		
	
	def profit(self,month):
		profit = []
		for product in self.products.values():
			profit.append(product.get_profit_by_month(month))
		return sum(profit)
			
		
class product:
	
	def __init__(self,product_name):
		self.product_name = product_name
		self.category = ''
		self.month_cp_sp = {}

		
	def set_category(self,category):
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
	
	def update_sale_price_by_product(self,month,new_margin):
		print(f"old sp :{self.month_cp_sp[month]['sp']}")
		self.month_cp_sp[month]['sp'] = [(price + (price*new_margin)/100) for price in (self.month_cp_sp[month]['cp'])]
		print(f"new sp :{self.month_cp_sp[month]['sp']}")
		return True
	
	def update_sale_price(self,new_margin):
		for month in self.month_cp_sp.keys():
			self.month_cp_sp[month]['sp'] = [(price + (price*new_margin)/100) for price in (self.month_cp_sp[month]['cp'])]
		
	
		
	def get_months(self):
		return self.month_cp_sp.keys()
		
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


def update_sale_price():
	try:
	
		shelf = str(input("choose shelf : "))
		if shelf not in mystore.shelves.keys():
			print("Invalid input!!! please Try again")
			return Fasle
		product = str(input("choose product : "))
		if product not in (mystore.shelves[shelf].products.keys()):
			print("Inavalid input!!! please Try again")
			return False
		product_obj = mystore.shelves[shelf].products[product]
		print(list(mystore.shelves[shelf].products[product].get_months()))
		month = str(input("choose month :"))
		if month not in (mystore.shelves[shelf].products[product].get_months()):
			print("Invalid input!!! please Try again")
			return False 
		margin = int(input("Enter new margin : "))
		return product_obj.update_sale_price_by_product(month,margin)
		
		
	except Exception as e:
		print(f"{e}")

def take_product_object():
	try:
		shelf = str(input("choose shelf : "))
		if shelf not in mystore.shelves.keys():
			print("Invalid input!!! please Try again")
			return Fasle
		product = str(input("choose product : "))
		if product not in (mystore.shelves[shelf].products.keys()):
			print("Inavalid input!!! please Try again")
			return False
		product_obj = mystore.shelves[shelf].products[product]
		return product_obj
	except Exception as e:
		print(f"{e}")


	
	

#excution starting from here.....
if __name__ == "__main__" :
	print("Welcome.................")
	mystore = store()
	predefined_months = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec')
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
							month = str(input("Enter month (ex:'Jan'): "))
							if month.lower() not in predefined_months:
								print("Enter valid month!!! Please Try again!!!")
								continue
							try:
								cp = list(map(int,input("Enter cost price seperated by space : ").split(" ")))
								margin = int(input("Enter margin for sale price % :"))
								product_obj.set_cost_price(month,cp,margin)
								print("added cost price to the product by month")
								corn = continueOrNotWithMessage("add another month cost price")
								if corn:
									continue
								else:
									break
							except Exception as e:
								print("something went wrong!!! please try again!!!")
								continue
						
						corn = continueOrNotWithMessage("add another product")
						if corn:
							continue
						else:
							break
				elif sub_choice == 2:
					mystore.display_products()
						
				elif sub_choice == 3:
					break
				
				else:
					print("Invalid choice!!! Please Try Again!!!")
				
				
		elif choice == 3:
			while True:
				print("""
1. update the sale price with a given percentage.
2. update the sale price for a given shelf with a given percentage.
3. Method to set a category for a given product.
4. Method to create a new shelf. ( go through with menu )
5. Method to reset cost price with 0 for a given shelf, product, and month.
6. Method to get the maximum or minimum price with the shelf name of a product.
   Display a proper message that shows the shelf and product.
7. Define the method and display the Average cost and a sale also profit based on
   the shelf for a specific month.
8. Display the Average cost and sales also profit based on the product for a specific
   month.
9. exit
				""")
				try:
					sub_choice = int(input("enter choice : "))
					if sub_choice == 1:
						mystore.display_products()
						result = update_sale_price()
						if result:
							print("sale price updated successfully.")
						else:
							print("sale price is not updated !!! Please Try again.")
							
					elif sub_choice == 2:
						print(mystore.display_all_shelves())
						shelf = str(input("choose shelf for updating sale price : "))
						if shelf not in mystore.shelves.keys():
							print("no shelf found!!! Please try again.")
							continue
						shelf_obj = mystore.shelves[shelf]
						try:
							margin = int(input("Enter new margin for shelf products : "))
							shelf_obj.update_sale_price_on_shelf(margin)
							print("sale price updated on shelf successfully")
						except Exception as e:
							print("something went wrong!!! please try again.")
					elif sub_choice == 3:
						mystore.display_products()
						product_obj = take_product_object()
						if product_obj == False:
							print("something went wrong please try again")
							
						category = str(input("Enter category for the product : "))
						product_obj.set_category(category)
						print(f"successfully set category {product_obj.category} for {product_obj.product_name}")
					elif sub_choice == 4:
						pass
					elif sub_choice == 5:
						mystore.display_products()
						product_obj = take_product_object()
						print(list(product_obj.get_months()))
						month = str(input("choose month :"))
						if month not in list(product_obj.get_months()):
							print("Invalid input!!! please Try again")
							continue
						product_obj.reset_cp(month)
						print("successfully reset cost price")
						 
					elif sub_choice == 6:
						for sname,sobject in mystore.shelves.items():
							result = sobject.get_min_max_sale_price()
							for key,value in result.items():
								print(f"{sname} --> {key} --> min: {value[0]} max: {value[1]}")
					elif sub_choice == 7:
						print(mystore.display_all_shelves())
						shelf = str(input("choose shelf: "))
						if shelf not in mystore.shelves.keys():
							print("no shelf found!!! Please try again.")
							continue
						shelf_obj = mystore.shelves[shelf]
						month = str(input("Enter month (ex 'Jan'):"))
						if month not in predefined_months:
							print("enter valid month")
							continue
						avg_cost_price, avg_sale_price = shelf_obj.avg_cost_sale_based_on_month(month)
						profit_shelf =  shelf_obj.profit(month)
						print(f"{shelf_obj.shelf_name} Average cost price on {month} is {avg_cost_price}")
						print(f"{shelf_obj.shelf_name} Average sale price on {month} is {avg_sale_price}")
						print(f"{shelf_obj.shelf_name} Average profit on {month} is {profit_shelf}")
					elif sub_choice == 8:
						mystore.display_products()
						product_obj = take_product_object()
						month = str(input("choose month :"))
						if month not in predefined_months:
							print("Invalid input!!! please Try again")
							continue
						avg_cost = product_obj.get_avg_cost_by_month(month)
						avg_sale = product_obj.get_avg_sale_by_month(month)
						profit = product_obj.get_profit_by_month(month)
						print(f"{product_obj.product_name} Average cost price on {month} is {avg_cost}")
						print(f"{product_obj.product_name} Average sale price on {month} is {avg_sale}")
						print(f"{product_obj.product_name} profit on {month} is {profit}")
					elif sub_choice == 9:
						break
					else:
						print("Invalid choice!!! Please Try again!!!")
						continue
				except Exception as e:
					print(e)
					#print("something went wrong!!! please try again!!!")
					continue
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
			
