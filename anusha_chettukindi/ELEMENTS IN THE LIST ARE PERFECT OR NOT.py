PROGRAM TO PRINT THE WHETHER THE ELEMENTS IN THE LIST ARE PERFECT OR NOT

DEscription: A number is said to be perfect when the sum of the factors of the number should equal to the actual number

PROGRAM:

#create the list
l=[7,28,1,12,6,2]
#create the function for finding the perfect number 
def perfect_num(n):
    #To store sum of the factors of that number
    sum=0
    #range upto half of the length of list because the factor of any number should not exist after a mid
    for i in range(1,(n//2)+1):
        #condition for perfect square
        if(n%i==0):
            sum=sum+i
    #check whether factors sum of that that number is equal to the actual number
    if(sum==n):
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
#loop for iterating the every element in the list
for i in l:
    #function call to check every element is perfect or not
    perfect_num(i);

OUTPUT:
7 is not a perfect number
28 is a perfect number
1 is not a perfect number
12 is not a perfect number
6 is a perfect number
2 is not a perfect number