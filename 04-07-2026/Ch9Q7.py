def insertList(num, idx, list):
    list.insert(idx, num)
    
    return list


list = [12, 2, 567, 89, 22, 56, 88]
num = int(input("Enter the number you want to insert: "))
idx = int(input("Enter the position where you you want to insert the element: "))

print("The original list is: ", list)
newList = insertList(num, idx, list)
print("The new list is: ", newList)
