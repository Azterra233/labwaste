# Reverse of a number
n=int(input("Enter a number: "))
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reversed Number:",rev)
# This program takes an integer input from the user and reverses the digits of that number.
# For example, if the user inputs 1234, the output will be 4321.