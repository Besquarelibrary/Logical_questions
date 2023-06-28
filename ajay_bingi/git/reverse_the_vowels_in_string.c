#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    int size;
    printf("Enter the size of a string: ");
    scanf("%d", &size);
    char *str = malloc(size*sizeof(char));
    printf("Enter string: ");
    scanf("%s", str);
    int length = strlen(str);
    char *i = str+0, *j = str+length-1; //two pointers technique
//printf("i=%d j=%d\n",*i,*j);
    // loop until i and j cross each other
    while(i < j) 
    {
        // if i is not a vowel, move to next character
        if(*i != 'a' && *i != 'e' && *i != 'i' && *i != 'o' && *i != 'u' &&
           *i != 'A' && *i != 'E' && *i != 'I' && *i != 'O' && *i != 'U') {
            i++;
        }
        // if j is not a vowel, move to previous character
        else if(*j != 'a' && *j != 'e' && *j != 'i' && *j != 'o' && *j != 'u' &&
                *j != 'A' && *j != 'E' && *j != 'I' && *j != 'O' && *j != 'U') {
            j--;
        }
        // if both i and j are vowels, swap them
        else {
            char temp = *i;
            *i = *j;
            *j = temp;
            i++;
            j--;
        }
    }
    printf("Reversed vowels string: %s", str);
    free(str);
    return 0;
}