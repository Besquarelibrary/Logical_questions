//stdio.h library provides functions for input and output operations
//string.h library provides functions and macros for working with strings like “strlen”
#include <stdio.h> 
#include <string.h>
#include <stdlib.h> 

//The function printKeypadSequence() is defined, which takes a pointer to a character array (string) as input.
void printKeypadSequence(char *input) {

     //calculate string length 
     //Iterate over each character in the input string
     //initialise 'count' variable for count the number of time digit need to print
    int length = strlen(input);
    for (int i = 0; i < length; i++) {
        int count = 0;

	 // Check if the current character is between 'a' and 'c'
         //Calculate the count based on the position of the character in the range 'a' to 'c'
         //in this for loop print “2” upto count num
       if (input[i] >= 'a' && input[i] <= 'c')
	 {
            count = input[i] - 'a' + 1;
	    for (int j = 0; j < count; j++) 
		{
                	printf("2");
            	}
        }
	 // Check if the current character is between 'd' and 'f'
         //Calculate the count based on the position of the character in the range 'd' to 'f'
         //in this for loop print “3” upto count num
        else if (input[i] >= 'd' && input[i] <= 'f')
	 {
            count = input[i] - 'd' + 1;
            for (int j = 0; j < count; j++) {
                printf("3");
            }
        }
         // Check if the current character is between 'g' and 'i'
         //Calculate the count based on the position of the character in the range 'g' to 'i'
         //in this for loop print “4” upto count num
        else if (input[i] >= 'g' && input[i] <= 'i') 
        {
            count = input[i] - 'g' + 1;
            for (int j = 0; j < count; j++) 
            {
                printf("4");
            }
        }
         // Check if the current character is between 'j' and 'l'
         //Calculate the count based on the position of the character in the range 'j' to 'l'
         //in this for loop print “5” upto count num
        else if (input[i] >= 'j' && input[i] <= 'l') {
            count = input[i] - 'j' + 1;
            for (int j = 0; j < count; j++) {
                printf("5");
            }
        }
         //Check if the current character is between 'm' and 'o'
         //Calculate the count based on the position of the character in the range 'd' to 'f'
         //in this for loop print “6” upto count num
        else if (input[i] >= 'm' && input[i] <= 'o') {
            count = input[i] - 'm' + 1;
            for (int j = 0; j < count; j++) {
                printf("6");
            }
        }
         //Check if the current character is between 'p' and 's'
         //Calculate the count based on the position of the character in the range 'p' to 's'
         //in this for loop print “7” upto count num
        else if (input[i] >= 'p' && input[i] <= 's') 
        {
            count = input[i] - 'p' + 1;
            for (int j = 0; j < count; j++) 
            {
                printf("7");
            }
        }
         // Check if the current character is between 't' and 'v'
         //Calculate the count based on the position of the character in the range 't' to 'v'
         //in this for loop print “8” upto count num
        else if (input[i] >= 't' && input[i] <= 'v') 
        {
            count = input[i] - 't' + 1;
            for (int j = 0; j < count; j++) 
            {
                printf("8");
            }
        }
         // Check if the current character is between 'w' and 'z'
         //Calculate the count based on the position of the character in the range 'w' to 'z'
         //in this for loop print “9” upto count num
        else if (input[i] >= 'w' && input[i] <= 'z') 
        {
            count = input[i] - 'w' + 1;
            for (int j = 0; j < count; j++) 
            {
                printf("9");
            }
        }
        // Check if the current character is ' '/space 
        //print '0'
        else if (input[i] == ' ')
        {
            printf("0");
        }
    }
}

int main() {
    char input[100];

    printf("Enter the input string: ");
    //scanf("%s", input);//Read the input string from user only one word
   gets(input);// Read the input string from the user multiple words

    printf("Output: ");

    // Call the function printKeypadSequence() with the input string as an argument
    printKeypadSequence(input);

    return 0;
}

