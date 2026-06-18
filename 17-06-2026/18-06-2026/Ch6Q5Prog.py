#to generate a sequence:-5, 10, -15, 20, -25... upto n, where n is an integer input by the user
n = int(input("Enter the number:"))

for n in range(1,n+1):
    n =(5*n)*((-1)**n)
    if n == n-1:
        break
    print(n)