def CompoundInterest():
    P = float(input("Enter the Principal Amount:"))
    R = float(input("Enter the Rate:"))
    N = float(input("Enter the number of times the interest is compounded:"))
    T = float(input("Enter the Time:"))
    A = P*(1+(R/N))**(N*T)
    CI = A - P
    print(f"The compound interest of the given data is ${CI:.2f}" )

CompoundInterest()