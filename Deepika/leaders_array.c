#include <stdio.h>

void printLeaders(int arr[], int size)
{
    int leaders[size], num_leaders = 0, is_leader;
    for(int i=0;i<size;i++){                            //iterate each element of the array
        is_leader=1;                                    //assume current element is a leader
        for(int j=i+1;j<size;j++){                     //check is current element is greater than its right
            if(arr[j]>arr[i]){                        //if the right element is greater than the current element then it's not a leader
                is_leader=0;
                break;
            }
        }
        if (is_leader)                              //if the element is leader then add to the leaders array
        {
            leaders[num_leaders++] = arr[i];
            printf(" %d ",arr[i]);
        }
        
    }
   
   
}


int main()
{
    int arr[] = {1, 7, 9, 8, 3, 6};
    int size = sizeof(arr) / sizeof(arr[0]);      // size of array

    printLeaders(arr, size);                     // Call the function to find and print the leaders


    return 0;
}
