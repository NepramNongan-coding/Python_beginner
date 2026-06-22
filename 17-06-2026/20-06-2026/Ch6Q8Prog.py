#to check whether the input number is palindrome or not
def palin(n):
    rev_n = n[::-1]
    if n == rev_n:
        print("The input number is palindrome.")
    else:
        print("The input number is not palindrome.")
n = input("Enter the number:")
palin(n)