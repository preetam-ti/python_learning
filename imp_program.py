##Febonici series:
x=0
y=1
feb = []
feb.append(x)
num = 0
while num<13:
    feb.append(y)
    temp=y
    y = x+y
    x = temp
    num = num +1

print(feb)

##Palindrum program in python :
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

##palindrum string:

str = 'JaVaJ'  
strstr = str.casefold()  
  
# This string is reverse.  
rev = reversed(str)  
  
if list(str) == list(rev):  
   print("PALINDROME !")  
else:  
   print("NOT PALINDROME !")  
