
def is_armstrong(num):
    
    sum = 0
    temp = num
    n = 0

    if num in (range(1,10)):
        return True
    
    while num > 0 :
        num = num // 10
        n += 1

    num = temp 
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp = temp // 10
        
    if num == sum:
        return True
    else:
        return False

num = int(input("Enter a number :"))

print(is_armstrong(num))



     
