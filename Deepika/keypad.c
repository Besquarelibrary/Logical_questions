#include <stdio.h>
#include <string.h>

void printKeyMappings(char input)
{
    // Define the character to string mappings
    const char* mappings[26] = {
        "2", "22", "222",               // a, b, c
        "3", "33", "333",              // d, e, f
        "4", "44", "444",              // g, h, i
        "5", "55", "555",             // j, k, l
        "6", "66", "666",            // m, n, o
        "7", "77", "777", "7777",   // p, q, r, s
        "8", "88", "888",           // t, u, v
        "9", "99", "999", "9999"    // w, x, y, z
    };

    if (input >= 'a' && input <= 'z') {
        int index = input - 'a';             // Calculate the index based on ASCII value
        printf("%s", mappings[index]);      // Print the corresponding string
    }
}

int main()
{
    char input[100];

    printf("Enter a string (a-z): ");
    fgets(input, sizeof(input), stdin);

    size_t len = strlen(input);         // length of the string

    printf("Output: ");
    for (int i = 0; i < len; i++) {     
        printKeyMappings(input[i]);
    }
    printf("\n");

    return 0;
}
