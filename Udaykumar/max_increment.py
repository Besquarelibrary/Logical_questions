# Input List to find max increment value
my_list = [10, 15, 2, 3, 4, 1, 2, 3, 4, 5]

# Storing the maximum increment value
max_inc = 0
# To store the increment count value
count = 0
# Iterating the list elements using loop
for ele in range(len(my_list) - 1):
    # Comparing elements with each other
    if my_list[ele] < my_list[ele + 1]:
        count += 1
    else:
        if count > max_inc:
            max_inc = count
        count = 0
# Updating the max increment value if count is greater than max increment
if count > max_inc:
    max_inc = count

print("Max increment is:", max_inc)

