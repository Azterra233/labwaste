# Menu Driven Calculator
def add(x, y):
    return x + y    
def subtract(x, y):
    return x - y
def product(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
print("Select operation of your choice:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("The sum is: ", add(x, y))
elif choice == 2:
    print("The difference is: ", subtract(x, y))
elif choice == 3:   
    print("The product is: ", product(x, y))
elif choice == 4:
    print("The quotient is:", divide(x,y))