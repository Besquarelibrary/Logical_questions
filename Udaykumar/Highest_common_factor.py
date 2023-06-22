num_1 = int(input("Enter a number:"))  # Prompting the user to enter a number and converting it to an integer.

num_2 = int(input("Enter a number:"))  # Prompting the user to enter another number and converting it to an integer.

list_1 = []  # Initializing an empty list to store even numbers from the range.

list_2 = []  # Initializing another empty list to store even numbers from the second range.

for i in range(2, num_1):  # Looping through the range from 2 to the first input number (exclusive).
    if i % 2 == 0:  # Checking if the current number is even.
        list_1.append(i)  # Adding the even number to list_1.

for i in range(2, num_2):  # Looping through the range from 2 to the second input number (exclusive).
    if i % 2 == 0:  # Checking if the current number is even.
        list_2.append(i)  # Adding the even number to list_2.

new_list = list_1 + list_2  # Combining both lists to create a new list containing all even numbers from both ranges.

max_common_factor = 0  # Initializing a variable to store the maximum common factor.

for ele in new_list:  # Looping through each element in the new list.
    if ele in list_1 and list_2:  # Checking if the current element is present in both list_1 and list_2.
        if max_common_factor < ele:  # Checking if the current element is greater than the current maximum common factor.
            max_common_factor = ele  # Updating the maximum common factor with the current element.

print(list_1, list_2)  # Printing the contents of list_1 and list_2 (even numbers from the respective ranges).
print(max_common_factor)  # Printing the maximum common factor found among the even numbers.

