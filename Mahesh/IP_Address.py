# check whether given IP address is correct or not?
# Taking input from user
x=input("enter an IP address:")
# Empty string to store "." from input and split by using "."
Empty_string=""
# Empty list to store values after split of IP address
Empty_list=[]
# loop used for spliting the string and saving into list 
for i in x:
    # checking the condition if "i" is equal to '.'
    if i==".":
        # Adding Empty_string to Empty_list by using append function
        Empty_list.append(Empty_string)
        # After appending into Empty-list we are making Empty_string Empty to store another value untill "." comes
        Empty_string=""
        # When If condition is false it will enter into else block
    else:
        # In Empty-string it will store values untill if condition becomes true
        Empty_string=Empty_string+i
# In the last itration which was stored in Empty_string appending to Empty_list
Empty_list.append(Empty_string)
print(Empty_list)
# To store length of list assing length variable
length=0
# To store the count of list which is >0 and <=255
count=0
# To check Empty_list is in the range of 0 to 255 or not
for i in Empty_list:
    length+=1
    # Checking item in list is in given range or not
    if int(i)>=0 and int(i)<=255:
        # if condition is true then count will increase 
        count+=1
# Checking that count value and length value is equal or not 
if count==length:
    print("perfect IP address")
else:
    print("Wrong IP address")



output:
    enter an IP address:24.34.123.234
    ['24', '34', '123', '234']
    perfect IP address
