#include<stdio.h>
int main()
{
    int number[] = {121,456,323,89798};
    int n=sizeof(number)/sizeof(number[0]);
    int max_palin=0;
    for(int i=0;i<n;i++){
        int reverse_num=0;
        int num=number[i];
        int original_num=number[i];
        while(num!=0){
            int remainder=num%10;
            reverse_num=reverse_num*10+remainder;
            num /=10;
        }
        if(original_num==reverse_num){
           if(original_num>max_palin){
               max_palin=original_num;
           }
        }
    }
    if(max_palin==0){
        printf("no palindrome found\n");
    }
    else{
        printf("maximum palindrome number is: %d\n",max_palin);
    }
    return 0;
}
