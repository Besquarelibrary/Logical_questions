# Given 2 lists should be combined sorted and output list should be sort way with the length
list1=[1,3,5,2,6,7]
list2=[4,9,8,0,1]
# adding 2 lists
list3=list1+list2
# 2 loops
for i in range(len(list3)):
    for j in range(len(list3)):
# if length of list3[i] less than or equal to length of list3[j]
        if list3[i]<=list3[j]:
# swaping the elements
            list3[i],list3[j]=list3[j],list3[i]
# slice the elements of list3 according to the length of list1
list1=list3[0:len(list1)]
# slice the elements of list3 according to the length ok list2
list2=list3[len(list1):]
print(list1)
print(list2)
