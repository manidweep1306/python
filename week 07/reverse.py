def list(l):
    n = len(l)
    for i in range(n//2):
        l[i],l[n-i-1] = l[n-i-1],l[i]
    return l
print(list([1,2,3,4]))
