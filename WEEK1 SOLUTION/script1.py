#check number is prime or not...
n= int(input("Enter any number: "))
for i in range(2,n):
    if n%i==0:
        print("{} is not prime number...!".format(n))
        break
else:
    print("{} is prime number.".format(n))
