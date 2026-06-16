P=int(input("Enter the principle:"))
R=int(input("Enter the rate:"))
T=int(input("Enter time in years:"))
SI=(P*R*T)/100
A=SI+P
print("The simple interest is", SI)
print("The amount payable is", A)