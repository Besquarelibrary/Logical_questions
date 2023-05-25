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
