num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))
num3=int(input("Enter your last number:"))
if num1>num2 and num2>num3:
    print("num1 is larger.")
elif num2>num1 and num2>num3:
    print("num2 is larger.")
else:
    print("num3 is larger.")