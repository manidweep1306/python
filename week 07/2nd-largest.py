def max(l):
    l.sort()
    print("the 2nd largest element in ",l,"is",l[-2])
n = int(input('Enter the no. of elements: '))
l = []
print('Enter the content in 1st list: ')
for i in range(n):
    l.append(input())
l=list(set(l))
max(l)
