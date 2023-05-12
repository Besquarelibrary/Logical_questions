#include<stdio.h>

int main(){
	int arr[]={1,1,1,2,3,3,1,2,2,2,2,3,3,3,3,2,2,2,2,2,2},i;
	int size=sizeof(arr)/sizeof(int);
	printf("%d\n",size);
	int hash[100]={0};
	for(i=0;i<size;i++)
	{
			hash[arr[i]]++;	
	}
	for(i=0;i<size;i++)
	{
		if(hash[arr[i]]>size/2)
		{
			size=0;
			printf("%d is the majority number \n",arr[i]);
		}
	}
	if(size!=0)
	{
		printf("there are no majority numbers");
	}
	return 0;

}
