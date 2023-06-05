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




# print given string in reverse words not char.
# done in python using in built functions
x="python is very easy"
z=x.split(" ")
y=z[::-1]
str(y)





# print given string in reverse words not char.
x="python is very easy"
z=[]
tmp=''
for i in x:
#     comparing where i == space then save untill sapce and store in z
    if i==" ":
        z.append(tmp)
        tmp=''
    else:
        tmp=tmp+i
    print(tmp)
if tmp:
    z.append(tmp)
print(z)
# reversing the string
y=z[::-1]
print(y)
# converting into string from list using join function
a=" ".join(y)
a






# check whether the given string is pangram or not, if not then print the missing char?
x="The quick brown fox jumps over the lazy dog"
# another variable contains of all a to z char.
y="qwertyuiopasdfghjklxvbnmcz"
# converting string into lower case or upper case.
x=x.lower()
# converting string into set for unique char.
x=set(x)
# converting set into list for comparing
a=list(x)
# sorting for alphabet order for easy compair.
a.sort()
# remove space between words or char
a.remove(" ")
b=list(y)
b.sort()
print(a)
print(b)
d=[]
# comparing two list to check equal or not.
if a==b:
    print("yes pangram")

else:
    for i in b:
#         comparing if i not in a then add to d list
        if i not in a:
#         if conditions is true then save to d empty list
            d.append(i)
#     print d list
    print("not pangram",d)

