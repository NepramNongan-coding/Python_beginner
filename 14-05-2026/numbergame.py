# from random import randint
# guessed_number=int(input("Enter a number which you want: "))
# if guessed_number==randint(1,10):
#     print("You won the game.")
# else:
#     print("Your number is incorrect,please try again.")


# from random import randint

# rand_num = randint(1,10)
# guessed_number=int(input("Enter a number which you want: "))

# if guessed_number==rand_num:
#     print("You won the game.")
# else:
#     print("Your number is incorrect. The correct number is", rand_num , "\nPlease try again.")

from random import randint

while True:
    rand_num = randint(1,5)
    guessed_number=int(input("Enter a number which you want: "))
    if guessed_number==rand_num:
        print("You won the game.")
        break
    else:
        print("Your number is incorrect. The correct number is", rand_num , "\nPlease try again.")