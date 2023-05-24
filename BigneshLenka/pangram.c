#include<stdio.h>
int main()
{
	int i,count[26],found;
	char str[]="this is Bignesh lenka";
	for(i=0;str[i]!='\0';i++)
	{
		
		count[str[i]-'a']++;
	}
	found=1;
	for(i=0;i<26;i++)
	{
		if(count[i]==0)
		{
			found=0;
			printf("%c ",i+'a');
		}
	}
	if(found)
	{
		printf("pangram");
	}
	else
	{
		printf(" are the repeated elements");
	}
	return 0;
}
