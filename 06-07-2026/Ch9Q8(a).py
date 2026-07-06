def popElement(list = [1,2,3,4,5,6,7,8,9]):
    n = int(input("Enter the position of the element which you want to remove:"))
    list1 = list.pop(n)
    print("The element you want to remove is",list1)
    return list

print("The modified list is",popElement())