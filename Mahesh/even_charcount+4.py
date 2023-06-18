# print given string most repeated count of char and check count of value is even and
# if it is even take max value of char in even count and 
# check askey value is even then print position of char+4 th position char?
x="beesquare aaahhee"
d={}
for i in x:
#     checking askey value is even or odd
    if ord(i)%2==0:
#         count should be >1 and count should be even
        if x.count(i)>1 and x.count(i)%2==0:
#         store in d variable in key:values
            d[i]=x.count(i)
print(d)
for i in d:
#     calling with key of value and checking values is equal or not with max value
    if d[i]==max(d.values()):
#         printing order of char with addition of 4
        print(chr(ord(i)+4))

output: {'h': 2}
