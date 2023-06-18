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

LOGIC IN C:

#include <stdio.h>

int main() {
    //initialize array
    int a[]={1,3,4,5,6,7,2,3,4,5,6,7,8,9};
    //for finding the length of an array
    int size=sizeof(a)/sizeof(a[0]);
    //initialize max as 0 for storing the max sequence length
    int max=0;
    //initialize count as 1 for storing the sequence length
    int count=1;
    //iterate an array
    for(int i=0;i<size-1;i++){
        //condition to check the every element should less than next ele
        if(a[i]<a[i+1]){
            //increment the count upto condition satifies
            count=count+1;
        }
        else{
            //for storing the max sequence
            if(max<count){
                max=count;
                count=1;
            }
        }
    }
    //for the last elements which doesn't match with initial if condi
    if(max<count){
        max=count;
    }
    printf("longest sequence length is:%d",max);
}

OUTPUT:

longest sequence length is:8