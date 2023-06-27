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
print(a)
