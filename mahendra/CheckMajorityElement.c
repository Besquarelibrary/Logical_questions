#include <stdio.h>

int main() {
    int arr[] = {1, 2, 1, 1, 1, 4, 2, 5, 3, 1, 2, 1, 1};
    int len = sizeof(arr) / sizeof(arr[0]);
    int i, j, count, found = 0;
 // Iterate over the array elements
    for (i = 0; i < len; i++) {
        // Check if the element is not marked as visited
        if (arr[i] != '*') {
            count = 1; // Initialize count to 1 for the current element

            // Iterate over the remaining elements
            for (j = i + 1; j < len; j++) {
                // If a matching element is found, increment count and mark it as visited
                if (arr[i] == arr[j])// check if current element is repeated
		{
                    count++;// increment count
                    arr[j] = '*'; // Mark the element as visited
                }
            }

            // Check if the count exceeds len/2
            if (count > len / 2) {
                printf("%d occurs more than len/2 times in the array.\n", arr[i]);
                found = 1;
            }
        }
    }

    // If no element occurs more than len/2 times, print a message
    if (!found) {
        printf("No element occurs more than len/2 times in the array.\n");
    }

    return 0;
}

