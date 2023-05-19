#include <stdio.h>  // Header for input and output
#include <string.h> // Header for string_length

// Function to convert integer values into a string representing an IP address
void intToIP(int a, int b, int c, int d, char* ip_str) {
    sprintf(ip_str, "%d.%d.%d.%d", a, b, c, d);
}

// Function to check if a string represents a valid IP address
int isValidIP(char* ip_str) {
    int nums[4] = {0}; // Array to store the 4 numbers of the IP address
    int count = 0;     // Counter for the numbers
    int num = 0;       // Current number being constructed

    for (int i = 0; ip_str[i] != '\0'; i++) {
        if (ip_str[i] == '.' || ip_str[i] == '\0') {
            nums[count] = num; // Store the completed number as a array element 
            num = 0;           // Reset the number variable after every '.'
            count++;           // Increment the count variable 
        } else {
            num = num * 10 + (ip_str[i] - '0'); // Build the number digit by digit
        }
    }

    // Check if the IP address is valid
    if (count != 4) {
        return 0; // Invalid IP address format
    }
    //Iterate over each 'nums'array  element
    for (int i = 0; i < count; i++) {
        //Check array element in between 0 to 255 or not 
        if (nums[i] < 0 || nums[i] > 255) {
            return 0; // Invalid number
        }
    }

    return 1; // Valid IP address
}


int main() {
    int a, b, c, d;//initialise int variable’s for input  
    printf("Enter an IP address in the form of a.b.c.d: ");
    scanf("%d.%d.%d.%d", &a, &b, &c, &d);//taking input from user 

    //declares a character array named 'ip_str' with a size of 16
    char ip_str[16];
    //function call to the 'intToIP' function, passing the arguments a, b, c, d, and ip_str.
    intToIP(a, b, c, d, ip_str);

    printf("IP address as string: %s\n", ip_str);
    // checking ip address is valid or not 
    if (isValidIP(ip_str)) {
        printf("Valid IP address\n");
    } else {
        printf("Invalid IP address\n");
    }
    
    return 0;
}
