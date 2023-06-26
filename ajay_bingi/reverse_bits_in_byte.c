#include <stdio.h>

/*function body*/
 void reverseBits(int x) 
{
    int result = 0;
    for (int i = 0; i < 8; i++) 
    {
        /*storing the bits in reverse order*/
        result = (result << 1) | (x & 1); 
        x >>= 1;
    }
    printf("after reversing: %d\n",result);
} 

int main() 
{
    int number;
    printf("Enter an input: ");
    scanf("%d",&number); 
    /*function call to reverse the bits*/
    reverseBits(number);  
   
    return 0;
}
