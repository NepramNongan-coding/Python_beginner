def removeElement(list = [1,2,3,4,5,6,7,8,9]):
    n = int(input("Enter the element you want to remove:"))
    list1 = list.remove(n)
    print("The element you want to remove is",n)
    return list

print("The modified list is",removeElement())