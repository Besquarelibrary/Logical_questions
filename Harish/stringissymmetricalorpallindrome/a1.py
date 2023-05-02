string = 'geeksoskeeg'
if len(string)%2!=0:
    half=len(string)//2+1
    first_str = string[:half]
    second_str = string[half-1:]
else:
    half = int(len(string) / 2)
    print(half)
    first_str = string[:half]
    second_str = string[half:]


if first_str == second_str:
    print('string is symmetrical')
else:
    print('string is not symmetrical')

# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')