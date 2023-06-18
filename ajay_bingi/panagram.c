#include<stdio.h>
int main()
{
    char stringing[]="abcdefghijklmnopqrstuvwxyz";
    int i,count=0;
    //this loop is fot checking the each character in a stringing having 26 alphabet's or not
    for(i=0; stringing[i]!='\0'; i++)
    {
       if(stringing[i]>='a'&&stringing[i]<='z' || stringing[i]>='A'&&stringing[i]<='Z')  
        count++;
    }
    if(count>=26)
    printf("The given stringing is a Panagram\n");
    else
    printf("The given stringing is not a Panagram\n");
}