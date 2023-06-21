#include<stdio.h>
int j,k;   //global variables
int main()
{
    int size1,size2;
    lable:
    printf("Enter the size of array1: ");
    scanf("%d",&size1);
    printf("Enter the size of array2: ");
    scanf("%d",&size2);
    /*if the size1 and size2 is equal then only we are allowing to do operation*/
    if(size1 == size2)
    {
    printf("\n");
    int arr1[size1],arr2[size2];
    printf("Enter %d array1 elements: ",size1);
    for(int i=0; i<size1; i++)    // this loop  is to enter input into array1
        scanf("%d",&arr1[i]);
    printf("Enter %d array2 elements: ",size2);
    for(int i=0; i<size1; i++)   // this loop  is to enter input into array2
        scanf("%d",&arr2[i]);
    
    int length = size1 + size2; //adding size1 and size2
    int arr3[length];
    for(int i=0; i<length; i++)
    {
        /*here we are assining  array1 elements to the even places of array3*/
         if(i%2==0)  
         {
            arr3[i]=arr1[j];
            j++;
         }
        /*here we are assining  array2 elements to the odd places of array3*/ 
         else
         {
            arr3[i]=arr2[k];
            k++;
         }
    }
    /*printing the array3*/
    for(int i=0; i<length; i++)
        printf("%d ",arr3[i]);
    }
    /*if size's dosen't match then we are printing a statement*/
    else
    {
       printf("#invalid size\nplease enter equal size\n");
       goto lable;  //it is type of while loop and when it execute it will directly go to lable where it has been declared and start the exexution again
    }
}