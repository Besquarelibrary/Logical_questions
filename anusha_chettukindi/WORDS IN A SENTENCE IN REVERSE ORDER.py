LOGIC TO PRINT THE WORDS IN A SENTENCE IN REVERSE ORDER
LOGIC-1:-------------------PYTHON___________________---
s="anusha chettukindi is here"
s1=s.split()
l=''.join([s1[i]+" " for i in range(-1,-4,-1)])
print(l)

LOGIC-2
s="anusha chettukindi is here"
s1=""
l=[]
for i in s:
    if i==' ':
        l=l+[s1]
        s1=""
    s1=s1+i
l=l+[s1]
result=''.join([l[i]+" " for i in range(-1,-len(l)-1,-1)])
print(result)
OUTPUT:
here  is  chettukindi anusha
----------------------------------------------------------------------------------------------------------
--------------------------------
