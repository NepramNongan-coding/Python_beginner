name = input("Enter your name:") 
print("Hello,",name,"!")

age = int(input("Enter your age:"))
print("Your age is",age)

if age < 18:
    print("Your age is not eligible for license",name)
else:
    print("You are eligible for a license",name)