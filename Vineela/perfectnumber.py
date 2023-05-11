 # sum of its values are equal to number itself.then it will be a perfect number else not a perfect number.

input_num = 6           
#here we assigning some value as an input
result = 0              
#initialize the variable With '0'  
for i in range( 1,input_num ): 
#loop over all possible factors of the number  
  if(input_num % i == 0):          
#if number is divisible by 'i'
   result = result + i      
#here adding 'i' to the sum of the factors
if(result == input_num):   
#check if the sum of values is equal to itself number
  print("given number is a perfect number") 
#if yes print its a perfect number.
else:
  print("given number is not perfect number") #else not a perfect number.
  Output: given number is a perfect number
