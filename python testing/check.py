#program to determine whether an integer is divisible by both 3 and 5,only by 3,only by 5,or neither using if - elif = else
n = int(input("Enter the number:"))
if n%3==0 and n%5==0:
    print("The number is divisible by both 3 and 5.")
elif n%3==0:
    print("Tne number is divisible by 3 but not by 5.")
elif n%5==0:
    print("The number is divisible by 5 but not by 3.")
else:
    print("The number is divisible by neither 3 nor 5.")