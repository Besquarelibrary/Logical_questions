#include<stdio.h>
int main()
{
	int rows=0,columns=0,number=10; // taking variable for loops and input 
	for(rows=0;rows<=number;rows++) // outer loop for pattern
	{
		for (columns = 0; columns <= rows; columns++) { // inner loop for printing the pattern
            printf("%d",columns); //print statement
        }
        printf("\n");
	}
}

