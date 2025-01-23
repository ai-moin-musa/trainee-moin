def get_two_indices(nums,target):
	#take element one by one
	for i in range(len(nums)):
		#take remaining element one by one after selected element
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] ==  target:
				return list([i,j])



try:
	nums = list(map(int,input("Enter numbers seperated by space : ").split()))
	target = int(input("Enter your Target sum : "))
except Exception as e:
	print(f"Exception occurred : {e}")

print(get_two_indices(nums,target))



"""#Test case -1 
nums = [-3, 2, 3, 1, -10,0]
target = 0
print(get_two_indices(nums,target))

#Test case -2
nums = [2, 7, 11, 15]
target = 9
print(get_two_indices(nums,target))

#Test case -3
nums = [3, 2, 3, 1, 4]
target = 7
print(get_two_indices(nums,target))

#Test case -4
nums = [3, -2, 3, 1, 4, -12]
target = -8
print(get_two_indices(nums,target))

#Test case -5
nums = [3, -2, 3, 1, 4, -12]
target = -14
print(get_two_indices(nums,target))"""
