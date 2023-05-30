QUESTION:PROGRAM TO PRINT THE CHARACTERS IN THE RESULTANT TABLE FROM THE GIVEN STRING
CODE:
    
#to read the string input from user
s=input("enter the string")
#create the empty string
s1=""
#to read integer value from the user
table_val=int(input("which table you are going to print"))
#iterate the string
for j in s:
    #need to create another string to store only alphabates 
    if j!=' ' and (65<=ord(j)<=90 or 97<=ord(j)<=122):
        s1=s1+j
n=len(s1)
i=1
while(i<=10):
    a=2*i
    #if that table result is greater than the length of the string then we have to break the loop because there is nothing to print
    if(a>n):
        break
    #to print the output in the table format
    print(table_val,"*",i,"=",s1[a])
    i+=1

OUTPUT:
enter the stringabu% ghj&v **b anu
which table you are going to print2
2 * 1 = u
2 * 2 = h
2 * 3 = v
2 * 4 = a
2 * 5 = u
-------------------------------------------------------------------------------
