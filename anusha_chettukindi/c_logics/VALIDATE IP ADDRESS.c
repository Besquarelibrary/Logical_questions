QUESTION:
PROGRAM TO CHECK WHETHER THE IP ADDRESS ENTERED BY THE USER IS VALID OR NOT

PROGRAM:
#include <stdio.h>
#include<string.h>
#include<stdlib.h>
int a_to_i(char w[3]){
    int sign=1;
    int result,i=0;
    if(w[i]=='-'){
        sign=-1;
        i=1;
    }
    while(w[i]!='\0'){
        if(w[i]>='0' && w[i] <= '9'){
            result = result * 10 + (w[i] - '0');
        }
        else{
            printf("invalid input\n");
            break;
        }
        i++;
    }
    return result*sign;
}

int main() {
    char s[12];
    int num;
    int count=0;
    printf("enter ip");
    gets(s);
    char w[3];
    int j=0;
    for(int i=0;s[i]!='\0';i++){
        if(s[i]!='.'){
            w[j]=s[i];
            j++;
        }
        else{
            w[j]='\0';
            num=a_to_i(w);
            if(0<=num<=255){
                count=count+1;
            }
            else{
                break;
            }
            j=0;
        }
    }
    if(j>0){
        w[j]='\0';
        num=a_to_i(w);
        if(0<=num<=255){
            count=count+1;
        }
    }
    if(count==4){
        printf("valid ip");
    }
    else{
        printf("Invalid ip");
    }
}
OUTPUT:
enter ip123.8.(
invalid input
Invalid ip
