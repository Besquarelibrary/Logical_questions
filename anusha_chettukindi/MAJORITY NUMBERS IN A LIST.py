PROGRAM TO PRINT THE MAJORITY NUMBERS IN A LIST

DESCRIPTION: A number is said to be major when that frequency of that number should greater than the len(list)//2

PROGRAM:

#create the list
l=[1,1,1,1,2,2]
#To store the half the value of length of list
mid=len(l)//2
# creating dictionary for storing the element as key and that frequency as value
dict={}
for i in l:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
max=0
#this is to find the max frequency element in the dictionary
for i,j in dict.items():
    if j>max:
        index=i
        max=j
#checking the condition that maximum is greater the mid or not
if(max>mid):
    print(index,"is majority number")
else:
    print("there is no major number in the given list")

OUTPUT:
{1: 4, 2: 2}
1 is majority number