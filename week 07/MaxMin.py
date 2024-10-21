def maxMin(l):
    return max(l),min(l)
n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in 1st list: ')
for i in range(n):
    l.append(input())
print(maxMin(l))
