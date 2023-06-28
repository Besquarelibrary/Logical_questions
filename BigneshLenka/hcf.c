#include <stdio.h>
#include <stdlib.h>

int *arraycompare(int *arr, int *arr1, int number, int number1) { // fucntion defination of arraycompare
    int i, k = 0;
    int *ptr = malloc(number * sizeof(int));  // Allocate memory for the result array

    for (i = 0; i < number; i++) { // loop for copying the values to ptr
        if (arr[i] == arr1[i]) { //condition for copying
            ptr[k] = arr[i];
            k++;
        }
    }

    return ptr; //returning ptr
}

int main() {
    int number = 10, number1 = 15, k = 0, l = 0;
    int arr[number - 1], arr1[number1 - 1], *arr2;
    int i;

    for (i = 1; i <= number; i++) { //loop for finding the divisibles 
        if (number % i == 0) { //condition for finding the divisibles
            arr[k] = i;
            printf("%d is in arr\n", arr[k]);
            k++;
        }
    }

    for (i = 1; i <= number1; i++) { //loop for finding the divisibles
        if (number1 % i == 0) { //condition for finding the divisibles
            arr1[l] = i;
            printf("%d is in arr1\n", arr1[l]);
            l++;
        }
    }

    arr2 = arraycompare(arr, arr1, number, number1); //calling the arraycompare function

    for (i = 0; arr2[i]!='\0'; i++) { // loop for printing the array
        printf("%d is in arr2\n", arr2[i]);
    }

    free(arr2);  // Free the dynamically allocated memory

    return 0;
}

