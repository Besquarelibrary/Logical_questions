# given arrays sort and store in lenth of arrays 
l1=[1,2,4,3,6]
l2=[6,7,5,4,8,9,6]
# find lenth of array assign variables as zero
c=0
l=0
len=0
# for 1st array length 
for i in l1:
    c=c+1
print(c)
# second array length
for i in l2:
    l=l+1
print(l)
# adding two arrays
l3=l1+l2
print(l3)
# l3 length 
for i in l3:
    len+=1
print(len)
l4=[]
l5=[]
# for sorting of array we use this loops
for i in range(0,len):
    for j in range(0,len):
        # checking index 0 with total list if condition is true enter into if statement
        if l3[i]<l3[j]:
            # swaping of elements using index
            l3[i],l3[j]=l3[j],l3[i]
print(l3)
# spliting array according to length of array
for i in range(0,c):
    l4+=[l3[i]]
print(l4)
# spliting array according to length of array
for j in range(c,len):
    l5+=[l3[j]]
print(l5)

output:5
7
[1, 2, 4, 3, 6, 6, 7, 5, 4, 8, 9, 6]
12
[1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9]
[1, 2, 3, 4, 4]
[5, 6, 6, 6, 7, 8, 9]
