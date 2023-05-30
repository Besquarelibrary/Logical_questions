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
int main()
{	int arr[]={0,2,1,0,1,2,0,1,2,0,2,1},size;
	size = sizeof(arr)/sizeof(int);	
	printArr(arr,size-1);//calling printarray function
	printf("\n");
	quick(arr,0,size-1); // calling quick sort function
	printArr(arr,size-1); //calling printarray function
	return 0;
}
