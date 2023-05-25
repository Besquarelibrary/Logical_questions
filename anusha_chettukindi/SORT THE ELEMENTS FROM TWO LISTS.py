SORT THE ELEMENTS IN THE TWO LISTS BY TAKING THE ELEMENTS FROM THE BOTH THE LISTS
--------------------------
l1=[1,4,0,8]
l2=[3,5,2,9,6]
l3=l1+l2
for i in range(0,len(l3)):
    for j in range(i+1,len(l3)):
        if(l3[i]>l3[j]):
            l3[i],l3[j]=l3[j],l3[i]
l1=l3[0:len(l1):1]
l2=l3[len(l1)::]
print(l1,l2)

OUTPUT:
[0, 1, 2, 3] [4, 5, 6, 8, 9]
-----------------------------------------------------------------------------------
LOGIC -2
l1=[6,3,2,1,0,4]
i = 0
while i < len(l1)-1:
    if l1[i] > l1[i+1]:
        l1[i],l1[i+1]=l1[i+1],l1[i]
        if(i>0):
            i=i-1
    else:
        i += 1
            
print(l1)
OUTPUT:
[0, 1, 2, 3, 4, 6]
-----------------------------------------------------------------------------------------
LOGIC IN C
// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int a[]={1,4,6,2};
    int a1[]={5,3,8};
    int a_len=sizeof(a)/sizeof(a[0]);
    int a1_len=sizeof(a1)/sizeof(a1[0]);
    int com_len=a_len+a1_len;
    int com_arr[com_len];
    //to store first array elements in combined array
    for(int i=0;i<a_len;i++){
        com_arr[i]=a[i];
    }
    //to store second array elements in combined array
    for(int i=0;i<a1_len;i++){
        com_arr[a_len+i]=a1[i];
    }
    //sort the combined array
    int i=0;
    while(i<com_len-1){
        if(com_arr[i]>com_arr[i+1]){
            int temp=com_arr[i];
            com_arr[i]=com_arr[i+1];
            com_arr[i+1]=temp;
            if(i>0){
                i-=1;
            }
        }
        else{
            i+=1;
        }
    }
    //to store sorted array elements in to first array and second array based on length
    for (int i = 0; i < com_len; i++) {
        if (i < a_len) {
            a[i] = com_arr[i];
        } else {
            a1[i - a_len] = com_arr[i];
        }
    }
    //to print first array
    printf("first array is: ");
    for(i=0;i<a_len;i++){
        printf("%d ",a[i]);
    }
    printf("\n");
    //to print second array
    printf("second array is: ");
    for(i=0;i<a1_len;i++){
        printf("%d ",a1[i]);
    }
    
    return 0;
}
