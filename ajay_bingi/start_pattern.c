#include<stdio.h>
int main()
{
    int number,k;
    printf("Enter a  Number: ");
    scanf("%d",&number);
    /*for printing star pattern*/
    k=number-1;
    for(int i=0; i<number; i++)
    {
        for(int j=0; j<number; j++)
        {
            if(j<k)
                printf(" ");
            else
                printf("*");
        }
        printf("\n");
        k-=1;
    }
}