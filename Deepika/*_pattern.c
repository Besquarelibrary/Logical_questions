#include<stdio.h>

int main() {
    int i, j;
    int size = 5;
    
    for(i = 1; i <= size; i++) {
        // Loop to print '*' based on the value of 'i'
        for(j = 0; j <= i; j++) {
            if(i > j) {
                printf("* "); // Print '*' if i > j
            }
        }
        printf("\n"); // Move to the next line after each row is printed
    }
    
    return 0;
}
