myList = [22,4,16,38,13]
choice = 0
while True:
    print("The list 'myList' has the following elements", myList)
    print("\nL I S T  O P E R A T I O N S")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to the given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element by its position")
    print("6. Delete an existing element by its value")
    print("7. Sort the list in ascending order")
    print("8. Sort the list in descending order")
    print("9. Display the list")
    print("10. Exit")
    
    choice = input("Enter your favorite choice (1-10): ")
    
    if choice == "1":
        element = int(input("Enter the element you want to append: "))
        myList.append(element)
        print("The",element, "has been appended to the list\n")
        
    elif choice == "2":
        element = int(input("Enter the element you want to insert: "))
        pos = int(input("Enter the position of the element you want to insert (by index): "))
        myList.insert(pos,element)
        print("The",element, "has been inserted in the list")
        
    elif choice == "3":
        myNewList = [124,11,34]
        myList.extend(myNewList)
        print("The",myNewList,"has been extended to the previous list")
        
    elif choice == "4":
        i = int(input("Enter the position of the element to be modified: "))
        # error handling
        if i < len(myList):
            newElement = int(input("Enter the new element: "))
            oldElement = myList[i]
            myList[i] = newElement
            print("The element", oldElement,"has been modified\n")
        else:
            print("Index out of range")
    
    elif choice == "5":
        i = int(input("Enter the position of the element to be deleted: "))
        if i < len(myList):
            element = myList.pop(i)
            print("The element", element,"has been modified\n")
            print("The new list: ", myList)
        else:
            print("Index out of range")
            
    elif choice == "6":
        i = int(input("Enter the element to be deleted: "))
        if i in myList:
            myList.remove(i)
            print("The element", i, "has been deleted")
        else:
            print("Value not found")
        
    elif choice == "7":
        sortedList = myList.sort()
        print("The sorted list is: ", sortedList)
        
    elif choice == "8":
        descSort = myList.sort(reverse=True)
        print('The sorted list is ', descSort)
        
    elif choice == "9":
        print("My list is", myList)
    
    elif choice == "10":
        break
    
    else:
        print("Please select a valid option\nPress any key to continue...")
        ch = input()
