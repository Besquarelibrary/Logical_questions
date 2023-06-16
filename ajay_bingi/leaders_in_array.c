#include <stdio.h>

//function defination
void printLeaders(int array[], int size)
{
    int leaders[size], num_leader = 0;

    //to find leader
    for (int i = 0; i < size; i++) 
    {
        int is_leader = 1;
        for (int j = i + 1; j < size; j++) 
        {
            if (array[j] > array[i]) 
            {
                is_leader = 0;
                break;
            }
        }
        if (is_leader) 
        {
            leaders[num_leader++] = array[i];
        }
    }

    printf("Leaders: ");
    //printing leasders
    for (int i = 0; i < num_leader; i++) 
    {
        printf("%d ", leaders[i]);
    }
    printf("\n");
}

int main()
{
    int array[] = {1,7,9,8,3,6};
    int size=sizeof(array)/sizeof(array[0]);

    printLeaders(array, size); //function call

    return 0;
}