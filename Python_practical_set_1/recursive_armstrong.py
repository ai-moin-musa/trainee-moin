def is_armstrong(num):
    if num in (range(1,10)):
        return True
    n = 0
    temp = num
    while temp > 0 :
        temp = temp // 10
        n += 1
    
    sum = armstrong(num,n)
    return num == sum

def armstrong(num, n,sum = 0):
  
    
    if num == 0:
        return sum
    else:
        digit = num % 10
        sum += digit ** n
        num = num // 10
        return armstrong(num, n, sum)  
    
num = int(input("Enter a number: "))
    
print(is_armstrong(num))