#to check if the year entered by the user is leap year or not
y = int(input("Enter the year:"))

if y%4 == 0:
    print("The entered year is a leap year.")
else:
    print("The entered year is not a leap year.")