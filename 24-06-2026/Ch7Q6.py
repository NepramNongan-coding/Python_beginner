def swap(num1,num2):
    if num1<num2:
        return num2,num1
    else:
        return num1,num2

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number which will be greater from the first number:"))

a,b = swap(num1,num2)

print("The first number is",a)
print("The second number is",b)