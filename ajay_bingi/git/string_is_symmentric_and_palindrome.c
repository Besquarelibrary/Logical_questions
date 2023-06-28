#include<stdio.h>
int my_strcmp(char s1[], char s2[]);
int my_stringcmp(char s1[], char s2[]);
void check(char [],int);
int str_len;
int string_len;
int main()
{
    char str[]="level";
    char string[]="level";
    //for checking length
    for(int i=0; str[i]!='\0'; i++)
    for(int i=0; string[i]!='\0'; i++)
    {
        str_len++;
        string_len++;
    }
    check(str,str_len);
    check(string,string_len);
}
void check(char str[], int len)
void check(char string[], int len)
{
    char temporary1[50],temporary2[50],temporary3[50];
    int mid_ind=len/2;
    //1st half of string
    //1st half of stringing
    for(int i=0; i<mid_ind; i++)
        temporary1[i]=str[i];    
        temporary1[i]=string[i];    

    //2nd half of string
    //2nd half of stringing
    for(int i=mid_ind; i<len; i++)
        temporary2[i-mid_ind]=str[i];
        temporary2[i-mid_ind]=string[i];

    //reverse of 2nd string
    //reverse of 2nd stringing
    for(int i=len-1; i>=mid_ind; i--)
        temporary3[len-1-i]=str[i];
        temporary3[len-1-i]=string[i];

    if(my_strcmp(temporary1,temporary2)==0 && my_strcmp(temporary1,temporary3)==0)  
    if(my_stringcmp(temporary1,temporary2)==0 && my_stringcmp(temporary1,temporary3)==0)  
    printf("it is Symentric and Palindrome\n");
    else if(my_strcmp(temporary1,temporary2)==0)
    else if(my_stringcmp(temporary1,temporary2)==0)
    printf("it is Symentric\n");
    else if(my_strcmp(temporary1,temporary3)==0)
    else if(my_stringcmp(temporary1,temporary3)==0)
    printf("it is Palindrome\n");
    else
    printf("not Symentric and not Palindrome");
}


// user-defined strcmp function
int my_strcmp(char s1[], char s2[]) {
// user-defined stringcmp function
int my_stringcmp(char s1[], char s2[]) {
  int i = 0;
  while (s1[i] == s2[i]) {
    if (s1[i] == '\0' || s2[i] == '\0')
      break;
    i++;
  }
  if (s1[i] == '\0' && s2[i] == '\0')
    return 0;
  else if (s1[i] < s2[i])
    return -1;
  else
    return 1;
}