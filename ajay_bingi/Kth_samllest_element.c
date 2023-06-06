/*In an arrayay of elements, find the K value's smallest element  */

#include <stdio.h>
void find_Kth_smallest_element(int,int [],int); //function declaration
int main() 
{
    int size,i,arrayay_length=0,k;
    printf("enter arrayay size to be: ");
    scanf("%d",&size);   //user input
    int arrayay[size]; //  arrayay declaration
    printf("enter %d arrayay elements: ",size);
    //this for loop is for entering input elements 
    for(i=0; i<size; i++)
    scanf("%d",&arrayay[i]);  //user input
   
    printf("enter key value: ");
    scanf("%d",&k); //user input
    
    //checking the K value is less than length of arrayay
    if(k<size)
    find_Kth_smallest_element(k,arrayay,size); // function call to find smallest elemement
    else
    printf("Invalid \n K is greater than arrayay length\n");
    return 0;
}


// function defination
void find_Kth_smallest_element(int k,int arrayay[],int arrayay_length)
{
    int i,first_smallest=100,second_smallest=100; //statically assigning the 1st & 2nd smallest variables with 100
    
    //this for loop is for sortinng the elements
    for(i=0; i<arrayay_length; i++)
    {
        for(int j=i+1; j<arrayay_length; j++)
        {
            //comparing  & swapping, previous and next element's
            if(arrayay[i]>arrayay[j])
            {
            int temporary=arrayay[i];
            arrayay[i]=arrayay[j];
            arrayay[j]=temporary;
            }
        }
    }
    printf("%dth smallest element in arrayay is %d\n",k,arrayay[k-1]);
    
}