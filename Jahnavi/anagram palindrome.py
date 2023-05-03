x='Jahnavi'
d1={}
for i in x:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)
c=0;
for i in d1.values():
    if i%2==1:
        c=c+1
if c<=1:
    print("True")
else:
    print("False")