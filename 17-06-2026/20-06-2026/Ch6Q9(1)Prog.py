#to print a pattern
#num=3
#for i in range (1,num +1):
#    if i==1:
#         stars1 = "      *       "
#    elif i==2:
#         stars2 = "    * * *    "
#    elif i==3:
#        stars3="*"*5
#        print(stars1)
#        print(stars2)
#   print(stars3)

n = 3
for i in range(1,n+1) :
    for j in range(2*(n-i)):
        print(" ",end="")
    for k in range(2*i-1):
        if k==(2*i-2):
            print("*", end="")
        else:
            print("* ", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(2*(n-i)):
        print(" ",end="")
    for k in range(2*i-1):
        if k==(2*i-2):
            print("*", end="")
        else:
            print("* ", end="")
    print()