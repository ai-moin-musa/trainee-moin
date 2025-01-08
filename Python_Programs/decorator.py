import time
def decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Result: {result}")
        return result
    return wrapper




@decorator
def add(a, b):
    return a + b

@decorator
def subtract(a, b):
    return a - b

@decorator
def multiply(a, b):
    return a * b

@decorator
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

@decorator
def modulo(a, b):
    return a % b

@decorator
def power(a, b):
    return a ** b

start = time.time()
while True:

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "6":
        break
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter number.")
      
    if choice == '1':
        add(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiply(num1, num2)
    elif choice == '4':
        divide(num1, num2)
    elif choice == '5':
        modulo(num1, num2)
    else:
        print("Invalid choice! Please select a valid operation.")

end = time.time()

print(f"time taken by program: {end - start}")
