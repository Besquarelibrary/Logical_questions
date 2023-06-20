REVERSE THE BITS IN A BYTE
INPUT:INTEGER 10(1010)
OUTPUT: 5(0101)

#read the input number
input_integer=int(input("enter integer"))
#to store the binary of integer
empty_string=""
#to store the binary of integer
while(input_integer!=0):
    #to get the reminder of the integer
    reminder=input_integer%2
    #append that binary digits to resultant
    empty_string=empty_string+str(reminder)
    #again taking coefficient and store it in the integer
    input_integer=input_integer//2
i=0
resultant_integer=0
#for reading digits of binary in reverse
j=len(empty_string)-1
#loop for getting the decimal of reversed binary number 
while(i<len(empty_string)):
    #for doing 001=1*pow(2,0)(binary to decimal conversion)
    resultant_integer=resultant_integer+int(empty_string[j])*(2**i)
    i+=1
    j-=1
#for storing resultant decimal value
print(resultant_integer)

OUTPUT:
enter integer10
5
