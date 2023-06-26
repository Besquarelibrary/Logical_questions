		Find the length of the sliced array is equal to the length of the given array
		-----------------------------------------------------------------------------

import itertools

arr = [1, 6, 8, 7, 2, 4, 9]
length = len(arr)
pick_value = 2

loop = list(itertools.combinations(arr, pick_value ))

for i in loop:
    print('combination:', i)
    max_element = max(i)
    min_element = min(i)
    difference = max_element - min_element 
    result = pick_value + difference 
    if result == length:
        print('True')
    else:
        break
    print('-' * 10)
