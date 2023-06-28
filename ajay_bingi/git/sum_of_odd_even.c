#include<stdio.h>
/*function defination*/
int evenorodd(int index)
{
	if(index%2==0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

/*function to sum*/
int sum(int arr[],int i,int length)
{
	static int totaleven=0,totalodd=0;
	if(evenorodd(i))
	{
		totaleven = totaleven + arr[i];
	}
	else
	{
		totalodd = totalodd + arr[i];
	}
	if(i+1==length)
	{
		if(totaleven>totalodd)
		{
			return totaleven;
		}
		else
		{
			return totalodd;
		}
	}
}

/*function to increment*/
int increment(int arr[],int n,int length,int *ptr)
{
	if(n==length)
	{
		return;
	}
	else
	{
	*ptr = sum(arr,n,length);
	return increment(arr,n+1,length,ptr);
	}

}

int main()
{
	int arr[]={1,5,4,1,6,8,9},i=0,length, value;
	length = sizeof(arr)/sizeof(int);
    /*function call*/
	increment(arr,i,length,&value); 
	printf("max value in the even or odd indexes is %d\n",value);
	return 0;
}