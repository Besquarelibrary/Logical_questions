#include <stdio.h>
int main() {
    char stringing[] = "racecar";
    int frequent[256] = {0};
    int length = 0;
    //to find legnth of stringing
    for(int i=0; stringing[i]!='\0'; i++)
        length++;
    printf("%d\n",length);
    //keeping stringing elementrs as index values for frequent array and incrementing them which are repeated
    for (int i = 0; i <= length; i++) 
        frequent[stringing[i]]++;
    
    int odd_count = 0;
    //checking the which one is not repeated
    for (int i = 0; i < 256; i++) 
    {
        if (frequent[i] % 2 != 0) 
        {
            odd_count++;    //if not repeated then odd_count will  be incremented
        }
    }
    if (length % 2 == 0 && odd_count == 0 || odd_count == 1) 
    {
        printf("it's a palindrome\n");
    }
    else
	printf("it's not a palindrome\n");
    return 0;
}
