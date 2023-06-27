Find the combinations based upon on pick value
----------------------------------------------

arr = [1, 8, 4, 5]
pick = 3
# taking empty list to store the combinations of given array
list_combinations = []

if pick < len(arr):
    for i in range(len(arr)- pick + 1):
        for j in range(i+1, i + pick + 2):
            for k in range(j+1, len(arr)):
                combinations = (arr[i], arr[j], arr[k])
                list_combinations.append(combinations)
    print('list_combinations:', list_combinations)
    
    # compare the length of the array & sum_value
    for combination in list_combinations:
        sum_value = pick + (max(combination) - min(combination))
        if sum_value == len(arr):
            print(combination, 'True')
    else:
        print('No Combinations')
else:
    print('Pick values is not less than length of the array')

