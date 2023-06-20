PROGRAM TO PRINT THE MAXIMUM STOLEN VALUE FROM THE HOUSES BY THIEF HE CAN'T ABLE TO STOLE THE ADJACENT HOUSES MONEY

CODE IN PYTHON:
-----------------------------------------------------------
#initialize the loop
l=[1,2,1,6,4,5]
#initialize the max_profit as zero 
max_profit=0
#loop through the list
for i in range(0,len(l)-2):
    #to store starting home value in the sum
    sum=l[i]
    #loop through list as any of the adjacent element not be taken
    for j in range(i+2,len(l)+1):
        #for the last element in the list
        if(j==len(l)-1):
            #add the last value to sum
            sum=sum+l[j]
            #break the loop when j reaches to end of the list
            break
        #this is to when the alternate element is less than the element which placed beside of that to store the maximum element value to sum
        elif(l[j]<l[j+1]):
            #move to next element
            j=j+1
        #when the alternate index value is greater than or equal to adjacent value 
        else:
            #the alternate value only added to the sum
            sum=sum+l[j]
            #to skip one element to satify no adjacency rule
            j=j+2
    #to store maximum sum value
    if max_profit<sum:
        max_profit=sum
        #to store next choosen path sum
        sum=0
    #move to next path
    sum=0
#to print final sum value
print("maximum stolen value is :",max_profit)

OUTPUT:
maximum stolen value is : 13

-------------------------------------------------------------------