/*The number  which is most repeated and that repeaatation should be grater than the half_lenght 
of the given array is treated as a MAJORITY NUMBER*/

#include <stdio.h>
int main() 
{
    int array[]={1,1,2,2,2,2,2,2,2,3,4,5,5,6,6};
    int length=0,x=0;
    //finding length of array
    for(int i=0; array[i]!='\0';  i++)
        length++;
        printf("array length %d\n",length);
    int half_length=length/2; // dividing the length of an arrayay
    int temporaryorary[length]; // temporaryorary arrayay 
      for(int i=0; i<length; i++) 
    {
        temporaryorary[array[i]]=0;  //assigning zero's 
    }  
    for(int j=0; j<=length; j++)
    {
        temporaryorary[array[j]]++; //incrementing the values of temporary arrayay
    }
    
    for(int k=0; k<=length; k++)
    {   
        if(temporaryorary[k]>=half_length) //checking the value is greater than or equal to hal_length of arrayay 
        {
            x++;
            printf("%d is the majority one among all elements",k);
        }
    }
    if(x==0)
    printf("no majority number in a given arrayray\n");
    
}