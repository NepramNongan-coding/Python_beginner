#accept two integers and display their sum,difference,product,quotient and remainder
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

sum = a+b
print("The sum is",sum)

if a>b:
    dif = a-b
    print("The difference is",dif)
else:
    dif = b-a
    print("The difference is",dif)

prd = a*b
print("The product is",prd)

if a>b:
    quo = a//b
    print("The quotient is",quo)
    rem = a%b
    print("The remember is",rem)
else:
    quo = b//a
    print("The quotient is",quo)
    rem = b%a
    print("The remember is",rem)