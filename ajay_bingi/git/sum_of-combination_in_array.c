#include<stdio.h> //Header file for standard input and output 
//function declaration 
void adjacent_value_check(int array[],int index, int array_length, int key_value);
int main()
{
    int array[]={1,2,3,4,5,6,7}; //statically alocating elements in array
    int key_value, array_length=0; // integer variables
    printf("enter key value : ");
    scanf("%d",&key_value); //User input
    //To find the length of array
    for(int i=0; array[i]!='\0'; i++)
    {
        array_length++;
    }
    
    //This loops is for Function call
    for(int j=0; j<array_length; j++)
    {
       adjacent_value_check(array,j,array_length,key_value); //Here I'm passing array,index,array_length,key_value.
    }
}

//Function defination
void adjacent_value_check(int array[], int index, int array_length, int key_value) // I'm Collecting here
{
   //To check for adjacent values that sum up to the key value
    for(int i=index+1; i<array_length; i++)
    {
        if(array[index] + array[i] == key_value)
        printf("(%d %d) ",array[index],array[i]); // printing combination's
    }
}