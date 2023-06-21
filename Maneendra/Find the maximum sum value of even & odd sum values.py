"""
Find the maximum sum value of even sum and odd sum of the given array
"""


def sum_even_odd_recursive(arr, index=0, even=0, odd=0):
    # check if the length of the array is equal to the index value
    if index == len(arr):
        return even, odd
    
    # find the even number & sum it or odd number & sum it
    if arr[index] % 2 == 0:
        even += arr[index]
    else:
        odd += arr[index]
    
    return sum_even_odd_recursive(arr, index + 1, even, odd)


# calling sum_even_odd_recursive function
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = sum_even_odd_recursive(array)
print("Sum of even values:", even_sum)
print("Sum of odd values:", odd_sum)

# find the maximum sum of the even & odd sum
if even_sum > odd_sum:
    print("Maximum value:", even_sum)
else:
    print("Maximum value:", odd_sum)
