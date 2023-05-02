x = "vvvviiijjjjaaaayy nuthhhhaaahhlllaaipppattiiiiiiii"
d= {}
for i in x:
    if (ord(i)) %2 == 0:
        if x.count(i)>1 and x.count(i)%2 ==0:
            d[i] = x.count(i)
# print(d)
for j in d:
    if d[j] ==max(d.values()):
        print(chr(ord(j) + 4))
        
    else:
        print(j,"Not Allowed")
