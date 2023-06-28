#include<stdio.h>
int main()
{
    int array[]={2,4,6,7,10,5,3,1,8},i,j;
    /*to find array length*/
    int length = *(&array + 1) - array ;
     for (i = 0; i < length - 1; i++) 
    {
        for (j = 0; j < length - i - 1; j++) 
        {
            if (array[j] > array[j + 1]) 
            {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
    int min = array[0];
    int max = array[length-1];
    int k=0;
    for(int i=min; i<=max; i++)
    {
        if(i != array[k])
        {
            printf("missing number is: %d\n",i);
            break;
        }
        k++;
    }
}