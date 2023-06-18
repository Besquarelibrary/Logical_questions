#include<stdio.h>
#include<string.h>
int main()
{
	char str1[]="Hii i'm, bigneh lenka what ;  about u    hii";
	int i,n,x;
	n=2;
	if(n==0)
	{
		printf("a number that greater than 0\n");
		scanf("%d",&n);
	}
	for(i=0;str1[i]!='\0';i++) //looping till the end of the string 
	{
		x=n*i;
		if(x<strlen(str1)) //condtion if x is less than length of the string
		{
			if(str1[x]>='a'&&str1[x]<='z') // condtion for strings for letting in only alphabets
			printf("The character is %c\n",str1[x]);
			if(str1[x]>=' '&&str1[x]<='@') //condtion if string element having special characters and space
			{
				x=x+1;
				if(str1[x]>=' '&&str1[x]<='@') //condtion if string element having special characters and space
				{
					while(str1[x]>=' '&&str1[x]<='@') //looping untill a alphabet is accessed
					{
						x=x+1;
					}
					printf("the character is after two spaces = %c \n",str1[x]); //print statement for the nth table character if space detected 
				}
				else
				{
					printf("the character at %d*%d+1 is %c\n",n,i,str1[x]); // print statement for the nth table character
				}
			}
		}
		
	}
	return 0;
}


