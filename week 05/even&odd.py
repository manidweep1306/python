l = []
e = []
o = []
n = int(input("enter no of ele:"))
print("enter ele:")
for i in range(n):
    a =int(input())
    l.append(a)
for j in l:
    if(j%2==0):
        e.append(j)
    else:
        o.append(j)
print("even:") 
print(e)
print("odd:")
print(o)
