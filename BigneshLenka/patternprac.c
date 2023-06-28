#include<stdio.h>
int main()
{
	int rows=0,columns=0,number=10; // taking variable for loops and input 
	for(rows=0;rows<=number;rows++) // outer loop for printing the upperhalf pattern
	{
		for (columns = 0; columns <= rows; columns++) { // inner loop for printing the upperhalf pattern
            printf("%d",columns);
        }
        printf("\n");
	}
	for(rows = rows - 2 ; rows >= 0;rows--) // outerloop for printing the lower half
	{
		for (columns = 0; columns <= rows ; columns++) { // inner loop for printing the lowerhalf pattern
            printf("%d",columns);
        }
        printf("\n");	
	}
}

