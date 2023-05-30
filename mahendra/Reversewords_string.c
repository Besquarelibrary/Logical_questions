#include<stdio.h>         // Include the standard input/output library
#include<string.h>        // Include the string manipulation library
#include<stdlib.h>        // Include the standard library

int main() {             // Main function
    char str[100];       // Declare a character array to store the string
    int i, len;          // Declare variables for loop and string length
    printf("Enter a string:\n");  // Display a prompt to enter a string
    gets(str);          // Read the string from the user
  
    len = strlen(str);  // Get the length of the string

    printf("Reverse string order:\n");  // Display a message for reverse string order

    for(i = len - 1; i >= 0; i--) {     // Loop through the string in reverse order
        if(str[i] == ' ' || i == 0) {   // Check if a space is encountered or it's the first word
            int j;                     // Declare a variable for inner loop
            if(i == 0)                  // Check if it's the first word
                j = i;                  // Set j to i
            else
                j = i + 1;              // Set j to i + 1 to skip the space

            while(str[j] != '\0' && str[j] != 32) // Loop through the characters of the word
            {
                printf("%c", str[j]);  // Print each character of the word
                j++;                   // Increment j to move to the next character
            }

            if (i > 0)                 // Check if there are more words left to print
                printf(" ");           // Print a space after each word
        }
    }

    return 0;                        // Return 0 to indicate successful execution
}
