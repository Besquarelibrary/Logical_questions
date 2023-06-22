SORT THE ELEMENTS IN THE TWO LISTS BY TAKING THE ELEMENTS FROM THE BOTH THE LISTS
--------------------------
l1=[1,4,0,8]
l2=[3,5,2,9,6]
l3=l1+l2
for i in range(0,len(l3)):
    for j in range(i+1,len(l3)):
        if(l3[i]>l3[j]):
            l3[i],l3[j]=l3[j],l3[i]
l1=l3[0:len(l1):1]
l2=l3[len(l1)::]
print(l1,l2)

OUTPUT:
[0, 1, 2, 3] [4, 5, 6, 8, 9]
-----------------------------------------------------------------------------------
LOGIC -2
l1=[6,3,2,1,0,4]
i = 0
while i < len(l1)-1:
    if l1[i] > l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
        if(i>0):
            i=i-1
    else:
        i += 1
            
print(l1)
OUTPUT:
[0, 1, 2, 3, 4, 6]