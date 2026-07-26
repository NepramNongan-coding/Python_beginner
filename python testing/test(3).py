# while count < 6:
#     print("Enter the number ",count)
#     user_input= int(input())
    
#     if count == 1:
#         a = user_input
#     elif count == 2:
#         b = user_input
#     elif count == 3:
#         c = user_input
#     elif count == 4:
#         d = user_input
#     elif count == 5:
#         e = user_input
        
#     count += 1
# count = 1
# print("The minimum number is: ", min(a,b,c,d,e))
# print("The maximum number is: ", max(a,b,c,d,e))

num = int(input("Enter number 1: "))
minimum = maximum = num
for i in range(2, 6):
    num = int(input(f"Enter number {i}: "))
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum number =", minimum)
print("Maximum number =", maximum)