#include<stdio.h>
int main(){
    int num[]={1,1,2,6,6,6,6,6,6,6,8,9,7,3};
    int i,count,n,max_count,major_num;
    n=sizeof(num)/sizeof(num[0]);      //size of the array 
    for(i=0;i<n;i++){
        for(int j=i+1;j<n;j++){       // checking the number with their index to other indices 
            if(num[i]==num[j]){       //checking the number is matching with other index number
                count++;              //if the above condition true incrementing count
            }
        }
        if(count>max_count){         //If the current count is greater than the previous maximum count, update the maximum count
            max_count=count;      
            major_num=num[i];       //considering major number which is repeated more
        }
    }
    if(max_count>n/2){              // if maximum count is greter than half of the size of array print major number
        printf("majority number: %d",major_num);
    }
    else{
        printf("there is no major number");
    }
    return 0;
}
