#include <stdio.h>
/*fucntion body*/
int findHCF(int num1, int num2) 
{
    int temp;

    while (num2 != 0) {
        temp = num2;
        num2 = num1 % num2;
        num1 = temp;
    }
    return num1;
}

int main() 
{
    int num1, num2;

    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    int hcf = findHCF(num1, num2); // function call

    printf("The HCF is %d\n",hcf);
}