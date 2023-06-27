string = "The quick brown fox jumps over the lazy dog"
result_string = ""

# Initialize variables
length_result_string = 0

# Generate a string of lowercase alphabets using ASCII values
for order in range(97, 123):
    result_string += chr(order)
    length_result_string += 1
result_string = list(result_string)

# Print the generated alphabet string
print(result_string)
# Print the length of the generated alphabet string
print(length_result_string)

# Convert the original string to lowercase
string = string.lower()
element_count = {}
miss_element = ""

# Count the occurrences of each lowercase alphabet in the string
# and keep track of missing alphabets
for each in string:
    if ord(each) >= 97 and ord(each) <= 122:
        if each in result_string:
            element_count[each] = 1
        else:
            miss_element += each

# Print the count of each alphabet in the string
print(element_count)
# Print the missing alphabets from the generated alphabet string
print(list(miss_element))

length_element = 0

# Count the number of unique alphabets present in the string
for i in element_count:
    length_element += 1
    
print(length_element)  # Print the number of unique alphabets in the string

# Check if the number of unique alphabets is equal to the length of the generated alphabet string
# If yes, it is a pangram; otherwise, it is not a pangram
if length_element == length_result_string:
    print("Pangram")
else:
    print("Not Pangram")
