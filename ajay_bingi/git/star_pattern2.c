#include <stdio.h>

int main() {
    int rows, i, j;

    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    // Upper half of the pattern
    for (i = 1; i <= rows; i++) {
        for (j = 1; j <= i; j++) 
        {
            printf("* ");
        }
        printf("\n");
    }

    // Lower half of the pattern
    for (i = rows - 1; i >= 1; i--) {
        for (j = 1; j <= i; j++) 
        {
            printf("* ");
        }
        printf("\n");
    }

    return 0;
}
