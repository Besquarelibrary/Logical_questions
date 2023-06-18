# check given string is symmetric or not and also split string and reverse second half string and check palindrome or not
x="oanoan"
x=list(x)
a=[]
b=[]
# check string symmetric or not
if len(x)%2==0:
#     spliting string first half
    for i in range(0,len(x)//2):
        a.append(x[i])
    print(a)
    for k in range(len(x)//2,len(x)):
        b.append(x[k])
        z=b[::-1]
    print(z)
    print("yes symmetric")
# comparing two list 
    if a==z:
        print("yes palindrome")
    else:
        print("not palindrome")

else:
    print("not symmetric")
