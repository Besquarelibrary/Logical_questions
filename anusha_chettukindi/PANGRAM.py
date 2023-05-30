
-----------------------------------------------------------------------------
PANGRAM:
------------
EVERY ALPHABET SHOULD PRESENT IN THE SENTENCE IF NOT PRINT THAT ALPHABET
------------------------------------------------------------------------------
l1=[]
a=65
while(a >= 65 and a <= 90):
    b=chr(a)
    l1=l1+[b]
    a=a+1;
count=0
freq={}
x="bjjjhb hjbjn j"
for i in x:
    if i!=' ':
	if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
g=''.join(list(freq.keys()))
l=[]
for i in l1:
    if i in g.upper():
        count=count+1
    else:
        l=l+[i]
if count==len(l1):
    print("its pangram")
else:
    print(l)

-------------------------------------------------------------------------
DIFFERENT LOGICS FOR EVEN
LOGIC1:
if num&1==0
if num//2*2==num
if
-------------------------------------------------------
        

        