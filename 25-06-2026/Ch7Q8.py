import random
Q1 = "The largest fresh water lake in north-east India is-"
Q2 = "The most powerful weapon in India is-"
Q3 = "The 5th U-15 Sub Junior Boys & Girls National Boxing Championship 2026 is held in-"
Q4 = "The newest large cosmic structure named by Dr.Ronaldo Laishram is-"
Q5 = "The most famous writer in Manipur is-"

mark = 0

for i in range(5):
    rand = random.randint(1,5)
    if rand == 1:
        print(Q1)
        Ans = input()
        if Ans.lower() == "loktak lake" or "loktak":
            mark+=1
    elif rand == 2:
        print(Q2)
        Ans = input()
        if Ans.lower() == "agni 5" or "agni V":
            mark+=1
    elif rand == 3:
        print(Q3)
        Ans = input()
        if Ans.lower() == "punjab" or "jalandar":
            mark+=1
    elif rand == 4:
        print(Q4)
        Ans = input()
        if Ans.lower() == "loktak protocluster":
            mark+=1
    elif rand == 5:
        print(Q5)
        Ans = input()
        if Ans.lower() == "anganghal" or "hijam anganghal" or "kabi anganghal":
            mark+=1

def score(mark):
    return mark

def remark(mark):
    if mark == 5:
        print("Outstanding.")
    elif mark == 4:
        print("Excellent.")
    elif mark == 3:
        print("Good.")
    elif mark == 2:
        print("Read more to score more.")
    elif mark == 1:
        print("Needs to take interest.")
    else:
        print("General knowledge will always help you. Take it seriously.")

Total = score(mark)
print("The total mark is",Total)
remark(Total)