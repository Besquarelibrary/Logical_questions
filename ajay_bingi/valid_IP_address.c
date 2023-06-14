#include <stdio.h>
// Function to convert a string to an integer
int a_to_i(char w[3]) 
{
    int sign = 1;
    int result, i = 0;
    
    if (w[i] == '-') 
    {
        sign = -1;
        i = 1;
    }
    
    while (w[i] != '\0') 
    {
        if (w[i] >= '0' && w[i] <= '9') 
        {
            result = result * 10 + (w[i] - '0');
        }
        else 
        {
            printf("invalid input\n");
            break;
        }
        i++;
    }
    
    return result * sign;
}

//main function 
int main() {
    char s[12];
    int num;
    int count = 0;
    
    printf("Enter IP address: ");
    scanf("%s", s);
    
    char w[3];
    int j = 0;
    
    // Loop through each character in the input string
    for (int i = 0; s[i] != '\0'; i++) 
    {
        if (s[i] != '.') 
        {
            w[j] = s[i];
            j++;
        }
        else 
        {
            w[j] = '\0';
            num = a_to_i(w);
            
            // Check if the extracted number is within the valid range
            if (0 <= num <= 255) 
                count = count + 1;
    
            else 
                break;
            
            
            j = 0;
        }
    }
    
    // Check if there is a remaining number after the last dot
    if (j > 0) 
    {
        w[j] = '\0';
        num = a_to_i(w);
        
        // Check if the extracted number is within the valid range
        if (0 <= num <= 255) 
            count = count + 1;
    }
    
    // Check if there are exactly four valid numbers
    if (count == 4)
        printf("Valid IP");
    
    else 
        printf("Invalid IP");
    
    
    return 0;
}
