#include<stdio.h>
int main()
{
    int array1[]={0,3,5,9,6}, array2[]={2,7,1,8,4}; 
    int length1=length2=0,i,j,m,k,a,b;
    //to find legnth of array's
    for(i=0; array1[i]!='\0'; i++)
        length1++;
    for(i=0; array2[i]!='\0'; i++)
        length2++;
    int temporary[length1+length2];
    //assigning array1 elements to temporary array
    for(i=0; i<length1; i++)
    {
        temporary[i]=array1[i];
    }
    //assigning array2 elements to temporary array
    for(j=0; j<length2; j++,i++)
    {
        temporary[i]=array2[j];
    }
    int length3=0;
    //to find legnth of array
    for(i=0; temporary[i]!='\0'; i++)
        length3++;

    //swapping elements using bubble_sort 
    for(k=0; k<length3; k++)
    {
        for(m=k+1; m<length3; m++)
        {
            if(temporary[k]>temporary[m])
            {
            int temporary_variable=temporary[m];
            temporary[m]=temporary[k];
            temporary[k]=temporary_variable;
            }
        }
    }

    //assigning the temporary array elements to array1 & array2 and printing them
    for(a=0; a<length1; a++)
    {
        array1[a]=temporary[a];
        printf("%d ",array1[a]);
    }
    printf("\n");
    for(b=0; b<length2; b++,a++)
    {
        array2[b]=temporary[a];
         printf("%d ",array2[b]);
    }
    printf("\n");
}