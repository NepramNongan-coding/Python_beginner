# to find the sum of 1 + 1/8 + 1/27 + ...+ 1/(n^3)
n = int(input("Enter the number:"))
count = 1
sum = 0

while count <= n:
    num = 1/(count**3) 
    sum = sum + num
    count += 1

print(sum)