def reverse_string(string):
	string = list(string) #converting string into list because of we cant change in existing string. strings are immutable. 
	head = 0
	tail = (len(string)-1)
	new_string = ''
	while head < tail:	
		if string[head].isalpha() and string[tail].isalpha():
			string[head],string[tail] = string[tail],string[head]
			head += 1
			tail -= 1
		elif not string[head].isalpha():
			head += 1
		else:
			tail -= 1
		
	#converting list into string
	for s in string:
		new_string += s
		
	return new_string	

try:
	string = str(input("Enter string : "))
except Exception as e:
	print(f"Error occured : {e}")

print(reverse_string(string))

"""
#Test case-1
print(reverse_string('moin-s'))
#Test case-2
print(reverse_string('a-bC-dEf-ghIj'))
#Test case-3
print(reverse_string('Test1ng-Leet=code-Q!'))
#Test case-4
print(reverse_string('Test 1'))"""
