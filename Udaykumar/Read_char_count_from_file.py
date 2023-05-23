# To find chars count in a file

# To store the count value
Count = 0

# To store each char count in dict
My_dict = {}
# Reading the data from file
with open("text.txt", "r")as Read:
    # Store the red data into a var for iterating purpose
    Data = Read.read()
    # Iterating the data from object
    for i in Data:
        for j in Data:
            # Comparing each char
            if i == j:
                # Count calculation
                Count +=1
        # Storing char count into dict
        My_dict[i] = Count
        # Again making count 0 for next iteration
        Count = 0
print(My_dict)
