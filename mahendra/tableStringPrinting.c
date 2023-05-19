//stdio.h library provides functions for input and output operations
//string.h library provides functions and macros for working with strings like “strlen”
#include <stdio.h> 
#include <string.h>

int main() {
    int i, n, x, l;
    char str[] = "Hii all of you take, care of your self, guide other guies";
    l = strlen(str);

    printf("Enter number for table: ");
    scanf("%d", &n);

    for (i = 0; i < l; i++) 
    {
        if (i % n == 0) 
	{
            x = i;
            // Check if the character at index x is not a space (32), comma (44), exclamation mark (33), question mark (63), or colon (58)
            if (str[x] != 32 && str[x] != 44 && str[x] != 33 && str[x] != 63 && str[x] != 58) 
	    {
                printf("%d * %d = %c\n", n, i/n+1, str[x]);
            }
            //If the character at index x is a space, comma, exclamation mark, question mark, or colon
	    else if (str[x] == 32 || str[x] == 44 || str[x] == 33 || str[x] == 63 || str[x] == 58) 
	    {
                //Check i+2 value lessthen l or not 
                if (i+1 < l) 
		{
                    x = i+1;//Increase i value by 1 and assign to x
                    //Check if the character at index 'x' is not a space, comma, exclamation mark,question mark, or colon
                    if (str[x] != 32 && str[x] != 44 && str[x] != 33 && str[x] != 63 && str[x] != 58) 
		    {
                        printf("%d * %d = %c\n", n, i/n+1, str[x]);
                    }
                    //If the character at index x is a space, comma, exclamation mark, question mark, or colon
		    else if (str[x] == 32 || str[x] == 44 || str[x] == 33 || str[x] == 63 || str[x] == 58) 
		    {
                        //Check i+2 value lessthen l or not 
                        if (i+2 < l) 
			{
                            x = i+2;//Increase i value by 2 and assign to x
                            // Check if the character at index 'x' is not a space, comma, exclamation mark, question mark, or colon
                            if (str[x] != 32 && str[x] != 44 && str[x] != 33 && str[x] != 63 && str[x] != 58) 
			    {
                                printf("%d * %d = %c\n", n, i/n+1, str[x]);
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}
