#include<stdio.h>
int i,odd_sum,even_sum;
/******************using loops***********************/
/* void fun(int arr[],int length)
{
    for(; i<length; i++)
    {
        if(i%2==0)
            even_sum+=arr[i];
        else
            odd_sum+=arr[i];
    }
    printf("odd sum = %d  even sum = %d\n",odd_sum,even_sum);
}  */

/**************using recursion*************/
int fun(int arr[],int i ,int length)
{
    if(i%2==0)
        even_sum+=arr[i];

    else
        odd_sum+=arr[i];

    /*checking if the index is equal to length*/
    if(i+1==length)
    {
        if(odd_sum>even_sum)
            return odd_sum;

        else
            return even_sum;
    }
    fun(arr,i+1,length);
}  
int main()
{
    int arr[]={1,2,3,4,5,6};
    int length=0;
    /*to find array length*/
    int size=*(&arr+1) - arr;
    int value=fun(arr,0,size);
    printf("max value is %d\n",value);
}