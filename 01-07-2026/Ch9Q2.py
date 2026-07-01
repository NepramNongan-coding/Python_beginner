list = [1,2,3,4,5,-1,-2,-3,-4,-5]
list1 = []
list2 = []

for element in list:
    if element>0:
        list1.append(element)
    else:
        list2.append(element)

print("The first list is",list)
print("The list of the positive integers is",list1)
print("The list of the negative is",list2)