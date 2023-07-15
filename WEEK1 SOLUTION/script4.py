# write a script to check number is armstrong or not..!
a = int(input("Enter any number: "))
sum=0
t=a
while(a>0):
    b=a%10
    c=b*b*b
    a=a//10
    sum=sum+c
if(sum==t):
    print("{} is armstrong.".format(t))
else:
    print("{} is not armstrong..!".format(t))
