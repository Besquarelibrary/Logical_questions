find the given arr longest common prefix in array?
arr = ["greeksforgreeks", "greeks", "greek", "greezes"]

# Find the length of the shortest string in the array
min_length = len(arr[0])
for string in arr:
    if len(string) < min_length:
        min_length = len(string)

# Iterate over each character position
common_prefix = ""
for i in range(min_length):
    char = arr[0][i]  # Take the character from the first string
    mismatch = False  # Flag to check for character mismatch

    # Check if the character matches in all other strings
    for j in range(1, len(arr)):
        if arr[j][i] != char:
            mismatch = True
            break

    if mismatch:
        break
    else:
        common_prefix += char

print("Longest common prefix:", common_prefix)

output:gree
