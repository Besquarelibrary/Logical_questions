#include <stdio.h>
int main()
{
	char str[]="hii vowel u";
	char str2[100];
	int i,n,j=0;
	puts(str); //print statement
	for(i=0;str[i]!='\0';i++) // looping to copy the vowels in the string 
	{
		if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u') //condition for a vowel
		{
		str2[j] = str[i];
		j++;
		}
	}
	str2[j]='\0';
	puts(str2); // print stateent 
	j--;
	for(i=0;str[i]!='\0';i++)// looping to replace the reversed vowel 
	{
	if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u') //condition for a vowel
		{
		str[i] = str2[j];
		j--;}
	}
	puts(str); // print statement
	
}
