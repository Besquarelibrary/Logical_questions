# to find given number is perfect number or not
n= int(input("enter a number"))
sum=0
# the index values of n will store in i
for i in range(1,n):
    if(n%i==0):
# if the above condition is true then the sum value will be added with i
        sum=sum+i
# if sum equals to n
        if(sum==n):
            print(n,"is a perfect number")
        else:
            print(n,"is not a perfect number")



