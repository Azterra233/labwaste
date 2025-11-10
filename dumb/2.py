# Menu Driven Calculator
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
input("Select operation of choice:")
choice = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n 4. Division\n: "))
if choice == 1:
    print("The sum is: ", a + b)
elif choice == 2:
    print("The difference is: ", a - b)
elif choice == 3:
    print("The product is: ", a * b)
elif choice == 4:
    if b != 0:
        print("The quotient is: ", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")








