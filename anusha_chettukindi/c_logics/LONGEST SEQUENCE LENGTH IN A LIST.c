QUESTION: WRITE A PROGRAM TO PRINT THE LENGTH OF LONGEST SEQUENCE IN THE LIST

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