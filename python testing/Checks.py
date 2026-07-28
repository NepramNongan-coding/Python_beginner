#To check whether a number is prime
n = int(input("Enter the number:"))
if n<2:
    print("Invalid Input")
else:
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime = False
            break
    
    if prime:    
        print("The number is prime.")
    else:
        print("The number is not prime.")