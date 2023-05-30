PROGRAM TO FIND THE LEADERS IN A LIST
l=[9,3,1,7,5,6]
max=l[0]
i=0
while(i<len(l)):
    for j in range(i+1,len(l)):
        if(max<l[j]):
            max=l[j]
            max_index=j
    if(max==l[i]):
        max_index=i
        print(max,"is placed at index",max_index)
        if(max_index==len(l)-1):
            break
        max=l[max_index+1]
        i=max_index+1 
    else:
        print(max,"is placed at index",max_index)
        if(max_index==len(l)-1):
            break
        max=l[max_index+1]
        i=max_index+1
        
        
        
OUTPUT:
9 is placed at index 1
7 is placed at index 4
5 is placed at index 5