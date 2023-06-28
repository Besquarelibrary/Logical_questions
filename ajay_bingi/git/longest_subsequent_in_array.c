#include<stdio.h>
int main()
{
    int array[]={10,15,2,1,3,5,8}; //statically assigned elements
    int size=0,count=0; //variables
    //to find length of array
    for(int i=0; array[i]!='\0'; i++)
    {
        size++;
    }
    //to find the longest subsequent length
    for(int j=0; j<size; j++)
    {
        if(array[j]<array[j+1])
        count++; //if condition is true it will incerement 
    }
    printf("%d",count);
}