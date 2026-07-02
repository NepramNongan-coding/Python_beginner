# to find the median of a list

def mlf(list = [1,23,5,68,85,45,19]):    # if you want to add other elements,add them in list
    list1 = sorted (list)
    print("sorted list:",list1)
    n = len(list1)
    
    if n % 2 == 0:    
        h = int((n+1)/2)
        list2 = list1[h]
        return list2
    else:
        h = int(n/2)
        list2 = list1[h]
        return list2

print("The median of the list is",mlf())

# def mls(list = [1,23,5,68,85,45]):
#     list1 = sorted (list)
#     n = len(list1)
#     h = int((n+1)/2)
#     k = int((n+2)/2)
#     l = int((h+k)/2)
#     list2 = list1[l]
#     return list2

# print("The median of the list is",mls())