Merge the given arrays with alternate values
---------------------------------------------------------------------

first_arr = [1, 2, 3, 4, 5, 0]
second_arr = [6, 7, 8, 9 ,10]

# take an empty list to store the values alternatively
third_arr = []
length_first_arr = len(first_arr)
length_second_arr = len(second_arr)

# check the maximum length of the given two arrays & store it in max_value
if length_first_arr >= length_second_arr:
    max_value = length_first_arr
else:
    max_value = length_second_arr
    
for index in range(max_value):
    if index < length_first_arr:
        third_arr += [first_arr[index]]
    if index < length_second_arr:
        third_arr += [second_arr[index]]
print(third_arr)
