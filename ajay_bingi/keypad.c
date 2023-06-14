#include <stdio.h>
#include <string.h>

void printKeypadSequence(char *input) 
{
    int length = strlen(input),i,j;
  
    for (i = 0; i < length; i++) 
    {
        int count = 0;
        if (input[i] == ' ' ) //condition for printing 0
            printf("0");

        if (input[i] >= 'a' && input[i] <= 'c') // condition for printing 2
        { 
            count = input[i] - 'a' + 1;
            for ( j = 0; j < count; j++) //looping for the printing particular number in accordance to the count
                printf("2");
            
        }

        else if (input[i] >= 'd' && input[i] <= 'f')  //condition for printing 3
        {
		count = input[i] - 'd' + 1;
            for ( j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count
                printf("3");
            
        }

        else if (input[i] >= 'g' && input[i] <= 'i')  //condition for printing 4
        {    
            count = input[i] - 'g' + 1;
            for ( j = 0; j < count; j++) //looping for the printing particular number in accordance to the count
                printf("4");
        }

        else if (input[i] >= 'j' && input[i] <= 'l') //condition for printing 5
        {    
            count = input[i] - 'j' + 1;
            for ( j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count//looping for the printing particular number in accordance to the count
                printf("5");
        }

        else if (input[i] >= 'm' && input[i] <= 'o')  //condition for printing 6
        {    
            count = input[i] - 'm' + 1;
            for ( j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count
                printf("6");
        }

        else if (input[i] >= 'p' && input[i] <= 's')  //condition for printing 7
        {    
            count = input[i] - 'p' + 1;
            for ( j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count
                printf("7");
        }

        else if (input[i] >= 't' && input[i] <= 'v')  //condition for printing 8
        {    
            count = input[i] - 't' + 1;
            for (j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count
                printf("8");
        }

        else if (input[i] >= 'w' && input[i] <= 'z')  //condition for printing 9
        {    
            count = input[i] - 'w' + 1;
            for ( j = 0; j < count; j++)  //looping for the printing particular number in accordance to the count
                printf("9");
            
        }
    }
}

int main() 
{
    char input[100];
    printf("Enter the Input: ");
    scanf("%s",input);
    printf("Output: ");
    printKeypadSequence(input);//calling printKeypadSequence for printing the keypad numbers to be pressed
    return 0;
}