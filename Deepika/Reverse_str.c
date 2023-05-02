#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main() {
    char str[100]="deepu deepika";
    int i, len;
    len = strlen(str);

    printf("Reverse string order:\n");

    for(i = len - 1; i >= 0; i--) {
        if(str[i] == ' ' || i == 0) { 
            int j;
            if(i == 0) 
                j = i;
            else 
                j = i + 1;
            while(str[j] != '\0' && str[j] != 32) 
            {
                printf("%c", str[j]);
                j++;
            }
            if (i > 0) 
                printf(" ");
        }
    }

    return 0;
}
