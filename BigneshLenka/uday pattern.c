#include <stdio.h>

int main() {
    int rows = 5;  // Number of rows in the pattern
    int i, j;

    for (i = 0; i < rows; i++) {
        // Print spaces before the asterisks
        for (j = 0; j < i; j++) {
            printf(" ");
        }

        // Print the asterisks
        for (j = i; j < rows; j++) {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}

