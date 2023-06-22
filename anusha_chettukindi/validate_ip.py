QUESTION:
PROGRAM TO CHECK WHETHER THE IP ADDRESS ENTERED BY THE USER IS VALID OR NOT

PROGRAM:
#function declaration to makesure user input should contain either digits or "."
def validate_ip(ip):
    #initialize count
    count=0
    #we break the condition whenever count is zero 
    while(count<1):
        #iterate ip
        for char in ip:
            #stores boolean value
            bool_val=(48<=ord(char)<=57) or (ord(char)==46)
            #if not true count will be incremented
            if not bool_val:
                print("invalid ip you should enter ip with digits or (.) only")
                count=count+1
                break
        #when count>0 means that entered ip is invalid
        if(count!=0):
            #read the ip from user untill he enters correct one
            ip=input("enter ip")
            #initialize count to zero
            count=0
        else:
            #when count zero so thats the valid ip
            return ip
            break
#store ip return by the func       
string=validate_ip(input("enter ip"))
#initialize the count
count=0
#initialize empty string to store the digits upto "."
new_string=""
#iterate loop
for char in string:
    #store the string items in s1 untill we find "."
    if(char!="."):
        new_string=new_string+char
    else:
        #convert that string to integer and check the range
        string_integer=int(new_string)
        if(0<=string_integer<=255):
            count=count+1
             #then initialize s1 to empty to store the string after "."
            new_string=""
    
#for last string characters
if(0<=int(new_string)<=255):
    count=count+1
#since ip have four parts seperated with "."
if(count==4):
    print("Its a valid ip")
else:
    print("Its a invalid ip")

OUTPUT:
enter ip255.0.0.0
Its a valid ip
> OUTPUT:
enter ip234&.9
invalid ip you should enter ip with digits or (.) only
enter ip234.*
invalid ip you should enter ip with digits or (.) only
enter ip255.0.0.2
Its a valid ip
>-------------------------------------------------------------------------------------------------------

