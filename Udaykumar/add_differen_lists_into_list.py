my_list_1 = [1, 2, 3, 4, 5, 11, 12]
my_list_2 = [6, 7, 8, 9, 10, 13, 14, 15, 16]
new_list = []

# Iterate over the range of the maximum length between my_list_1 and my_list_2
for i in range(max(len(my_list_1), len(my_list_2))):
    # Check if the index is within the bounds of my_list_1
    if len(my_list_1) - 1 >= i:
        # Append the element from my_list_1 at the current index to new_list
        new_list.append(my_list_1[i])
    # Check if the index is within the bounds of my_list_2
    if len(my_list_2) - 1 >= i:
        # Append the element from my_list_2 at the current index to new_list
        new_list.append(my_list_2[i])

# Print the resulting new_list
print(new_list)
