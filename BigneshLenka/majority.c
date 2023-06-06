#include<stdio.h>

int main(){
	int arr[]={1,1,1,2,3,3,1,2,2,2,2,3,3,3,3,2,2,2,2,2,2},i; //taking an array as an input and i for looping
	int size=sizeof(arr)/sizeof(int); //calculating the size of the array
	int hash[100]={0}; //taking a extra array to find  and mainain the array elements repeation count
	for(i=0;i<size;i++) //loop to maintain the count
	{
			hash[arr[i]]++;	//increament count of the elemnet's repeation by one
	}
	for(i=0;i<size;i++) //loop for checking wheather there is a majority nummber
	{
		if(hash[arr[i]]>size/2) //conditon for majority
		{
			size=0; //for the array where there are no majority elemnets
			printf("%d is the majority number \n",arr[i]); //print statement
		}
	}
	if(size!=0) //condition for no majority elements
	{
		printf("there are no majority numbers"); // print statement
	}
	return 0;

}}
