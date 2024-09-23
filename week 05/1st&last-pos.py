l = []
e = []
o = []
n = int(input("enter no of ele:"))
print("enter ele:")
for i in range(n):
    a =int(input())
    l.append(a)
print(l.index(min(l)))
print(l.index(max(l)))
