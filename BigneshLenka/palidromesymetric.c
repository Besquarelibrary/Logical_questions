#include<stdio.h>
int evenorodd(int a) //Funtion defination for evenorodd
{
	if(a%2==0){ //condtion for even 
	return 1;} //returning 1 to main
	else 
	return 0;
}
char* rev(char *str,int a) { //funttion defination for rev 
    char *revStr; 
    int i=0;
 for(i=0;i<a;i++) //a is the length of the string //looping till the length of the string
     {
revStr[i] = str[a - i - 1]; //eversing the string 
}
    revStr[a] = '\0';
    puts(revStr);
    return revStr; //returning the reversed string
}

int strcm(char *p1,char *p2,int n) //function defination for strcm 
{
	int i=0,count=0;
	for(i=0;p1[i]!='\0';i++) //looping till null of the string 
	{
		if(p1[i]==p2[i]) // condition for checking each character in the string 
		{
			count++; //incrementing count 
		}
	}
	if(count==n){ //condtion for string are same 
		return 1; //retuning 1 to main
	}
	else{
		return 0; // Returning 0 to main
	}
}
int main()
{
	char str1[100]="amaama";
	char str2[100],str3[100];
	int n=0,i=0,a=0;
	while(str1[n]!='\0') //loop to find the length
	{
		n++;
	}
	printf("%d\n",n);
	if(evenorodd(n)) //condition for even length string // calling evenorodd function
	{
		n=n/2; 
		for(i=0;i<n;i++) //looping till n/2
		{
			str2[i]=str1[i]; // copying str1 to str2 till n/2 length
		}
		str2[i]='\0'; //null to the string2
		printf("%d\n",i);
		printf("%c\n",str1[i]);
		printf("%c\n",str1[i+1]);
		while(str1[i]!='\0') // looping till null of the string
		{
			str3[a]=str1[i]; //copying string 1 to string 3
			a++;
			i++;
		}
		str3[a]='\0';
		puts (str1);
		puts (str2);
		puts (str3);
		if(strcm(str2,str3,n))//condtion for symetric //calling strcm function
		{
			printf("symetric\n"); //print statement for symetric 
		}
		else 
		{
			printf("not symetric\n"); // print statement for not symetric
		}
		if(strcm(str2,rev(str3,a),n)) //condtion for palindrome //calling strcm and rev functions
		{
			printf("  palindrome\n"); //print statement for palidrome 
		}
		else 
		{
			printf("not palindrome\n"); // print statement fot not palidrome
		}
	}
	else{
		printf("the length of the string should be even"); // print statement if the length of the string is not even
	}
	
	return 0;
}
