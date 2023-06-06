#include<stdio.h>
void swap(int* a, int* b) { //swap function defination for swaping the array elements
    int temp = *a; 
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) { //partition function call 
    int pivot = arr[high];
    int i = (low - 1),j;
    
    for ( j = low; j <= high - 1; j++) { //looping till high -1 from low 
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]); //calling swap function
        }
    }
    swap(&arr[i + 1], &arr[high]); //calling swap function
    return (i + 1);
}

void sort(int arr[], int low, int high) { //funtion defination for sort 
    if (low < high) {
        int pi = partition(arr, low, high); //calling partition funtion 
        sort(arr, low, pi - 1); //recursive call 
        sort(arr, pi + 1, high); //recursive call
    }
}
int main()
{
	int i=0,r=0,n=0,q=0;
	int a[]={1,2,3,5,4,50,60,9,20,21,44},b[50],c[50];
	n=sizeof(a)/sizeof(int); // To find the length of array
	sort(a,0,n-1); //calling sort function
	for ( i = 0; i < n; i++) { //looping to array elements
        printf("%d ", a[i]);
    }
    printf("\n");
    for ( i = 0; i < n; i++) { //looping for checking the array elements 
    	if(a[i]<10){ //condition for jumping numbers having value less than 10 
		
        if (a[i]-a[i+1]==1||a[i]-a[i+1]==-1) // condition for jumping number
        {
        	printf("%d is a jumping number\n",a[i]);
		}}
		else //condition for jumping numbers having value greater than and less than 99
		{
			r=a[i]%10; //reminder
			q=a[i]/10; //quoficient
			if(r-q==1||r-q==-1) //condition for jumping numbers
			{
				printf("%d is a jumping number\n",a[i]); //print statement for jumping number
			}
			else
			{
				printf("%d is not jumping number\n",a[i]); //print statement for number that is not a jumping number	
			}
		}

}
	return 0;
}
