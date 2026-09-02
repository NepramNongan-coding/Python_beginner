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

# def med(list1):
#     list2 = []
#     list2 = sorted(list1)
    
#     print("The sorted list is",list2)
    
#     if n%2 != 0:
#         idx = (n-1)//2
#         val = list2[idx]
#     else:
#         idx1 = (n-1)//2
#         idx2 = idx1 + 1
#         val = (list2[idx1] + list2[idx2]) / 2
    
#     return val

# list1 = []
# n = int(input("Enter the numbers of element you want to input:"))

# for item_no in range(0,n):
#     item = int(input("Enter the element you want to input:"))
#     list1.append(item)

# print("The original list is",list1)
# print("The median of the list is",med(list1))