l=[0,0,1,2,1,1,2,0]
low=0
mid=0
high=len(l)-1
while mid<=high:
    if l[mid]==1:
        mid=mid+1
    elif l[mid]==0:
        l[low],l[mid]=l[mid],l[low]
        low=low+1
        mid=mid+1
    else:
        l[high],l[mid]=l[mid],l[high]
        high=high-1
print(l)

