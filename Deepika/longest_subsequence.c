#include<stdio.h>
int main()
{
    int array[]={10,15,2,1,3,5,8,9};          
    int count=0;                    
    
    int len=sizeof(array)/sizeof(array[0]);        //size of the array
   
    for(int index=0; index<len; index++)           // find longest subsequence length of the array
    {
        if(array[index]<array[index+1])           
        count++;                                   // above condition is true it will count
        break;
    }
    printf("%d",count);
}
