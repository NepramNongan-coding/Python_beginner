
def removedupli(list1):
    newlist = []
    for element in list1:
        if element not in newlist:
            newlist.append(element)
    return newlist


list1 = [2,4,5,7,9,1,2,4,2,3]

list = removedupli(list1)

print("The old list is",list1)
print("The new list is",list)