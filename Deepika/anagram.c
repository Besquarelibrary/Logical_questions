#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "deepika majji";
    char str2[] = "majji deepika";
    int count = 0;

    int len1 = strlen(str1);                  //size of string 1
    int len2 = strlen(str2);                 //size of string 2

    if (len1 == len2) {                      //check if the lengths of the strings are equal
        for (int indexstr1 = 0; indexstr1 < len1; indexstr1++) {         //iterating each character in str1
            for (int indexstr2 = 0; indexstr2 < len2; indexstr2++) {     //iterating each character in str2
                if (str1[indexstr1] == str2[indexstr2]) {    //check is any character is matching in str1 with str2
                    count++;                 //if found any characted increment count and break the inner loop
                    break;
                }
            }
        }

        if (count == len2) {               //check count is equal to string length
            printf("Anagrams\n");          //if equal print anagram
        }
        else{                              //else print not an anagram
            printf("not an anagram");
        }
    }

    return 0;
}

