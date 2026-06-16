result=0
val1=float(input("Enter the value 1:"))
val2=float(input("Enter the value 2:"))
op=input("Enter your operator given in bracket(+,-,*,/)")
if op=="+":
    result=val1+val2
elif op=="-":
    if val1>val2:
        result=val1-val2
    else:
        result=val2-val1
elif op=="*":
    result=val1*val2
elif op=="/":
    if val2 == 0:
        print("Error! Division by zero is not allowed. Program terminated")
    else:
        result = val1/val2
else:
    print("Wrong input,program terminated")
print("The result is ",result)