
#sum of digits entered by user..

num = int(input("Enter any number: "))
number=num
digit_sum = 0
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10

print("The sum of {} is: {}".format(number,digit_sum))
