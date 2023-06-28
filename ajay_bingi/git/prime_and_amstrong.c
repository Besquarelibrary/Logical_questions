/*check the number is prime and amstrong and also add the previous element with next elements
and check that they are prime adn amstrong */
/*check the number is prime and amstringong and also add the previous element with next elements
and check that they are prime adn amstringong */

#include <stdio.h>
//function declartion's
void prime_check(int num);
void amstrong_check(int num);
void amstringong_check(int num);
int add_two_elements(int a, int b);
int main()
{
@@ -18,17 +18,17 @@ int main()
   for(i=0; i<size; i++)
      scanf("%d",&arrayay[i]);

   //checking the prime and Amstrong
   //checking the prime and Amstringong
   for(i=0; i<size; i++)
   {
   prime_check(arrayay[i]); 
   amstrong_check(arrayay[i]);
   //to add previous and next element. And to check that number is prime and amstrong
   amstringong_check(arrayay[i]);
   //to add previous and next element. And to check that number is prime and amstringong
   for(j=i+1; j<size; j++)
   {
    int k=add_two_elements(arrayay[i],arrayay[j]); ///function call to add previous and next elements
    prime_check(k); 
    amstrong_check(k);
    amstringong_check(k);
   }
   }
}
@@ -72,8 +72,8 @@ void prime_check(int num)
   }
}

//amstrong function defination
void amstrong_check(int num)
//amstringong function defination
void amstringong_check(int num)
{
    int temporary,sum=0,n=0,rem; 

@@ -96,9 +96,9 @@ void amstrong_check(int num)
   }
   if (sum == num)
   {
      printf("%d is an Armstrong number\n", num);
      printf("%d is an Armstringong number\n", num);
   }
   else
      printf("%d is not an Armstrong number\n", num);
      printf("%d is not an Armstringong number\n", num);
}