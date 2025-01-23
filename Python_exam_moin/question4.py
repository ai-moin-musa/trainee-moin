

def make_sentence(string_list):
	
	for i in range(len(string_list)):
		
		if i == 0 and i != (len(string_list)-2):
			if string_list[i][0].lower() in ['a','i','o','e','u']:
				print(f"An {string_list[i]}",end=",")
			else:	
				print(f"A {string_list[i]}",end=",")
		elif i == (len(string_list)-2) and i == 0:
			if string_list[i][0].lower() in ['a','i','o','e','u']:
				print(f"An {string_list[i]}",end=" and ")
			else:	
				print(f"A {string_list[i]}",end=" and ")
		elif i == (len(string_list)-2):
			if string_list[i][0].lower() in ['a','i','o','e','u']:
				print(f"an {string_list[i]}",end=" and ")
			else:	
				print(f"a {string_list[i]}",end=" and ")
		elif i == (len(string_list)-1):
			if string_list[i][0].lower() in ['a','i','o','e','u']:
				print(f"an {string_list[i]}",end=".")
			else:	
				print(f"a {string_list[i]}",end=".")
		else:
			if string_list[i][0].lower() in ['a','i','o','e','u']:
				print(f"an {string_list[i]}",end=",")
			else:	
				print(f"a {string_list[i]}",end=",")
	
make_sentence(["car", "plane", "truck", "boat", "apple"])
