first_array = [0, 3, 5, 4, 6]
second_array = [2, 7, 1, 8, 4, 9]
third_array = first_array + second_array
print("Concat_array:", third_array)

# Initilize the array size of the count
count = [0] * len(third_array)
sort_array = []

# Count the occurrences of each element in the third_array
for each in third_array:
    count[each] += 1
    print(each, count)

# Create a sorted array based on the counts of each element
for line in range(len(count)):
    sort_array += [line] * count[line]
print("sorted_array:", sort_array)

# Update first_array with sorted elements from sort_array
first_array = sort_array[:len(first_array)]
print(first_array)

# Update second_array with sorted elements from sort_array
second_array = sort_array[len(first_array):]
print(second_array)
