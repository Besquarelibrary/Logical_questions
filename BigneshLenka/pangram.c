#include<stdio.h>
int main()
{
	int i,count[26],found;
	char str[]="this is Bignesh lenka";
	for(i=0;str[i]!='\0';i++) //looping for accessing the characters in the string
	{
		
		count[str[i]-'a']++; //logic for counting each character count in the string
	}
	found=1; //using for condition
	for(i=0;i<26;i++) // looping to check the count arrray
	{
		if(count[i]==0) //condition if the alphabet not being in the string
		{
			found=0; // Using for condition
			printf("%c ",i+'a');
		}
	}
	if(found) //condition for pangram
	{
		printf("pangram");
	}
	else
	{
		printf(" are the repeated elements");
	}
	return 0;
}
