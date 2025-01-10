def decorator(func):
	def wrapper():
		
		string = func()
		return string
		
	return wrapper
	
def second_decorator(func):

	def wrapper(*args):
		func(*args)
		print(args[0])
		func(*args)
		
	return wrapper
	
@decorator
def print_string(string):
	return string

@second_decorator
def print_pattern(string):
	print("*****")
	print("%%%%%")
	
string = str(input("Enter a string : "))
print_pattern(string)
