#write a script to print substring of string..

string = input("Enter a string: ")
start = int(input("Enter the starting index: "))
end = int(input("Enter the ending index: "))

substring = string[start:end]

print("\nSubstring Which Starts From", start, "Index No. And Ends At", end, "Index No. Is:", substring)
