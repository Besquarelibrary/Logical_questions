#include <stdio.h>
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

void generateCombinations(int arr[], int data[], int start, int end, int index, int r) {
    int i;
    if (index == r) {
        // Calculate minimum, maximum, and difference between them
        int min = data[0];
        int max = data[r - 1];
        int diff = max - min;
        
        // Print the combination
        for (i = 0; i < r; i++) {
            printf("%d ", data[i]);
        }
        printf("\n");
        
        // Print length, maximum, and minimum values
        printf("length = %d max = %d min = %d \n", end + 1, max, min);
        
        // Check if the combination meets the desired condition
        if (end + 1 == diff + r) {
            printf("This is the combination we are searching for.\n");
        } else {
            printf("This is not the combination we are searching for.\n");
        }
        
        return;
    }
    
    // Generate combinations recursively
    for (i = start; i <= end && end - i + 1 >= r - index; i++) {
        data[index] = arr[i];
        generateCombinations(arr, data, i + 1, end, index + 1, r);
    }
}

void printCombinations(int arr[], int n, int r) {
    // Create an array to store the combinations
    int data[r];
    
    // Call the helper function to generate combinations
    generateCombinations(arr, data, 0, n - 1, 0, r);
}


int main() {
    int arr[] = {1, 6, 3, 2, 8, 0, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int r = 3, i = 0;
    
    printf("n = %d\n", n);
    
    // Sorting the array in ascending order
    quick(arr, 0, n - 1);
    
    // Printing the sorted array
    for ( i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    // Generating combinations and checking conditions
    printCombinations(arr, n, r);

    return 0;
}

