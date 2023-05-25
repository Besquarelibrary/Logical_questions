#include<stdio.h>
int partition (int a[], int start, int end)  //partion funtion defination
{  
    int pivot = a[end];   
    int i = (start - 1),j,t;  
  
    for(j = start; j <= end - 1; j++) // Looping for end-1 from start 
    {  
          
        if (a[j] < pivot)  //condition for swapping
        { 
			i++;   

             t = a[i];  
            a[i] = a[j];  
            a[j] = t; 
 
        }  
    }  
    /*swapping*/
    t = a[i+1];  
    a[i+1] = a[end];  
    a[end] = t; 
    return (i + 1);  //returning i+1 to quick funtion
}  
  
  
void quick(int a[], int start, int end) //quick sort function defination
{  
    if (start < end)  
    {  
        int p = partition(a, start, end); // calling partition function 
        quick(a, start, p - 1);  //recursive call
        quick(a, p + 1, end);  //recursive call 
    }  
}  
  

void printArr(int a[], int n)  //print function defination
{  
    int i;  
    for (i = 0; i < n; i++)  //looping for accessing the array elements
        printf("%d ", a[i]);  
}  
int main(){
	int arr[]={8,9,7,5,6,3,2,6,0,7,11};
	int n=sizeof(arr)/sizeof(int),k=2;
	printArr(arr, n);//printing array elements before sorting
	quick(arr,0,n-1);//calling quick function for sorting
	printf("\nAfter sorting array elements are - \n");    
    printArr(arr, n);//printing array elements after sorting
    printf("\n");//printing a new line
    printf("The kth  smallest element is %d ",arr[k-1]);//printing the kth smallest element in an array
    return 0;
}
