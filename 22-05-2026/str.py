def replaceVowel(st):
    newstr = ''
    for character in st:
        if character in 'aeiouAEIOU':
            newstr += '*'
        else:
            newstr += character
    return newstr
st = input("Enter a String: ")
st1 = replaceVowel(st)
print("The original String is:",st)
print("The modified String is:",st1)