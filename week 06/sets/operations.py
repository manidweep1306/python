t1 = {0,1,2,3,3,5,6,77,7,7}
t2 = {4,5,6,7}
print(t1|t2)
print(t1&t2)
print(t1-t2)
print(t1^t2)
print(2 in t1)
print(0 in t2)
'''
output:
{0, 1, 2, 3, 4, 5, 6, 7, 77}
{5, 6, 7}
{0, 1, 2, 3, 77}
{0, 1, 2, 3, 4, 77}
True
False
'''
