pc = float(input("Enter the percentage:"))
if pc > 90:
    print("The grade with respect to the percentage is A.")
elif pc > 80 and pc <= 90:
    print("The grade with respect to the percentage is B.")
elif pc > 70 and pc <= 80:
    print("The grade with respect to the percentage is C.")
elif pc >= 60 and pc <=70:
    print("The grade with respect to the percentage is D.")
else:
    print("The grade with respect to the percentage is E.")