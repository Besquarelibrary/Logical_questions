#include <stdio.h>
#include <stdlib.h>

int main() {
    int num, last_digit, prev_digit, diff;
    printf("enter number:");
    scanf("%d",&num);
    prev_digit = num % 10; 
    num /= 10; 
    
    while (num > 0) {
        last_digit = num % 10; 
        diff = abs(last_digit - prev_digit); 
        if (diff != 1) {
            printf("%d is not a jumping number\n"); 
            return 0;
        }
        prev_digit = last_digit; 
        num /= 10; 
    }
    
    printf("%d jumping number\n");
    
    return 0;
}

