#include<stdio.h>
int my_strcmp(char s1[], char s2[]);
void check(char [],int);
int str_len;
int main()
{
    char str[]="level";
    //for checking length
    for(int i=0; str[i]!='\0'; i++)
    {
        str_len++;
    }
    check(str,str_len);
}
void check(char str[], int len)
{
    char temporary1[50],temporary2[50],temporary3[50];
    int mid_ind=len/2;
    //1st half of string
    for(int i=0; i<mid_ind; i++)
        temporary1[i]=str[i];    

    //2nd half of string
    for(int i=mid_ind; i<len; i++)
        temporary2[i-mid_ind]=str[i];

    //reverse of 2nd string
    for(int i=len-1; i>=mid_ind; i--)
        temporary3[len-1-i]=str[i];

    if(my_strcmp(temporary1,temporary2)==0 && my_strcmp(temporary1,temporary3)==0)  
    printf("it is Symentric and Palindrome\n");
    else if(my_strcmp(temporary1,temporary2)==0)
    printf("it is Symentric\n");
    else if(my_strcmp(temporary1,temporary3)==0)
    printf("it is Palindrome\n");
    else
    printf("not Symentric and not Palindrome");
}


// user-defined strcmp function
int my_strcmp(char s1[], char s2[]) {
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
















