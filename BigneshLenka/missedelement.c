#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 8, 7, 9, 4, 2, 1, 0}; 
    int n = sizeof(arr) / sizeof(int);
    int TOTAL_NUMBER = 26;
    int count[TOTAL_NUMBER] ;
    int i;

    for (i = 0; i < n; i++) { // loop for assign values to count array
        count[arr[i]]++;
    }

    for (i = 0; i < TOTAL_NUMBER; i++) { //looping to find thee missing element
        if (count[i] == 0) { // condition for missed elemnt 
            printf("%d is missing.\n", i);
        }
    }

    return 0;
}

