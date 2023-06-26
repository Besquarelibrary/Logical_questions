#include<stdio.h>
int main() {
    //initialize array
    int arr[]={1,2,4,5,2,4};
    //declare variables
    int com_arr[3];
    int max,min;
    int pickcount_diff_sum;
    int max_min_diff;
    //to get array size
    int size=sizeof(arr)/sizeof(arr[0]);
    //initialize pick_count
    int pick_count=3;
    int flag=0;
    //iterate array
    for(int i=0;i<size-2;i++){
        for(int j=i+1;j<size-1;j++){
            for(int k=j+1;k<size;k++){
                //store values in the combination array
                com_arr[0]=arr[i];
                com_arr[1]=arr[j];
                com_arr[2]=arr[k];
                max=com_arr[2];
                min=com_arr[0];
                max_min_diff=max-min;
                pickcount_diff_sum=max_min_diff+pick_count;
		//to check is that sum matching with length of array
                if(pickcount_diff_sum==size){
                    flag+=1;
                    printf("max_min_diff and pickcount sum matched with length of array combination are: ");
		    //loop for printing the matched combination
                    for(int i=0;i<=2;i++){
                        printf("%d ",com_arr[i]);
                }
                    
                }
                //to empty the existed combination array to store new combination
                for(int i=0;i<=2;i++){
                    com_arr[i]=0;
                }
                printf("\n");
            }
        }
        printf("\n");
    }
    //condition for when there is no combinations exist in the array
    if(flag==0){
        printf("there is no combinations found in this array which match with length");
    }
    
}

OUTPUT:
max_min_diff and pickcount sum matched with length of array combination are: 1 2 4 


max_min_diff and pickcount sum matched with length of array combination are: 1 2 4 


max_min_diff and pickcount sum matched with length of array combination are: 1 4 4 

max_min_diff and pickcount sum matched with length of array combination are: 1 5 4 
max_min_diff and pickcount sum matched with length of array combination are: 1 2 4 

max_min_diff and pickcount sum matched with length of array combination are: 2 4 5 

