# print given string in phone keyboard patten of integers?
string=input("enter a string:")
# After removing all special char in string store in update-string
Update_string=""
# check alphabets according to ascii values and store in update_string
for char in string:
    # Check char ascii value with in range store in update_string
    if ord(char)>=65 and ord(char)<=90:
        Update_string+=char
    # check char ascii value with in range store in update_string
    elif ord(char)>=93 and ord(char)<=122:
        Update_string+=char
print(Update_string)
# Assing all char according to keyboard patten
dict={'a':2,'b':22,'c':222,'d':3,'e':33,'f':333,'g':4,'h':44,'i':444,'j':5,'k':55,'l':555,'m':6,'n':66,'o':666,'p':7,'q':77,'r':777,'s':7777,'t':8,'u':88,'v':888,'w':9,'x':99,'y':999,'z':9999,'A':2,'B':22,'C':222,'D':3,'E':33,'F':333,'G':4,'H':44,'I':444,'J':5,'K':55,'L':555,'M':6,'N':66,'O':666,'P':7,'Q':77,'R':777,'S':7777,'T':8,'U':88,'V':888,'W':9,'X':99,'Y':999,'Z':9999}
# Empty_string to store the values of all char of given string
Empty_string=""
# To itirate the update_string using for loop
for i in Update_string:
    # check if character present in dict or not 
    if i in dict:
        # concating values in Empty_string
        Empty_string+=str(dict[i])
print(Empty_string)

output:
    enter a string:$#Mahesh123#Rajaboina.
    MaheshRajaboina
    62443377774477725222666444662
