#include <stdio.h>

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotate_array(int arr[], int n, int k) {
    k = k % n;
    reverse(arr, 0, n - 1);
    reverse(arr, 0, k - 1);
    reverse(arr, k, n - 1);
}

int main() {
    int size;
    printf("enter the size of an rray: ");
    scanf("%d", &size);
    int arr[size];
    printf("enter %d elements in an array: ",size);
    for(int i=0; i<size; i++)
    scanf("%d",&arr[i]);
    int n = sizeof(arr) / sizeof(arr[0]);
    int k;
    printf("enter no of times you wanted to rotate the array: ");
    scanf("%d", &k);
    
    rotate_array(arr, n, k);
    
    printf("Rotated array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    return 0;
}