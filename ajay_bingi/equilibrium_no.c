/*The sum of numbers which is left of that number and righr  of that number is equal,
then the middle one is called as EQUILIBRIUM NUMBER*/

#include <stdio.h>
//function defination
int equilibrium(int arrayay[], int length_of_arrayay) 
{
   int sum1 = 0, sum2 = 0; //initializing the variables with value 0

  // this for loo[p is to add all elements
   for (int i = 0; i <= length_of_arrayay; i++) 
   {
      sum1 += arrayay[i];
   }

    // this loop is for finding the Kth smallest element
   for (int i = 0; i <= length_of_arrayay; i++) 
   {
      sum1 -= arrayay[i]; //removing each element from sum1
      if (sum2 == sum1) //checking if sum1 is equal to sum2
      {
         return arrayay[i]; // if condition is true returning that index value
      }
      sum2 += arrayay[i]; // if  not then adding element to sum2 variable
   }

   return -1;
}

int main() 
{
   int arrayay[] = {1,1,5,1,5,1,1}; //initializing arrayay with elements
   int length_of_arrayay=0;
   //fthis loop is for sfiding lenght of arrayay
   for(int i=0; arrayay[i]!='\0'; i++)
        length_of_arrayay++;

   int x = equilibrium(arrayay, length_of_arrayay); // function call

   if (x == -1) 
   {
      printf("No equilibrium index found\n");
   } 
   else 
   {
      printf("Equilibrium number is %d\n",x);
   }
}