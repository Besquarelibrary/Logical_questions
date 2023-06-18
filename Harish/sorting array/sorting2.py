l=[1,6,7,4,0,3,4,6,8,5]
l1=[]

while l:
    minimum=l[0]
    for i in l:
        if i<minimum:
            minimum=i
    l1=l1+[minimum]
    l.remove(minimum)
print(l1)
