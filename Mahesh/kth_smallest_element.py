# Find the kth smallest element in the given array?
arr=[1,3,6,7,8,3,2,4,5,2,3,7]
k=int(input("enter an element:"))
# removing all duplicate values in array
set_arr=set(arr)
updated_arr=[]
# converting set into list 
for i in set_arr:
    updated_arr.append(i)
print(updated_arr)
# checking the kth element is lessthen the length of array
if k<=len(updated_arr):
    # itrating loop to find the kth element
    for i in range(0,len(updated_arr)):
        # checking the condition when i value is equal to k
        if i==k:
            # index start from 0 so -1 is used 
            print(updated_arr[i-1])
