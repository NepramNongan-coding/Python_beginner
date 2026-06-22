def gender():
    if gen == "Male" or gen == "male" or gen == "m" or gen == "M":
        print("Mr.", name)
    elif gen =="Female" or gen =="female" or gen =="f" or gen =="F" :
        print("Mrs.", name)
    else:
        print("Please concern a doctor.")
gen = str(input("Enter your gender:"))
name = str(input("Enter your name:"))

gender()