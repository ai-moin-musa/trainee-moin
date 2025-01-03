def operations_menu():
	print("""
		1. add
		2. update
		3. delete
		4. exit
	""")	
	
	
def sub_menu():
	print("""
		(i)   country
		(ii)  state
		(iii) city
		(iv)  exit 
	""")

while(True):
	
	operations_menu()
	
	try:
		operation = int(input())
	except:
		print('please try again, error occured')
		continue
	
	try:
		if operation > 4 or operation <= 0:
			print('please, enter valid option')
			continue
		
		elif operation == 4:
			break
	except:
		print('please, try again, error occured')
		continue
		
	print('success') 
	

	
	
	
	


	
	




	
	
		
	
	
	

