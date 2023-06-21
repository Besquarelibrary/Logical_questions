PROGRAM TO MERGE THE TWO LISTS IN TO SINGLE LIST

INPUT:l1=[1,2,3]
      l2=[4,5,6]

OUTPUT:[1,4,2,5,3,6]

EXAMPLE:

#Initialise the first list
first_list=[1,6,8,9,5]
#Initialise the second list
second_list=[2,7,3,0]
#to find the length of the resultant list
combined_length=len(first_list)+len(second_list)
#initialise the resultant list as empty
merge_list=[]
#for looping 
j=0
k=0
i=0
#loop untill its reaches the max length
while(i!=combined_length):
    #store the first list elements in the resultant list in the even positions
    if i%2==0 and i<combined_length and j<len(first_list):
        #to append the elements to resultant
        merge_list.append(first_list[j])
        #increment the first liust index
        j=j+1
        #increment the resultant list index
        i=i+1
    #else when thet index value is odd
    else:
        #this is for checking the index crossed the list lengths we should break there
        if i>=combined_length or k>=len(second_list):
            break
        #append the second list elements in the odd posiotions of the resultant
        merge_list.append(second_list[k])
        #increment the second list index
        k=k+1
        #increment the resultant list index
        i=i+1
#print the merged list
print(merge_list)

OUTPUT:
[1,2,6,7,8,3,9,0,5]
