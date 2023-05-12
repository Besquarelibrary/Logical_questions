#include<stdio.h>
int perfect(int k);//declaration
int main()
{
	int a[]={1,2,3,4,5,6,7,8,9,10,11,28,496,497}; //input array
	int i,j,n=0; // for looping
	for(i=0;a[i]!='\0';i++) //loop to find the perfect number
	{
	if(perfect(a[i])==a[i]) //function call passing an array element which returns n that is the sum of divisibles of the element and the condition which finds the sum of divisibles are equal to element  
	{
	printf("%d is a perfect number\n",a[i]);//print statement
	}
	}
	return 0;
	}
int perfect(int k) //defination 
{
	int j,n=0; //for looping
	for(j=1;j<=k/2;j++){ // looping till k/2 because there will be diviables of k after k/2
		if(k%j==0) //condition to check the divisibilty
		{
			n=n+j; //summing the numbers to find to it is perfect or not
		}
	}
	return n; // returning n to the function
}
/****************** another way to find the perfet number whose time complexity is n^2 **********************/ 
//		for(j=1;j<=a[i]/2;j++){
//		if(a[i]%j==0)
//		{
//			n=n+j;
//			if(n==a[i])
//			{
//				printf("%d is a perfect number\n",a[i]);
//			}
//			
//		}
//	}
