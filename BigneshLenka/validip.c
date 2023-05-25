#include<stdio.h>
#include<stdlib.h>
int ip(char *str,int a) // function defination of IP
{
	int i;
	i=atoi(str); //using atoi function to convert the ascii to interger
	
	printf("%dis ip\n",i); 
	if(0<=i<=255) //condition for valid IP
	{
		return 1; // returning 1 to main for Valid Ip 
	}
	else
	{
	return 0; //returning 0 to main for invalid IP
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
		if(str[i]=='.') // condtion for stoping the loop and copying the string untill '.' 
		{
			count--; //because it is count '.' as well
			printf("%d\n",count);
			puts(str1);
			if(ip(str1,count)) //calling IP function
			{
				validater=validater+1; //adding values so the validater is equal to 4
			}
			count=0;
		}
		if(str[i+1]=='\0') //condition for stoping the loop and copying the string untill '\0'
		{
			printf("%d\n",count);
			puts(str1);
			if(ip(str1,count)) //calling IP funtion
			{
				validater=validater+1; //adding values so the validater is equal to 4
			}
			count=0;
		}
	}
	if(validater==4) // condition for valid Ip 
	{
		printf("this is valid ip\n");
	}
	else
	{
		printf("this is not vaild\n");
	}
	return 0;
}
