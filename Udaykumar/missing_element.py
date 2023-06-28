# Define a list of integers
Input_List = {2, 4, 9, 8, 6, 1, 3, 7}

# Loop through the range of integers from 1 to the maximum value in the list
for i in range(1, max(Input_List)):
    # Check if the integer is not in the list
    if i not in Input_List:
        # Print the integer
        print(i)

