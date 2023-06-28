#include<stdio.h>
int evenorodd(int index) //function defination for evenodd
{
	if(index%2==0) //condition for number being even
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int sum(int arr[],int i,int length) //function defination for sum
{
	static int totaleven=0,totalodd=0; //static storage class is used to avoid destorying or intializing the varibles once
	if(evenorodd(i)) //static storage class is used to avoid destorying or intializing the varibles once
	{
		totaleven = totaleven + arr[i];
	}
	else
	{
		totalodd = totalodd + arr[i];
	}
	if(i+1==length) //contion for checking index equals to length
	{
		if(totaleven>totalodd) //conditon if the total even sum is greater than total odd sum
		{
			return totaleven;
		}
		else
		{
			return totalodd;
		}
	}
}
int increment(int arr[],int n,int length,int *ptr) //funtion defination for increment
{
	if(n==length) //condtion for unwinding the recursion
	{
		return;
	}
	else
	{
	*ptr = sum(arr,n,length); // value of fucntion sum is assigned to ptr
	return increment(arr,n+1,length,ptr); //recursion call
	}

}

int main()
{
	int arr[]={1,5,4,1,6,8,9},i=0,length, value;
	length = sizeof(arr)/sizeof(int);
	increment(arr,i,length,&value);
	printf("max value in the even or odd indexes is %d\n",value);
	return 0;
}
