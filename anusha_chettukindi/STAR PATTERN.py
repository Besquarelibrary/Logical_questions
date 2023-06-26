
QUESTION: PRINT THE STAR PATTERN 
*****
 ****
  ***
   **
    *
---------------------------------------------------------------
CODE:
    
#to read the input from user at run time number of numbers
n=int(input("enter the number of stars"))
#loop until the number rows
for i in range(0,n):
    #this is for spaces infront of stars
    for j in range(0,i+1):
        #to print space
        print(" ",end="")
    #loop to print the stars
    for k in range(1,n-i+1):
        #to print the stars
        print("*",end="")
    #for next line
    print("\n")

OUTPUT:
enter the number of stars5
    
    *****

     ****

      ***

       **

        *