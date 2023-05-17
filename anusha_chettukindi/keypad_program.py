QUESTION:
WRITE THE PROGRAM FOR KEYPAD WHICH WHEN USER WANTS TO SEND A MESSAGE WHAT DIGITS NEED TO BE SELECTED ON THE KEYPAD

PROGRAM IN C:

keypad = {
    "abc": "222",
    "def": "333",
    "ghi": "444",
    "jkl": "555",
    "mno": "666",
    "pqrs": "7777",
    "tuv": "888",
    "wxyz": "9999"
}
#read the input string from user
string=input("enter string")
#empty string to store the numeric value of every character
new_str=""
#iterate string
for chr in string:
    #read key and value from dict items
    for key,value in keypad.items():
        #iterate every key in dict
        for ele in range(len(key)):
            #check char exist in the key
            if chr==key[ele]:
                #add the digit value which belongs to character in string 
                new_str=new_str+value[0:ele+1:1]
#print the resultant string with digits
print(new_str)

OUTPUT:
enter string anusha
anusha
266887777442
-------------------------------------------------------------------------------------------------------------
LOGIC-2 IN PYTHON
#input string read from user
string=input("enter string")
#list of digits on keypad
keypad_digits=['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999']
alp=[]
#creation of alphabates list
for i in range(97,123):
    alp=alp+[chr(i)]
#to store string of digits
resultant_digits=""
#iterate the string
for i in range(0,len(string)):
    #iterate the alphabates
    for j in range(0,len(alp)):
        #condition to check the presence of char in alphabates
        if(string[i]==alp[j]):
           resultant_digits=resultant_digits+keypad_digits[j]
print(resultant_digits)
OUTPUT:
enter string anusha
anusha
266887777442

--------------------------------------------------------------------------------------------------------------------------------------
LOGIC IN C:
#include <stdio.h>

int main() {
    char char_array[26];
    int res_digit[10];
    //store input string 
    char input[]="anusha";
    //for creating alphabates array
    for(int i=0; i<26; i++){
        char_array[i] = 'a' + i;
    }
    //initialize array with keypad digits
    int digit_array[26]={2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999};
    //to create the new digit array
    int g=0;
    //iterate characters in an input string
    for(int i=0;input[i]!='\0';i++){
        //iterate digits array
        for(int j=0;j<26;j++){
            //comparing character in the list of alphabates array
            if(input[i]==char_array[j]){
                //store that character digit value in the new array
                res_digit[g]=digit_array[j];
                g+=1;
            }
        }
    
    }
    for(int i=0;i<g;i++){
        printf("%d",res_digit[i]);
    }
    
}
OUTPUT:
266887777442
