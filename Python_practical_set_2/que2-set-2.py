def check_conditions(string):
	
	new_string = string
	#The first character must capitalize and consonant.
	if string == new_string.capitalize() and (new_string.capitalize()[0]) not in ('A','E','I','O','U'):
		#The string must not contain any number.
		if string.isalpha():
			return True
	return False
	

def extract_string(string_list):
	string_list = [string for string in string_list if check_conditions(string)]
	return string_list

try:
	string_list = [string for string in list(map(str,input("Enter multiple string with seperated by space :").split(" ")))]
	print(extract_string(string_list))
except Exception as e:
	print(f"something went wrong!!! Please Try Again!!!")
