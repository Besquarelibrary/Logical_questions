#include <stdio.h>

//for sorting the array elements 
void sort(int arr[],int r, int length)
{
   
    for(int i=0; i<r; i++)
    {
        for(int j=i; j<r; j++)
        {
            if(arr[i]>arr[j])
            {
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    int difference = arr[0] - arr[r-1]; //finding difference btwn 1st and last elements
    if(difference<0)
        difference=-difference;
    if(difference + r == length) //comparing diff + pickcount & array length
    {
        for(int i=0; i<r; i++)
        {
            printf("%d ",arr[i]);
        }
        printf("\n");
    }
}

//printfCombinations fucntiion body
void printCombination(int arr[], int data[], int start, int end, int index, int r,int length) 
{
    // If current combination is ready to be printed, print it
    if (index == r) 
    {
        sort(data,r,length);  //function call to sort an array    
    }

    // replace index with all possible elements. The condition "end - i + 1 >= r - index" makes sure that
    // including one element at index will make a combination with remaining elements at remaining positions
    for (int i = start; i <= end && end - i + 1 >= r - index; i++) 
    {
        data[index] = arr[i];
        printCombination(arr, data, i + 1, end, index + 1, r,length);//recursively calling printCombination function 
    }
}


//generateCombinations function body
void generateCombinations(int arr[], int n, int r) 
{
    int data[r];
    printCombination(arr, data, 0, n - 1, 0, r,n); //printCombination function call
}

int main() 
{
    //int arr[] = {1,7,9,2,3,4,8};
    int arr[] = {1,2,3,4,5};
    int n = sizeof(arr) / sizeof(arr[0]);
    int r = 3;

    generateCombinations(arr, n, r); //generateCombinations function call

    return 0;
}
