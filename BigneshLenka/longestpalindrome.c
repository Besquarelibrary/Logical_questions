#include <stdio.h>
int maxelement(int *arr,int size,int *max,int *maxindex) //maxelement function defination
{
	int i;
	*max=arr[0];
	for(i=0;i<size;i++) //looping to find the max element
	{
		if(arr[i] > *max) //condition to find max element
		{
			*max=arr[i]; //return max element
			*maxindex = i; //returning maxelemnt index
		
	}
	
}
int main()
{
	int arr[]={121,555,666,98589,235,239,768},n,i,temp,sum,r,count[10]={0},max,maxindex,k;
	k=sizeof(arr)/sizeof(int);
	for(i=0;arr[i]!='\0';i++) // lloping till null 
	{
		temp=arr[i];
		n=arr[i];
		sum=0;
		while(n>0) //looping to find a number is palindrome
		{
			r=n%10; //logic for a number to in palindrome
			sum=sum*10+r;
			n=n/10;
			count[i]++;
		}
		if(temp==sum) //condition for a number to be palindrome
			printf("%d is a palindrome\n",temp); //print statement
		else
			printf("%d is not a palindrome\n",temp); //print statement
	
	}
		n=sizeof(count)/sizeof(int);
		maxelement(count,n,&max,&maxindex); // calling maxelement fucntion
		printf("%d is the longest palindrome",arr[maxindex]); //print statement
	
	return 0;
}
