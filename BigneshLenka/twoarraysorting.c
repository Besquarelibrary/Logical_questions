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
{
	int arr1[]={5,2,3};
	int arr2[]={2,6,8,3,9,7,5},m,n,o;
	int arr[20],i,j=0;
	m=sizeof(arr1)/sizeof(int); //to find length of array1
	n=sizeof(arr2)/sizeof(int); //to find length of array2
	for(i=0;i<m;i++) //loop for copying array1
	{
		arr[j]=arr1[i];
		j++;
	}
	for(i=0;i<n;i++) //loop for copying array2
	{
		arr[j]=arr2[i];
		j++;
	}
	o=m+n;
	printArr(arr,o);//calling printarray function
	printf("\n");
	quick(arr,0,o); // calling quick sort function
	printArr(arr,o); //calling printarray function
	printf("\n");
	j=0;
	for(i=0;i<m;i++) //loop for copying sorted array
	{
		arr1[i]=arr[j];
		j++;
	}
	for(i=0;i<n;i++) //loop for copying sorted array
	{
		arr2[i]=arr[j];
		j++;
	}
	printArr(arr1,m);//calling printarray function
	printf("\n");
	printArr(arr2,n); //calling printarray function
	return 0;
}

