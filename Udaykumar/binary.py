# Prompt the user to enter a number and convert it to an integer
input_number = int(input("Enter a number:"))

# Define the maximum size of the binary number
max_size = 8

# Convert the input number to its binary representation
bin_number = bin(input_number)

# Print the binary number of the given input
print("Binary number of given number:", bin_number)

# Reverse the binary number excluding the prefix '0b'
bin_rev = bin_number[:1:-1]

# Append zeros to the reversed binary number to match the maximum size
res_bin = bin_rev + (max_size - len(bin_rev)) * '0'

# Print the reversed binary number
print("Reversed binary number:", bin_rev)

# Print the resultant binary number after adding zeros
print("Resultant binary number after adding zero's:", res_bin)

# Convert the resultant binary number back to an integer
result = int(res_bin, 2)

# Print the resultant integer number
print("Resultant integer number:", result)
