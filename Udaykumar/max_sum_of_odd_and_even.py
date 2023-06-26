def sum_even_odd_recursive(arr, index=0, even_sum=0, odd_sum=0):
    # Recursive function to calculate the sum of even and odd numbers in the array

    # check if the length of the array is equal to the index value
    if index == len(arr):
        return even_sum, odd_sum

    # find the even number & sum it or odd number & sum it
    if arr[index] % 2 == 0:
        even_sum += arr[index]
    else:
        odd_sum += arr[index]

    return sum_even_odd_recursive(arr, index + 1, even_sum, odd_sum)


# calling sum_even_odd_recursive function
array = [1, 9, 2, 8, 5, 3, 7, 4, 9, 10]

# Calculate the sum of even and odd values in the array recursively
even_sum, odd_sum = sum_even_odd_recursive(array)

# Print the sum of even values
print("Sum of even values:", even_sum)

# Print the sum of odd values
print("Sum of odd values:", odd_sum)

# find the maximum sum of the even & odd sum
if even_sum > odd_sum:
    print("Maximum value:", even_sum)
else:
    print("Maximum value:", odd_sum)
