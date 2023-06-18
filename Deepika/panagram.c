#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

bool isPangram(const char *str) {
    int count[ALPHABET_SIZE] = {0}; // Initialize count array to 0

    for (int i = 0; str[i] != '\0'; i++) { // Iterate over each character in the string
        char c = tolower(str[i]); // Convert character to lowercase

        // Check if the character is a lowercase letter 'a' to 'z'
        if (c >= 'a' && c <= 'z') {
            count[c - 'a']++; // Increment the count for the corresponding letter
        }
    }

    for (int i = 0; i < ALPHABET_SIZE; i++) {
        printf("Count of %c: %d\n", i + 'a', count[i]);
    }

    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (count[i] == 0) { // If any count is 0, the letter is missing
            return false; // Not a pangram
        }
    }

    return true; // All letters are present, it is a pangram
}

int main() {
    const char *str = "The quick brown fox jumps over the lazy dog";

    if (isPangram(str)) {
        printf("The string is a pangram.\n");
    } else {
        printf("The string is not a pangram.\n");
    }

    return 0;
}
