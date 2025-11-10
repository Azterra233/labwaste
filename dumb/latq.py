# Program to print a triangle pattern of numbers starting from 1 to 9
n = int(input("Enter number of rows: "))
pattern = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(pattern, end=' ')
        pattern += 1
        if pattern > 9:
            pattern = 1
    print()