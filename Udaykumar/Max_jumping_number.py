def is_jumping_number(number):
    """
    Checks if a number is a jumping number.
    """
    number_str = str(number)  # Convert the number to a string
    for i in range(len(number_str) - 1):  # Iterate over the digits of the number
        if abs(int(number_str[i]) - int(number_str[i + 1])) != 1:  # Compare the difference between consecutive digits
            return False  # If the difference is not 1, the number is not a jumping number
    return True  # All differences are 1, so the number is a jumping number

def find_max_jumping_number(start_range, end_range):
    """
    Finds the maximum jumping number within a given range.
    """
    jumping_numbers = [num for num in range(start_range, end_range + 1) if is_jumping_number(num)]  # Generate a list of jumping numbers
    if jumping_numbers:  # If jumping numbers are found
        return max(jumping_numbers)  # Return the maximum jumping number
    else:  # If no jumping numbers are found
        return None  # Return None

start_num = 10
end_num = 100
max_jumping_number = find_max_jumping_number(start_num, end_num)  # Find the maximum jumping number in the range
if max_jumping_number:  # If a maximum jumping number is found
    print("The maximum jumping number between", start_num, "and", end_num, "is:", max_jumping_number)  # Print the maximum jumping number
else:  # If no jumping numbers are found
    print("There are no jumping numbers between", start_num, "and", end_num)  # Print a message indicating no jumping numbers are found

