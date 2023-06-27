# sum of its values are equal to number itself.then it will be a perfect number else not a perfect number.

n = 6           
#here we assigning some value as an input
a = 0              
#initialize the variable With '0'  
for i in range( 1,n ): 
#loop over all possible factors of the number  
  if n%i == 0:          
#if number is divisible by 'i'
   a += i      
#here adding 'i' to the sum of the factors
if(a == n):   
#check if the sum of values is equal to itself number
  print("given number is a perfect number") 
#if yes print its a perfect number.
else:
  print("given number is not perfect number") #else not a perfect number.
Output: given number is perfect number
