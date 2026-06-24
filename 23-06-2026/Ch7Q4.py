from random import randint

sed_number=int(input("Enter your ticket number: "))


rand_num = randint(1,600)
if sed_number==rand_num:
    print("You won the lucky draw.")
else:
    print("Your ticket number is not lucky number. The correct ticket number is", rand_num)
