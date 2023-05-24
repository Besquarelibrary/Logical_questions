#include<stdio.h>
#include<stdlib.h>
int ip(char *str,int a)
{
	int i;
	i=atoi(str);
	
	printf("%dis ip\n",i);
	if(0<=i<=255)
	{
		return 1;
	}
	else
	{
	return 0;
}
}
int main()
{
	char str[]="19.255.226.111";
	char str1[100];
	int i,count=0,validater,k;
	for(i=0;str[i]!='\0';i++)
	{
		str1[count]=str[i];
		count++;
		if(str[i]=='.')
		{
			count--;
			printf("%d\n",count);
			puts(str1);
			if(ip(str1,count))
			{
				validater=validater+1;
			}
			count=0;
		}
		if(str[i+1]=='\0')
		{
			printf("%d\n",count);
			puts(str1);
			if(ip(str1,count))
			{
				validater=validater+1;
			}
			count=0;
		}
	}
	if(validater==4)
	{
		printf("this is valid ip\n");
	}
	else
	{
		printf("this is not vaild\n");
	}
	return 0;
}
