#include<stdio.h>
int main()
{
    int number;
    printf("Enter a  Number: ");
    scanf("%d",&number);
    /*for printing Number pattern in this code*/
    for(int i=1; i<=number; i++)
    {
        for(int j=1; j<=i; j++)
            printf("%d",j);
        printf("\n");
    }
}

