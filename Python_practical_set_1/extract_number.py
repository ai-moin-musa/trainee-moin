
def is_second_digit_odd(num):
    temp = num//100
    second_digit = temp % 10
    return second_digit % 2 != 0

def is_last_digit_even(num):
    last_digit = num % 10
    return last_digit % 2 == 0

def check_condition(num):
    if 1000 <= num <= 9999:
        if num % 8 == 0 or num % 5 == 0:
            if is_second_digit_odd(num) and is_last_digit_even(num):
                return True
    return False

def extract_number(num_list):
    
    result = [num for num in num_list if check_condition(num)]
    return result

num_list = [1234, 2345, 3456, 4567, 1780, 5678, 6789, 7890, 8901, 9012, 1000, 1001, 1002, 1152,]

print(extract_number(num_list))

#output: [1780, 1152]