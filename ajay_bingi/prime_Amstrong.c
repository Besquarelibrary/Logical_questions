/*check the number is prime and amstringong and also add the previous element with next elements
and check that they are prime adn amstringong */

#include <stdio.h>
//function declartion's
void prime_check(int num);
void amstringong_check(int num);
int add_two_elements(int a, int b);
int main()
{
   int size,i,j;
   printf("Enter size of an arrayay: ");
   scanf("%d", &size); //user input
   
   int arrayay[size];
   printf("Enter array elements: ");
  //user to enter inputs
   for(i=0; i<size; i++)
      scanf("%d",&arrayay[i]);
   
   //checking the prime and Amstringong
   for(i=0; i<size; i++)
   {
   prime_check(arrayay[i]); 
   amstringong_check(arrayay[i]);
   //to add previous and next element. And to check that number is prime and amstringong
   for(j=i+1; j<size; j++)
   {
    int k=add_two_elements(arrayay[i],arrayay[j]); ///function call to add previous and next elements
    prime_check(k); 
    amstringong_check(k);
   }
   }
}


//add function defination
int add_two_elements(int a, int b)
{
    int temporary = b;
    while (temporary != 0) 
    {
        a *= 10;
        temporary /= 10;
    }
    return a + b;
}

//prime function defination
void prime_check(int num)
{
    int flag=0,i;
    //1 and 0 are not prime numbers
   if (num == 0 || num == 1)
      printf("%d is not a prime number\n", num);
   else 
   {
      for (i = 2; i <= num/2; i++) 
      {
         if (num % i == 0) 
         {
            flag = 1;
            break;
         }
      }
      if (flag == 0)
      {
         printf("%d is a prime number\n", num);
      }
      else
         printf("%d is not a prime number\n", num);
   }
}

//amstringong function defination
void amstringong_check(int num)
{
    int temporary,sum=0,n=0,rem; 
    
    temporary = num;
    //counting no of digit present in input
    while (temporary != 0) 
    {
      temporary /= 10;
      ++n;
    }
    
   temporary = num;
   while (temporary != 0) 
   {
      rem = temporary % 10;
      //sum += pow(rem, n);
      sum +=rem<<n;
      // sum +=rem*n*n;
      temporary /= 10;
   }
   if (sum == num)
   {
      printf("%d is an Armstringong number\n", num);
   }
   else
      printf("%d is not an Armstringong number\n", num);
}

