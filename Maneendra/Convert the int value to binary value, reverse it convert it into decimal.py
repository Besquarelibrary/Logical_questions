"""
Convert the integer value to binary value, reverse it convert it into decimal
"""
number = 10
size = 8

# converting the given integer number into binary number
binary = bin(number)

# reverse the binary number
reverse = binary[-1:1:-1]

# adding the zero’s based on the length
convert = reverse + (size - len(reverse)) * '0'

# converting the binary number into decimal value
decimal = int(convert, 2)
print(dec)
