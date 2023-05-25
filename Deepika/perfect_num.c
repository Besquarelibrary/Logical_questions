#include <stdio.h>

int main() {
    int n = 28;                                   //input
    int i, add= 0;                               //initialization
    for (i = 1; i < n; i++) {                   //checking divisors for input number
        if (n % i == 0) {
            add += i;                           //if any divisor found add
        }
    }
    if (add == n) {                             // check sum of the divisors is equal to the input
        printf("Perfect number: %d\n", n);
    } else {
        printf("Not a perfect number\n");
    }
    return 0;
}

