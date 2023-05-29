#include<stdio.h>
int main()
{
	char str1[]="hii im big";
	char str2[]="big im hii";
	int i,n,same=0,count1[200]={0},count2[200]={0};
	for(i=0;str1[i]!='\0';i++) // loop to find the characters count 
	{
		count1[str1[i]-'a']++;
	}
	for(i=0;str2[i]!='\0';i++) // loop to find the characters count
	{
		count2[str2[i]-'a']++;
	}
	n=sizeof(count1)/sizeof(int);
	for(i=0;i<n;i++) // loop to find whether the two arrays are same
	{
		if(count1[i]==count2[i]) //condition to find whether the two arrays are same
		{
			same++;
		}
	}
	if(same==n-1)//condition to find the whether the strings are anagram
	{
		printf("the strings are in anagram\n"); //print statement
	}
	else
	{
		printf("the strings are not in anagram\n"); //print statement
	}
	return 0;	
}
