#include<stdio.h>
int partition (int a[], int start, int end)  
{  
    int pivot = a[end];   
    int i = (start - 1),j,t;  
  
    for(j = start; j <= end - 1; j++)  
    {  
          
        if (a[j] < pivot)  
        { 
			i++;   

             t = a[i];  
            a[i] = a[j];  
            a[j] = t; 
 
        }  
    }  

    t = a[i+1];  
    a[i+1] = a[end];  
    a[end] = t; 
    return (i + 1);  
}  
  
  
void quick(int a[], int start, int end) 
{  
    if (start < end)  
    {  
        int p = partition(a, start, end); 
        quick(a, start, p - 1);  
        quick(a, p + 1, end);  
    }  
}  
  

void printArr(int a[], int n)  
{  
    int i;  
    for (i = 0; i < n; i++)  
        printf("%d ", a[i]);  
}  
int main(){
	int arr[]={8,9,7,5,6,3,2,6,0,7,11};
	int n=sizeof(arr)/sizeof(int),k=2;
	while(k>n)
	{
		scanf("%d",&n);
	}
	printArr(arr, n);
	quick(arr,0,n-1);
	printf("\nAfter sorting array elements are - \n");    
    printArr(arr, n);
    printf("\n");
    printf("The kth  smallest element is %d ",arr[k-1]);
    return 0;
}
