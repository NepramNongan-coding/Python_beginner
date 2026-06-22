#to find the sum of digits of an integer number input by user
n = int(input("Enter the number:"))
sum = 0
while n > 0:
    digit = n % 10          #last digit pickup
    sum += digit
    n = n//10
print(sum)