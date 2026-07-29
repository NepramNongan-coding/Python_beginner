
while True:
    print("Choose one of the following \n1.Factorial\n2.Sum of first n Natural numbers\n3.Multiplication table of a number\n4.Exit.")
    n = input()
    if n == "1":
        num = int(input("Enter a number:"))
        fact = 1
        if num < 0:
            print("Sorry,factorial of a negative number is not exist.")
        elif num == 0:
            print("The factorial of 0 is 1.")
        else:
            for i in range (1,num+1):
                fact = fact * i
            print("The factorial of",num,"is",fact)

    elif n == "2":
        num = int(input("Enter a number:"))
        if num < 0:
            print("Please enter a natural number.")
        else:
            sum = (num*(num+1))/2
            print("The sum of first",num,"natural number is",sum)

    elif n == "3":
        num = int(input("Enter a number:"))
        x = 1
        while x<11:
            print(num,"x",x,"=",x*num)
            x+=1

    elif n == "4":
        break

    else:
        print("Invalid option,choose from 1 to 4.")