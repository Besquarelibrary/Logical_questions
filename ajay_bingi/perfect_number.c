/*Summ of factors of given number is equal to that number except that number is called PERFECT NUMBER*/

#include <stdio.h>   

void check_perfect(int);  // Function declaration for checking perfect number

int main() 
{
    int n; 
    printf("enter a number: "); 
    scanf("%d",&n);  //user input
    check_perfect(n); // Function call
    return 0; 
}

// Function definition
void check_perfect(int n) 
{
    int sum=0; 
    //To find perfect number
    for(int i=1; i<n; i++) 
    {
        if(n%i==0) // Checking if the number is a factor of the input number
        {
            sum+=i; // If it is, adding the factor to the sum
        }
    }
    if(sum==n) // Comapring the sum and input number are same or not
    printf("perfect number\n"); 
    else 
    printf("not a perfect number\n"); 
} 