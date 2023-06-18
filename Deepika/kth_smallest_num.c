#include<stdio.h>
int main()
{
    int i,len,j;
    int arr[]={4,2,3,8,1,9};                     
    len=sizeof(arr)/sizeof(arr[0]);                 // length of the array
    int k=1;                                        
    if(k>len){                                      // checking k value is greater or smaller than length
        return 0;                                   
    }
    for(i=0;i<len;i++){                             // sort the array using bubble sort
        for(j=i+1;j<len;j++){
            if(arr[i]>arr[j]){
                int temp=arr[i];                    //swap the elements
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        printf(" %d ",arr[i]);                     //print sorted array
    }
    printf(" \n ");
    printf("%d",arr[k-1]);                        // print smallest number according to k value
    return 0;
}
