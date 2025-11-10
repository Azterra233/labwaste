#Palindrome String
def palindrome_str(s):
   return s[::-1]
s = input("Type something:")
rev = palindrome_str(s)
if s == rev:
    print(s, "is Palindrome!")
else:
    print(s, "is not a Palindrome!")

