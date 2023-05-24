#include <stdio.h>
#include <string.h>

void printKeypadSequence(char *input) {
    int length = strlen(input),i,j;
  
    for (i = 0; i < length; i++) {
        int count = 0;
      if (input[i] == ' ' ) {
                printf("0");
        }
        if (input[i] >= 'a' && input[i] <= 'c') {
            count = input[i] - 'a' + 1;
            for ( j = 0; j < count; j++) {
                printf("2");
            }
        }
        else if (input[i] >= 'd' && input[i] <= 'f') {
            count = input[i] - 'd' + 1;
            for ( j = 0; j < count; j++) {
                printf("3");
            }
        }
        else if (input[i] >= 'g' && input[i] <= 'i') {
            count = input[i] - 'g' + 1;
            for ( j = 0; j < count; j++) {
                printf("4");
            }
        }
        else if (input[i] >= 'j' && input[i] <= 'l') {
            count = input[i] - 'j' + 1;
            for ( j = 0; j < count; j++) {
                printf("5");
            }
        }
        else if (input[i] >= 'm' && input[i] <= 'o') {
            count = input[i] - 'm' + 1;
            for ( j = 0; j < count; j++) {
                printf("6");
            }
        }
        else if (input[i] >= 'p' && input[i] <= 's') {
            count = input[i] - 'p' + 1;
            for ( j = 0; j < count; j++) {
                printf("7");
            }
        }
        else if (input[i] >= 't' && input[i] <= 'v') {
            count = input[i] - 't' + 1;
            for (j = 0; j < count; j++) {
                printf("8");
            }
        }
        else if (input[i] >= 'w' && input[i] <= 'z') {
            count = input[i] - 'w' + 1;
            for ( j = 0; j < count; j++) {
                printf("9");
            }
        }
    }
}

int main() {
    char input[100]="hduc  jidibcic  m";
  
    printf("Output: ");
    printKeypadSequence(input);
  
    return 0;
}
