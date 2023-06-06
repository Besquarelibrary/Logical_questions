PROGRAM TO FIND THE EQUILIBRIUM ELEMENTS IN THE ARRAY
l=[1,2,1,0,3]
sum1=l[0]
for i in range(1,len(l)):
    sum2=0
    for j in range(i+1,len(l)):
        sum2=sum2+l[j]
    if(sum1==sum2):
            print(l[i],"at",i,"index","is equlibrium")
    sum1=sum1+l[i]
    
OUTPUT:
1 at 2 index is equlibrium