
def is_first_odd(num):
	temp = num//1000
	first_digit = temp%10
	return first_digit%2 != 0

def is_last_even(num):
	last_digit = num%10
	return last_digit%2 == 0
	
def check_conditions(num):
	#The number must be 4 digits long i.e (1000 to 9999)
	if num >= 1000 and num <= 9999:
		#The number must be divisible by either 3 or 7
		if num % 3 == 0 or num % 7 == 0:
			#The first digit of the number must be odd and the last digit must be even.
			if is_first_odd(num) and is_last_even(num):
				return True
			
def extract_nums(nums_list):
	extracted_num = [num for num in nums_list if check_conditions(num)]
	return extracted_num
	

try:
	nums_list = list(map(int,input("Enter numbers with seperated by space :").split(" ")))
	print(extract_nums(nums_list))
except Exception as e:
	print(e)
	


