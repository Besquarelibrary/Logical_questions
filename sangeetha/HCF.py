# To find Highest Common Factor of  a given numbers
n = int(input("enter a number"))
m = int(input("enter a number"))
l1=[]
l2=[]
# To find the range of given number
for i in range(1,n+1):
    if n%i==0:
# if the above condition is true then the value will be stored in l1
        l1.append(i)
print(l1)
for j in range(1,m+1):
    if m%j==0:
    # if the above condition is true then the value will be stored in l2
        l2.append(j)
print(l2)
l3=l1+l2
maxval=l3[0]
for x in range(1,len(l3))
    # if the value of x is greater than maxval
    if l3[x]>maxval:
        maxval = l3[x]
        # if the maxval presented in l1 and l2
        if maxval in l1 and maxval in l2:
            print(maxval)
