#include <stdio.h>

//to reverse a substring 
void reverseSubstringing(char string[], int start, int end) {
    while (start < end) {
        char temp = string[start];
        string[start] = string[end];
        string[end] = temp;
        start++;
        end--;
    }
}

//to reverse a words in a string
void reverseWords(char string[]) {
    int length = 0;
    for(int i=0; string[i]!='\0'; i++)
        length++;
    int start = 0, end = 0;

    // Reverse the entire stringing
    reverseSubstringing(string, 0, length - 1);
    //while loop to reverse words
    while (end < length) 
    {
        if (string[end] == ' ') 
        {
            // Reverse the word
            reverseSubstringing(string, start, end - 1);
            start = end + 1;
        }
        end++;
    }

    // Reverse the last word
    reverseSubstringing(string, start, end - 1);
}

int main() {
    char string[] = "ajay bingi ";

    printf("Original stringing: %s\n", string);

    reverseWords(string);    //functiionn  call to reverse a words in a string

    //after reversing we are printing the string
    printf("Reversed words: %s\n", string);

    return 0;
}
