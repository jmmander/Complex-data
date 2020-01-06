lister = [1,2,3,4,5,67,8,9,0,1,23,2,31,321,31,3,1]

def findkth(list, k):
    list.sort()
    print(list)
    return list[k]

print(findkth(lister, 10))