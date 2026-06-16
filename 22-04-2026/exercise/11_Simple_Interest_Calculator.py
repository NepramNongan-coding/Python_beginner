P=float(input("Enter the principal:"))
R=float(input("Enter the rate of interest (in %) : "))
T=float(input("Enter the time in years:"))
SI=(P*R*T)/100
print("The simple interest is Rs.", SI)
AP=P+SI
print("The amount payable is Rs.", AP)