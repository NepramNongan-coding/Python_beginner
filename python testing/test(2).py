def mult(n,x):
    while n < 11:
        print(x,"x",n,"=",x*n)
        n+=1

x = int(input("Enter the number which you want to display its multiplication table:"))
n = 1

x = mult(n,x)
print(x)

# x = int(input("Enter a number:"))
# n = 1
# while n < 11:
#     print(x,"x",n,"=",x*n)
#     n+=1