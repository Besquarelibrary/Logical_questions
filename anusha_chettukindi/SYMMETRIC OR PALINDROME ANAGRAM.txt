LOGIC TO PRINT IF SYMMETRIC OR PALINDROME ANAGRAM
LOGIC-1:----------PYTHON------------

s="anutsanu"
n=len(s)//2
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
count=0
for i in dict:
    if(dict[i]%2!=0):
        count=count+1
if s[:n:]==s[n:len(s):]:
    print("symmetric")
elif (count<=1):
        print("anagram palindrome")
else:
    print("not a palindrone and not a symmetric")

OUTPUT:
not a palindrone and not a symmetric


LOGIC-2:
s="sossos"
n=len(s)//2
if s[:n:]==s[n:len(s):] and s[:n:]==s[-1:-n-1:-1]:
    print("it is symmetric as well as palindrome")
elif s[:n:]==s[n:len(s):]:
    print("symmetric")
elif s[:n:]==s[-1:-n-1:-1]:
    print("palindrome")
else:
    print("not a palindrone and not a symmetric")

OUTPUT:
it is symmetric as well as palindrome