/*The number which is equal, when we read it from left or right is called palindrome */

#include<stdio.h>
int ispalindrome(int num) //function defination
{
     int sum=0, temporaryorary_variable = num, reminder;

    //for reversing the number
     while(temporaryorary_variable)
     {
          reminder = temporaryorary_variable%10;
          sum = sum*10 + reminder;
          temporaryorary_variable /= 10;
     }
     
    //comparing if the reversed number and actuall nummber is same or not
      if(num==reminder)
        return 1;
      else
        return 0;
}

int main()
{
    int arrayay[] = {121,2551552,6116,07,1001},k=0;
    int size=0;
    //to find length of arrayay
    for(int i=0; arrayay[i]!='\0'; i++)
        size++;
  
    for(int i=0; i<=size; i++)
    {
             if(ispalindrome(arrayay[i])) //function call  in if statement
             {
                if(arrayay[i]>k)  //checking if arrayay element is greater than the k value 
                {
                  k=arrayay[i];      
                }
             }
    }
    printf("longest palindrome in a given arrayay is: %d \n",k);
}