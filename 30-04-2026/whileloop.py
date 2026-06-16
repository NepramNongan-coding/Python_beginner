entry=0
sum1=0
print("Enter the numbers to find their sum,negative numbers stop the loop.")
while True:
    entry=int(input())
    if entry<0:
        break
    sum1+=entry
print("sum=", sum1)