#include<stdio.h>
char* rev(char *str,int a)
{
	char *revStr; 
    int i=0;
 for(i=0;i<a;i++) //a is the length of the string //looping till the length of the string
     {
revStr[i] = str[a - i - 1]; //eversing the string 
}
    revStr[a] = '\0';
    return revStr; //returning the reversed string
}
int main()
{
	int i,j,count=0;
	char str1[]="hii im bignesh"; 
	char str2[100]; 
	char *str3;
	for(i=0;str1[i]!='\0';i++) //looping till null character to copy the string1 words to string2
	{
		str2[count]=str1[i];
		count++;
		if(str1[i+1]== ' ') //condition for copying till space character 
		{
			str3=rev(str2,count); //call rev function
			count=0;
			puts(str3); //printing reversed words
		}
		if(str1[i+1]== '\0') //condition for copying till null character
		{
			str3=rev(str2,count); //call rev function
			count=0;
			puts(str3); //printing reversed words
		}	
	}
	return 0;
}
