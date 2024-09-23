l = []
n = int(input("enter no of ele:"))
print("enter ele:")
for i in range(n):
    e =int(input())
    l.append(e)
a = int(input("enter ele to be removed:"))
l.remove(a)
print(l)
