# write a script to enter string and count number of vowels
a=input("enter any string:")
v=0
for i in a:
    if(i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E' or i=='I' or i=='O' or i=='U'):
        v=v+1
print("total number of vowels in this string :",v)
