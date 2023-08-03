#Write A Script To Print Index Value Instead of Printing Vowels In String....
string = input("Enter any string: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

u_string = ""
for i in range(len(string)):
    if string[i] in vowels:
        u_string += str(i)
    else:
        u_string += string[i]

print("\n\tInputted String Is:", string)
print("\tAfter coverting index number at vowels space the  String Is:", u_string)
