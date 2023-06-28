/*If the characters in stringing1 is equal to the chracters in  stringing2 irrespective of their positions
is called as ANAGRAM*/

#include <stdio.h>
int same; //here default value is zero
int main() 
{
    char stringing1[]="star";
    char stringing2[]="rast";
    
    int length1=0,length2=0;
    //The below two for loop's is for calculating the length of stringing's
    for(int i=0; stringing1[i]!='\0'; i++)
        length1++;
    for(int i=0; stringing1[i]!='\0'; i++)
        length2++;
    //chechking stringing length's are same or  not 
    if(length1==length2)
    {
    //cehcking each chracter in both the sgtring's
    for(int i=0;i<length1;i++)
    {
        for(int j=0; j<length2; j++)
        {
            //checking they are equal or not 
            if(stringing1[i]==stringing2[j])
            {
                same++; //if equal, increase's and then break the inner for loop
                break;
            }
        }
    }
   if(same==length1)  //checking if same and length1 is equal or not
         printf("its an ANAGRAM....\n");
    
  else
        printf("not matched....\n");
    }
    else
        printf("not matched....\n");
    return 0;
}