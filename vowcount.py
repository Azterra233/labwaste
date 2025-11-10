#Count vowels
vowels = ["a", "e", "i", "o", "u"]
x = input("Type a string:").lower()
s = 0
for i in x:
    if(i in vowels):
        s += 1
print (s)

       
