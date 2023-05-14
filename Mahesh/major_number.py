#Find the majority number(most repeated number) in a list?

list = [1, 1, 1, 1, 2, 2, 3, 4, 1, 1]  
#given Input list to find majority number
n = len(list)  
#length of the list
max_count = 0  
#here Initialize the variable with '0'
majority_num = None  
#Initialize the variable to keep track of the number with the highest count so far
for i in list:  
#Loop through each number in the list
    count = 0  
#Initialize the count for this number to 0
    for other_num in list:  
#Loop through each number in the list again
        if i == other_num:  
#If this number is equal to the other number
            count += 1  
#Increment the count for this number
    if count > max_count:  
#If the count for this number is higher than the current highest count
        max_count = count  
#Update the highest count so far
        majority_num = i 
#Update the number with the highest count so far

if max_count > n/2:  
#If the highest count so far is greater than half the length of the list
    print("Majority Number:", majority_num)  
#Print the number with the highest count
else:
    print("No Majority Number Found")  
#Otherwise, print that no majority number was found
