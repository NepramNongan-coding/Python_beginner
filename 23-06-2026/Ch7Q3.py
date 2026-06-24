def qdteqt():
    a = int(input("Enter the coefficient of x^2:"))
    b = int(input("Enter the coefficient of x:"))
    c = int(input("Enter the coefficient of x^0:"))
    det = (b**2)-(4*a*c)
    
    if det == 0:
        print("The determinant of the quadratic equation is zero i.e. ", det,".")
    elif det > 0:
        print("The determinant of the quadratic equation is positive i.e ", det,".")
    else:
        print("The determinant of the quadratic equation is negative i.e ", det,".")
    
qdteqt()