#include <stdio.h>         // Include the standard input/output library
#include <string.h>        // Include the string manipulation library

int isSymmetric(char[], int);      // Function prototype for checking symmetry
int isPalindrome(char[], int);     // Function prototype for checking palindrome

int isPalindrome(char str[], int len)    // Function definition for checking palindrome
{
  for (int i = 0; i < len-1; i++)        // Loop through the characters of the string
  {
    if (str[i] != str[len - i - 1])      // Check if characters from both ends are not equal
    {
      return 0;                          // Return 0, indicating it's not a palindrome
    }
  }
  return 1;                              // Return 1, indicating it's a palindrome
}

int isSymmetric(char str[], int len)      // Function definition for checking symmetry
{
  int mid = 0;                            // Variable to store the mid-point of the string
  if (len % 2 == 0) {
    mid = len / 2;                        // Calculate mid-point for even length
  } else {
    mid = len / 2 + 1;                    // Calculate mid-point for odd length
  }
  for (int i = 0; i < mid; i++)           // Loop through the first half of the string
  {
    if (str[i] != str[mid+i])             // Check if characters from the beginning and middle are not equal
    {
      return 0;                           // Return 0, indicating it's not symmetric
    }
  }
  return 1;                               // Return 1, indicating it's symmetric
}

int main()                                // Main function
{
  char str[200];                          // Declare a character array to store the string
  printf("Enter any string :\n");         // Display a prompt to enter a string
  gets(str);                              // Read the string from the user
  
  int len = strlen(str);                  // Get the length of the string

  int isPalindromeFlag = isPalindrome(str, len);     // Check if the string is a palindrome
  int isSymmetricFlag = isSymmetric(str, len);       // Check if the string is symmetric

  if (isPalindromeFlag == 1 && isSymmetricFlag == 1) {       //Condition Check
    printf("Given string is symmetric and palindrome\n");    // Print the result if it's symmetric and palindrome
  } else if (isPalindromeFlag == 0 && isSymmetricFlag == 1) {
    printf("Given string is symmetric\n");                   // Print the result if it's symmetric only
  } else if (isPalindromeFlag == 1 && isSymmetricFlag == 0) {
    printf("Given string is palindrome\n");                  // Print the result if it's palindrome only
  } else {
    printf("Given string is neither symmetric nor palindrome\n");  // Print the result if it's neither symmetric nor palindrome
  }

  return 0;                                // Return 0 to indicate successful execution
}
