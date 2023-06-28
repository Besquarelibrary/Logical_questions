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
int increment(int arr1[],int arr2[],int index,int length,int *ptr) //function defination for increment 
{
	if(index==length) //condtion for unwinding
	{
		return; //returning void
	}
	else
	{
	club(arr1,arr2,index,length,ptr); //calling function club
	return increment(arr1,arr2,index+1,length,ptr); // recursion call
	}
}
int club(int arr1[],int arr2[],int index,int length,int *arr) // fucntion defination for club
{
	static int k=0,l=0; //static storage class is used to avoid destorying or intializing the varibles once
	if(evenorodd(index)) // condtion for checking the index even or odd 
	{
		arr[index]=arr1[k];
		printf("index = %d,k=%d,arr = %d , arr1 = %d\n",index,k,arr[index],arr1[k]); //print statenments
		k++;
	}
	else
	{
		arr[index]=arr2[l];
		printf("index = %d,l=%d,arr = %d , arr2 = %d\n",index,l,arr[index],arr2[l]);//print statenments
		l++;
	}
}
int main()
{
	int arr1[]={1,2,3,4,5},arr2[]={6,7,8,9,10},length1 = 0,length2 = 0,length = 0;
	length1 = sizeof(arr1)/sizeof(int);
	length2 = sizeof(arr2)/sizeof(int);
	length = length1 + length2;
	int arr[length],i=0;
	length = sizeof(arr)/sizeof(int);
	increment(arr1,arr2,i,length,arr); // calling increment function
	return 0;
}
