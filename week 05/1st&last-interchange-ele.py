l = []
n = int(input("enter no of ele:"))
for i in range(n):
    e =int(input())
    l.append(e)
l[-1],l[0] = l[0],l[-1]
print(l)
