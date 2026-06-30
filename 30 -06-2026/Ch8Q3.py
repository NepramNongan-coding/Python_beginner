def deleteChar(str,char):
    newstring = ""
    for ch in str:
        if ch!=char:
            newstring+=ch
    return newstring

str = input("Enter the string:")
char = input("Enter the character you want to remove:")

newstring = deleteChar(str,char)
print(newstring)