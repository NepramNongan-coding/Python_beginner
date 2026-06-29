#To find total no. of character,alphabet,digits,special symbol & word
text = input("Enter the text:")

l = len(text)
print("The total number of character is", l)

alp = sum(text.isalpha() for text in text)
print("The total number of alphabet is",alp)

dig = sum(text.isnumeric() for text in text)
print("The total number of digit is",dig)

spa = sum(text.isspace() for text in text)

sym = l-(alp+dig+spa)
print("The total number of special symbol is",sym)

word = len(text.split())
print("The total number of words is",word)