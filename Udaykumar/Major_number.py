# Input list
My_list = [2, 4, 5, 7, 1, 1, 1, 1, 1, 1, 1]

# With using in-built methods:

# Find half of the length of given list
Len_of_list = len(My_list) // 2

# Loop to iterate list elements converting list into set to eliminate unwanted iterations
for ele in set(My_list):
    # To compare count of each element with half of the length of given list
    if My_list.count(ele) > Len_of_list:
        print(ele, "Perfect number")
    else:
        print(ele, "Not a Perfect number")




# Without using in-built methods:

# Variable to store length of the given list
Total_Length = 0

# Iterating loops to find length
for ele in My_list:
    Total_Length += 1

# Find half of the length of given list
Length = Total_Length // 2

# Variable to store count of each element in list
count = 0

# Converting list into set to eliminate unwanted iterations and iterating list elements to find count of elements
for i in set(My_list):
    for j in My_list:
        if i == j:
            count += 1

    # Comparing the count of the element with half of the length of list
    if count > Len_of_list:
        print(i, "Perfect number")
    else:
        print(i, "Not a Perfect number")

    # Making count zero to use for next iterations
    count = 0

