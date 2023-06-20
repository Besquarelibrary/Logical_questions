PRINT THE ODD AND EVEN INDEX SUM IN THE LIST USING RECURSION

l=[1,3,4,4,6]
i=0
even_sum=0
odd_sum=0
#for returning the even index elements 
def even(i,even_sum,l):
    #for checking the even index 
    if i%2==0 and i<len(l):
        #adding the value to sum
        even_sum=even_sum+l[i]
        #for adding next even value 
        return even(i+1,even_sum,l)
    #for checking if it is odd
    elif i%2!=0:
        #for calling the function when it is odd 
        return even(i+1,even_sum,l)
    #when that exceeds the length 
    else:
        return even_sum
#calling for printing the even sum
print("even sum is:", even(i,even_sum,l))
#for returning the odd index elements
def odd(i,odd_sum,l):
    #checking for odd indexes
    if i%2!=0 and i!=len(l):
        #add the elements to odd sum when that index is odd
        odd_sum=odd_sum+l[i]
        #for caling the odd sum function for storing next odd value
        return odd(i+1,odd_sum,l)
    #checking for even if it is even don't add it to odd sum but call the function to check for next index 
    elif i%2==0:
        #calling functn when it is even
        return odd(i+1,odd_sum,l)
    #when index exceeds the length
    else:
        #to return the resultant odd_sum
        return odd_sum
##calling for printing the odd sum
print("odd sum is:", odd(i,odd_sum,l))


OUTPUT:
even sum is: 11
odd sum is: 7