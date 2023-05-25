Find the most frequently repeated character in a string check whether count is even and also the max count contained character also even then increment the value of the character to the 4 and print the character
s="BBADDDDAAAAFFFFFF"
def maxi():
    max=1
    for i,j in dict.items():
        if max<j:
            max=j
            max_chr=i
    return max,max_chr
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
while(True):
    v=maxi()
    if v[0]%2==0 and ord(v[1])%2==0:
        c=ord(v[1])+4
        d=chr(c)
        print(v[0],d)
        break
    else:
        del dict[v[1]]
OUTPUT:
6 J