#to find the second largest element of the list
def seclarg(list = [1,3,85,39,900,598,869,302]):
    list1 = sorted (list)
    n = len(list1)
    list2 = list1[n-2]
    return list2

print(seclarg())