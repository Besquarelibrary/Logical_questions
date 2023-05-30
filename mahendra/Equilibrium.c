#include <stdio.h>// Include the standard input/output library


// Function to find the equilibrium index in the array
int findEquilibrium(int arr[], int n) {
    int i, j, leftSum, rightSum;// Initialization of local variable inside the function 
    
    // Iterate through each element of the array
    for (i = 0; i < n; i++) {
        leftSum = 0;
        rightSum = 0;
        
        // Calculate the sum of elements on the left side of the current index
        for (j = 0; j < i; j++) {
            leftSum += arr[j];
        }
        
        // Calculate the sum of elements on the right side of the current index
        for (j = i + 1; j < n; j++) {
            rightSum += arr[j];
        }
        
        // Check if the left and right sums are equal
        if (leftSum == rightSum) {
            return i; // Return the index as the equilibrium point
        }
    }
    
    return -1; // Return -1 if no equilibrium point is found
}

int main() {
    int arr[] = {1, 4, 6, 4, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    int equilibriumIndex = findEquilibrium(arr, n);

    if (equilibriumIndex == -1) {
        printf("There is no equilibrium point in the array\n");
    } else {
        printf("The equilibrium point is at index %d\n", equilibriumIndex);
    }

    return 0;
}

