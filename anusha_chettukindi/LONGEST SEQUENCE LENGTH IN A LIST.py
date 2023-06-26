QUESTION: WRITE A PROGRAM TO PRINT THE LENGTH OF LONGEST SEQUENCE IN THE LIST

CODE IN PYTHON:

#list initialization
l=[1,2,3,2,3,4,5,6,3,4,22,66,99,890,2]
#To store the max sequence count
max=0
#to store the count of the squence
count=1
#looping to traverse a list
for i in range(len(l)-1):
    #comparing element with next element
    if(l[i]<l[i+1]):
        #increment the count when the condition is true
        count=count+1
    #when condition is false
    else:
        #to store the max count
        if(max<count):
            max=count
            count=1
#this is for when the initial if condition is false
if(max<count):
    max=count
print("longest sequence length",max)

OUTPUT:
longest sequence length 6

-----------------------------------------------------------------------------------
