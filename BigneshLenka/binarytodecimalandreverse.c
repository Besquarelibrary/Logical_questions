#include <stdio.h>

#define INT_SIZE sizeof(int) * 8

// Function to calculate the power of a base raised to an exponent
double power(double base, int exponent) {
    double result = 1.0;
    int i;

    if (exponent >= 0) {
        for (i = 0; i < exponent; i++) {
            result = result * base;
        }
    } else {
        for (i = 0; i > exponent; i--) {
            result = result / base;
        }
    }

    return result;
}

// Function to convert a binary array to decimal
double binaryToDecimal(int arr[], int length) {
    double decimal = 0.0;
    int i;

    // Iterate over each element of the binary array
    // and calculate the decimal value
    for (i = 0; i < length; i++) {
        if (arr[i] == 1) {
            decimal = decimal + power(2, length - i - 1);
        }
    }

    return decimal;
}

int main() {
    int bin[INT_SIZE];
    double result;
    int number = 160, index, i;
    index = INT_SIZE - 1;

    // Convert decimal number to binary representation
    while (index >= 0) {
        bin[index] = number & 1;  // Extract the least significant bit
        index--;
        number = number >> 1;  // Right shift number by 1
    }

    printf("Converted binary: ");
    for (i = 0; i < INT_SIZE; i++) {
        printf("%d", bin[i]);
    }
    printf("\n");

    // Convert binary to decimal and print the value
    result = binaryToDecimal(bin, INT_SIZE);
    printf("Value = %.2lf\n", result);

    // Reverse the binary representation
    for (i = 0; i < INT_SIZE / 2; i++) {
        bin[i] = bin[i] + bin[INT_SIZE - i - 1];  // Swap values using addition
        bin[INT_SIZE - i - 1] = bin[i] - bin[INT_SIZE - i - 1];  // Swap values using subtraction
        bin[i] = bin[i] - bin[INT_SIZE - i - 1];  // Swap values using subtraction
    }

    printf("Reversed binary: ");
    for (i = 0; i < INT_SIZE; i++) {
        printf("%d", bin[i]);
    }
    printf("\n");

    // Convert reversed binary to decimal and print the value
    result = binaryToDecimal(bin, INT_SIZE);
    printf("Value = %.2lf\n", result);

    return 0;
}

