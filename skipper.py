sample = [1,2,3,4,5,6,7,8,9,10]
skipped = sample[0: :2]
print(skipped)

def skip(n, loe):
    newlist = loe[0::n+1]
    return newlist


print(skip(2,sample))
print(skip(0,sample))
print(skip(1,sample))