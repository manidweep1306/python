t1 = (0,1,2,3,3,5,6,77,7,7)
t2 = (4,5,6,7)
for i in t1:
	print(i)
print(t1.index(2))
print(t1.count(7))
t3 = t1
print(t3)
t4  = tuple(zip(t1,t2))
print(t4)
''' 0
1
2
3
3
5
6
77
7
7
#2
#2
#(0, 1, 2, 3, 3, 5, 6, 77, 7, 7)
#((0, 4), (1, 5), (2, 6), (3, 7))
'''
