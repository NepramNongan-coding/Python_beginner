p1 = 0
p2 = 0

for i in range(0,5):
    in_val = int(input("Enter 1 for player1 and 2 for player2:"))
    if in_val == 1:
        p1+=1
    elif in_val == 2:
        p2+=1
    else:
        print("Wrong input")
        continue

if p1 == 3:
    print("Player1 wins,then player1 will eat the cake")
else:
    print("Player2 wins,then player2 will eat the cake")