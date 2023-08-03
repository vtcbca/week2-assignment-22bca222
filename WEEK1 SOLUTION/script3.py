#write a script to check number is palindrome or not..!
a = int(input("Enter any number: "))
t=a
r=0
while(a>0):
    b=a%10
    r=r*10+b
    a=a//10
if(r==t):
    print("{} is plindrome.".format(t))
else:
    print("{} is not plindrome..!".format(t))
