3. sorting of 0,1,2 in the list using while condition in time complexity?
l=[0,0,1,2,1,1,2,0]
low=0
mid=0
high=len(l)-1
while mid<=high:
#    (l[0]==1,0==1) false, if it true then mid value will increase 
    if l[mid]==1:
        mid+=1
#   (l[0]==1,0==0) true, if it true, swap low=mid,mid=low then mid and low value will increase  
    elif l[mid]==0:
        l[low],l[mid]=l[mid],l[low]
        low+=1
        mid+=1
#    (l[6]==1,2==0) two conditions fail,then swap high=mid,mid=high then high value will decrease 
    else:
        l[high],l[mid]=l[mid],l[high]
        high-=1
print(l)
output: [0, 0, 0, 1, 1, 1, 2, 2]
----------------------           ----------------------              ---------------------------                      -----------------------------

l=[0,0,1,2,1,1,2,0]
# in sorted we need to asign new variable
y=sorted(l)
print(y)
output: [0, 0, 0, 1, 1, 1, 2, 2]
----------------             ------------------           -----------------               --------------------

l=[0,0,1,2,1,1,2,0]
# in sort it will update same list
l.sort()
print(l)
output: [0, 0, 0, 1, 1, 1, 2, 2]	
#using bubble sort 
l = [1, 2, 0, 1, 2, 0, 1,0,2]

# Bubble sort algorithm
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

# Print the sorted list
print(l)
output: [0, 0, 0, 1, 1, 1, 2, 2]

