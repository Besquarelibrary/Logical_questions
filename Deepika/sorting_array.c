#include<stdio.h>
int main()
{
    int arr[]={1,5,16,35,10,33,2,8};                        
    int arr1[]={9,3,6,4,0,12,32};
    int len=sizeof(arr)/sizeof(arr[0]);            //size of the arr
    int len1=sizeof(arr1)/sizeof(arr1[0]);        //siz of arr1
    int totallen=len+len1;                        //total size of the two arrays
    int i,j,mergedarray[totallen];                
    for(i=0;i<len;i++){
        mergedarray[i]=arr[i];                   //copying elements of arr into mergedarray
    }
    for(i=0;i<len1;i++){
        mergedarray[len+i]=arr1[i];              //copying elements of arr1 into mergedarray from the position of size of 1st arr
    }
    
    for(int i=0;i<totallen;i++){
         printf(" %d ",mergedarray[i]);         // printing merged array
    }
    printf("\n");
    for(i=0;i<totallen;i++){                    // sorting the merged array using bubble sort
        for(j=i+1;j<totallen;j++){
            if(mergedarray[i]>mergedarray[j]){
                int temp=mergedarray[i];
                mergedarray[i]=mergedarray[j];
                mergedarray[j]=temp;
            }
        }
        printf(" %d " , mergedarray[i]);         // printing sorted array
    }
    printf(" \n ");
   
    
    printf("arr[] = : ");
    for (i = 0; i < len; i++) {                  // assigning elements back to arr according to their length
        arr[i] = mergedarray[i];
        printf("%d ", arr[i]);
    }
    printf("\n");
    

    printf("arr1[] = : ");
    for (i = 0; i < len1; i++) {                //assigning elements back to arr1 according to their length
        arr1[i] = mergedarray[len+i];
        printf("%d ", arr1[i]);
    }
    printf("\n");


    return 0;
}
