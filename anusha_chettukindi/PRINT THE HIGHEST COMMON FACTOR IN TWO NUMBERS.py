QUESTION: PROGRAM TO PRINT THE HIGHEST COMMON FACTOR IN TWO NUMBERS
---------------------------------
CODE:
---------------------------------------------------------------
#initialize the list with two elements
input_list=[12,8]
#Create the empty list to store factors of first element
factors_element1=[]
#Create the empty list to store factors of second element
factors_element2=[]
#loop to iterate the list
for i in range(len(input_list)):
    #To store the first element  factors
    if i==0:
      #check the values upto the range of actual element(element1)
        for j in range(1,input_list[i]+1):
            #condition to check that when the element and range of numbers reminder zero
            if input_list[i]%j==0:
                #when reminder zero append to factors_element1 list
                factors_element1.append(j)
        #to print the factors of first element
        print("factors of :",input_list[i],"is",factors_element1)
    #for second element
    else:
        #check the values upto the range of actual element(element2)
        for j in range(1,input_list[i]+1):
            #condition to check that when the element and range of numbers reminder zero
            if input_list[i]%j==0:
                #when reminder zero append to factors_element2 list
                factors_element2.append(j)
        #to print the factors of second element
        print("factors of :",input_list[i],"is",factors_element2)
#to check the highest common factor iterate from the last as it is arranged in asscending order 
i=len(factors_element1)-1
#this is for whenever no common factors found in the factors list
flag=0
#loop until list first element(minimum)
while(i>0):
    #condition to check every highest factor in first list should exist in the second factors list
    if factors_element1[i] in factors_element2:
        flag=1
        #when that factor exists in both the factors lists then that is highest common factor so print that value
        print("Highest common factor is :",factors_element1[i])
        #as we need highest common factor so it is one so break the loop
        break
    #when that index element not exist in second factors list decrement the inde to to move to next largest element
    else:
        i=i-1
#when the no factors exist that means there is no change in flag value 
if flag==0:
  #print the statement whenever the absence of common factors
  print("there is no common factors")
-------------------------------------------------------------------

OUTPUT:
factors of : 12 is [1, 2, 3, 4, 6, 12]
factors of : 8 is [1, 2, 4, 8]
Highest common factor is : 4