# Program that prints minimum and maximum of five numbers entered by the user
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number:"))
e = int(input("Enter the fifth number: "))
print("The minimum number is: ", min(a,b,c,d,e))
print("The maximum number is: ", max(a,b,c,d,e))
"""

count = 1
while count < 6:
    print("Enter number ", count)
    user_input = int(input())
    
    if count == 1:
        a = user_input
    elif count == 2:
        b = user_input
    elif count == 3:
        c = user_input
    elif count == 4:
        d = user_input
    elif count == 5:
        e = user_input
        
    count += 1

print("The minimum number is: ", min(a,b,c,d,e))
print("The maximum number is: ", max(a,b,c,d,e))