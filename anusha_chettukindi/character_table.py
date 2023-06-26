
-------------------------------------------------------------------------------
QUESTION:PROGRAM TO PRINT THE CHARACTER TABLE

LOGIC IN PYTHON
PROGRAM

#read the string input from user
s=input("enter string")
#to print upto length of the string
p=len(s)//2
table_val=int(input("enter table number which you want to print"))
#initialize i=1 because table multiple starts with 1
i=1
#loop will run until i value greater the half of the length of input string
while(i<=p):
    #table result
    val=table_val*i
    #value should less than the length of the string
    if(val<len(s)):
        #character shouldn't be a space or symbol
        if(s[val]!='' and (97<=ord(s[val])<=122 or 65<=ord(s[val])<=90)):
            #to print the character table
            print(table_val,"*",i,"=",s[val])
            i=i+1
        else:
            i+=1
    else:
        break

OUTPUT:
enter stringf*f o&l l o*w y*o u r h6e+a r&t
enter table number which you want to print2
2 * 1 = f
2 * 2 = o
2 * 3 = l
2 * 4 = l
2 * 5 = o
2 * 6 = w
2 * 7 = y
2 * 8 = o
2 * 9 = u
2 * 10 = r
2 * 11 = h
2 * 12 = e
2 * 13 = a
2 * 14 = r
2 * 15 = t
> 
---------------------------------------------------------------------------------
