PRINT ALL THE ELEMENTS WHETHER PRIME OR ARMSTRONG WITH ALL THE ELEMENTS COMBINATIONS IN THE LIST
--------------------------
l=[1,3,7,21]
def prime(s):
    if s>=1:
        for j in range(2,s//2+1):
            if s % j == 0:
                return "not prime"
                break
        else:
            return "prime"
    else:
        return "its a negtive number"
def armstrong(s):
    temp=s
    p=str(s)
    sum=0
    while(temp!=0):
        r=temp%10
        sum=sum+pow(r,len(p))
        temp=temp//10
    if(sum==s):
        return "is armstrong "
    else:
        return "not armstrong"

for i in range(len(l)):
    count=0
    for j in range(i+1,len(l)):
        if(count==0):
            s=str(l[i])
            s=int(s)
            print(s,prime(s))
            print(s,armstrong(s))
            count=count+1
        s=str(l[i])+str(l[j])
        s=int(s)
        print(s,prime(s))
        print(s,armstrong(s))
OUTPUT:
----
1 prime
1 is armstrong 
13 prime
13 not armstrong
17 prime
17 not armstrong
121 not prime
121 not armstrong
3 prime
3 is armstrong 
37 prime
37 not armstrong
321 not prime
321 not armstrong
7 prime
7 is armstrong 
721 not prime
721 not armstrong

OTHER WAY-----------
---------------
l=[1,3,7,21]
def prime(s):
    if s>=1:
        for j in range(2,s//2+1):
            if s % j == 0:
                break
        else:
            return 1
    else:
        return 0
def armstrong(s):
    temp=s
    p=str(s)
    sum=0
    while(temp!=0):
        r=temp%10
        sum=sum+pow(r,len(p))
        temp=temp//10
    if(sum==s):
        return 1
    else:
        return 0
def result_check():
    if(result1==result2):
        print(s,"its armstrong as well prime")
    elif(result1):
        print(s,"prime")
    elif(result2):
        print(s,"armstrong")
    else:
        pass

for i in range(len(l)):
    count=0
    for j in range(i+1,len(l)):
        if(count==0):
            s=str(l[i])
            s=int(s)
            result1=prime(s)
            result2=armstrong(s)
            count=count+1
            result_check()
        s=str(l[i])+str(l[j])
        s=int(s)
        result1=prime(s)
        result2=armstrong(s)
        result_check()
OUTPUT:
1 its armstrong as well prime
13 prime
17 prime
3 its armstrong as well prime
37 prime
7 its armstrong as well prime
> 
------------------------------------------------------------

        