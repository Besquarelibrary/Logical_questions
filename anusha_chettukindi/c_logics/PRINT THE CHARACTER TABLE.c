QUESTION:PROGRAM TO PRINT THE CHARACTER TABLE
LOGIC IN C:

#include <stdio.h>
int main() {
    char s[100];
    printf("enter string\n");
    gets(s);
    int p=sizeof(s)/2;
    int table_val;
    printf("enter table you want to print");
    scanf("%d",&table_val);
    int i=1;
    while(i<p){
        int val=table_val*i;
        if(val<sizeof(s)){
            if(s[val]!=' ' && ((s[val]>=65 && s[val]<=90) || (s[val]>=97 && s[val]<=122))){
                printf("%d*%d=%c\n",table_val,i,s[val]);
                i+=1;
            }
            else{
                i+=1;
            }
        }
        else{
            break;
        }
    }
}
OUTPUT:
enter string
f*f o&l l o*w y*o u r h6e+a r&t
enter table you want to print2
2*1=f
2*2=o
2*3=l
2*4=l
2*5=o
2*6=w
2*7=y
2*8=o
2*9=u
2*10=r
2*11=h
2*12=e
2*13=a
2*14=r
2*15=t