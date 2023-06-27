def find_equilibrium_number(numbers):
    """
    Finds the equilibrium number from a given list.
    """
    total_sum = sum(numbers)  # Calculate the total sum of all numbers in the list
    left_sum = 0  # Initialize the left sum as 0
    for i in range(len(numbers)):  # Iterate through each index of the list
        total_sum -= numbers[i]  # Reduce the total sum by the current number
        if left_sum == total_sum:  # If the left sum is equal to the remaining sum, we found the equilibrium number
            return numbers[i]  # Return the equilibrium number
        left_sum += numbers[i]  # Add the current number to the left sum
    return None  # No equilibrium number found

num_list = [1, 2, 3, 4, 3, 2, 1]
equilibrium = find_equilibrium_number(num_list)  # Call the find_equilibrium_number function
if equilibrium:  # If an equilibrium number is found
    print("The equilibrium number in the list", num_list, "is:", equilibrium)  # Print the equilibrium number
else:  # If no equilibrium number is found
    print("There is no equilibrium number in the list", num_list)  # Print a message indicating no equilibrium number


