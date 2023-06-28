#include<stdio.h>
int main(){
    int arr[20]={1,4,5,3,6,9,8,15};
    int i,j,temp;
    for (i = 0;arr[i]!='\0'; i++)                       //using loop for sorting the array
        for (j = i+1;arr[j]!='\0'; j++) {
            if (arr[i] > arr[j]) {                  
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    printf("sorted array : ");                       // printing the sorted array
    for(i=0;arr[i]!='\0';i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
    int k=1;
    for(i=0;arr[i]!='\0';i++)                     // using loop for finding the missing number in the given array
    {
        if(k!=arr[i])                            // if the number is not in the array it will print that number 
        {
            printf("%d ",k);
            k++;
            i--;
        } 
        else{                                   // else it will continue the loop
            k++;
        }
    }
  
    return 0;
}
