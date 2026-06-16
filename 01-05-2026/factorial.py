num=int(input("Enter a number to find its factorial value: " ))
fact=1
for i in range(1,num+1):
    fact *= i
    
print(fact)