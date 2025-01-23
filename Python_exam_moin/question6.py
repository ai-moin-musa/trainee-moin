import datetime

def get_age_and_leap_year(dob):
	dob_year, dob_month, dob_date = map(int,dob.split("-"))
	x = datetime.datetime.now()
	age = 0
	leap_year_after_dob = []
	#check current year date of birth month is gone or not
	if x.month > dob_month:
		age = x.year - dob_year
	else:
		age = x.year - dob_year - 1
	
	for year in range(dob_year+1,x.year):
		if year%4 == 0 or (year%100 == 0 and year%400 == 0):
			leap_year_after_dob.append(year)
	
	print(f"Your current age is {age} years.")
	print(f"Leap years after your birthdate: {leap_year_after_dob}") 


try:
	dob = str(input("Enter your birthdate (YYYY-MM-DD): "))
	get_age_and_leap_year(dob)
except Exception as e:
	print("Invalid Input!!! Please Try again")


	

