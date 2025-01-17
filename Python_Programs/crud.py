
'''
****Data Structure****

data = {
    "india":{
        "Gujarat": ["Palanpur","Ahmedabad","Surat","Mahesana","Vadodara"],
        "Rajasthan": ["Jaipur","Udaipur","Ajmer","Jodhpur","Bikaner"],
        "Maharashtra": ["Mumbai","Pune","Nagpur","Nashik","Kolhapur"]
    },
    "Australia":{
    	"South Australia": ["Sydney"]
    
    }
}
'''
data = {}


def continueOrNot():
    while True:
        try:
            choice = str(input("Do you want to continue? (y/n): "))
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")

def validate_to_string(string):
    if not string.isalpha():
    	print("Please Enter string !!!")
    	return False
    return True


def is_country(country):
    if country not in data:
        print("Country not found. Please try again.")
        return False
    return True


def is_state(country, state):
    if state not in data[country]:
        print("State not found. Please try again.")
        return False
    return True


def is_city(country, state, city):
    if city not in data[country][state]:
        print("City not found. Please try again.")
        return False
    return True


def add_country(country):
    if country.lower() in data:
    	print('country already exits')
    else:
    	data[country.lower()] = {}


def Display_state(country):
    print("States: ", list(data[country].keys()))


def Display_city(country, state):
    print("cities: ", list(data[country][state]))


def Display_country():
    print("Countries: ", list(data.keys()))


def is_country_empty():
    if not bool(data):
        print("empty!!! country not found")
        return False
    return True


def is_city_empty(country, state):
    if not bool(data[country][state]):
        print("empty!!! city not found")
        return False
    return True


def is_state_empty(country):
    if not bool(data[country]):
        print("empty!!! state not found")
        return False
    return True

	
def input_state():
    while True:
    	 state = str(input("Enter state name: "))
    	 val =  validate_to_string(state)
    	 if not val:
    	 	continue
    	 return state.lower()

def input_country():
    while True:
    	country = str(input("Enter Country name: "))
    	val = validate_to_string(country)
    	if not val:
    		continue
    	return country.lower()
    	 
def input_city():
    while True:
    	city = str(input("Enter City name: "))
    	val = validate_to_string(city)
    	if not val:
    		continue
    	return city.lower()

#execution starts here-----------------
       
while True:

    print("""
        Select operation:
           1. Add
           2. Update
           3. Delete
           4. Exit
           5. Display
    """) 
    
    try:
        choice = int(input("Enter choice: "))  
        
        if choice == 1:
        
            while True:
            
                print("""
                    ****ADD****
                    Select option:
                      1. Country
                      2. State
                      3. City
                      4. Exit
                """)
                
                try:
                    sub_choice = int(input("Enter choice: "))
                    if sub_choice == 1:
             
                        while True:
                            try:
                                country = input_country()
                                add_country(country)
                                print(data)
                                corn= continueOrNot()
                                if corn:
                                    continue
                                else:
                                    break
                                    
                                    	
                            except ValueError:
                                print("Invalid input. Please enter a string.")
                                continue
                                
                    elif sub_choice == 2:
                    
                        while True:
                        
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            state = input_state()
                            
                            if state.lower() in data[country.lower()]:
                            	print("state is already exits!!!")
                            	continue
                                
                            data[country.lower()][state.lower()] = []

                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break

                    elif sub_choice == 3:  
                        
                        while True: 
                            Display_country()
                            if not is_country_empty():
                                break
                            
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            if not is_state_empty(country.lower()):
                                break
                            Display_state(country.lower())
                            
                            state = str(input("select state name: "))
                            if not is_state(country.lower(), state.lower()):
                            	continue
                            city = input_city()
                            if city.lower() in data[country.lower()][state.lower()]:
                            	print("city is already exits!!!")
                            	continue
                            data[country.lower()][state.lower()].append(city.lower())
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break

                    elif sub_choice == 4:
                        break
                    else:
                        print("Invalid choice. Please try again.")


                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
        
        elif choice == 2:
        
            while True:
                print("""
                    ****Update*****
                      Select option:
                        1. Country
                        2. State
                        3. City
                        4. Exit
                """)
                try:
                    sub_choice = int(input("Enter choice: "))
                    if sub_choice == 1:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            new_country = input_country()
                            
                            data[new_country.lower()] = data.pop(country.lower())
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 2:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            if not is_state_empty(country.lower()):
                            	break
                            Display_state(country.lower())
                            state = str(input("select state name: "))
                            if not is_state(country.lower(), state.lower()):
                            	continue
                            new_state = input_state()
                            data[country.lower()][new_state.lower()] = data[country.lower()].pop(state.lower())
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 3:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            Display_state(country.lower())
                            if not is_state_empty(country.lower()):
                            	break
                            state = str(input("select state name: "))
                            if not is_state(country.lower(), state.lower()):
                            	continue
                            Display_city(country.lower(), state.lower())
                            if not is_city_empty(country.lower(), state.lower()):
                            	break
                            city = str(input("select city name: "))
                            if not is_city(country.lower(), state.lower(), city.lower()):
                            	continue
                            new_city = input_city()
                            
                            data[country.lower()][state.lower()].remove(city)
                            
                            if new_city in data[country.lower()][state.lower()]:
                            	print('city is already exits please try again')
                            	break
                            	
                            data[country.lower()][state.lower()].append(new_city)
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 4:
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
        
        elif choice == 3:
        
            while True:
                print("""
                    ****Delete*****
                      Select option:
                        1. Country
                        2. State
                        3. City
                        4. Exit
                """)
                try:
                    sub_choice = int(input("Enter choice: "))
                    if sub_choice == 1:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            data.pop(country.lower())
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 2:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            Display_state(country.lower())
                            if not is_state_empty(country.lower()):
                            	break
                            state = str(input("select state name: "))
                            if not is_state(country.lower(), state.lower()):
                            	continue
                            data[country.lower()].pop(state.lower())
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 3:
                    
                        while True:
                            Display_country()
                            if not is_country_empty(): 
                                break
                            country = str(input("select country name: "))
                            if not is_country(country.lower()):
                            	continue
                            if not is_state_empty(country.lower()):
                            	break
                            Display_state(country.lower())
                            state = str(input("select state name: "))
                            if not is_state(country.lower(), state.lower()):
                            	continue
                                
                            if not is_city_empty(country.lower(), state.lower()):
                            	break
                            	
                            
                            Display_city(country.lower(), state.lower())
                            
                            city = str(input("select city name: "))
                            if not is_city(country.lower(), state.lower(), city.lower()):
                            	continue
                            
                            data[country.lower()][state.lower()].remove(city)
                            print(data)
                            corn= continueOrNot()
                            if corn:
                                continue
                            else:
                                break
                                
                    elif sub_choice == 4:
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
        
        elif choice == 4:
            break
        
        elif choice == 5:
            print(f"{data}")

        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
