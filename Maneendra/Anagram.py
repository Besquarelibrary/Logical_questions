def anagram(first_str, second_str):
    # Create empty dictionaries to store character frequencies for each word
    dict_first_str = {}
    dict_second_str = {}
    
    # Iterate over each character in the first word (first_str)
    for i in first_str:
        # Check if the character (i) is already present in dict_first_str
        if i in dict_first_str:
            # If it is, increment its frequency by 1
            dict_first_str[i] += 1
        else:
            # If it is not, initialize its frequency to 1
            dict_first_str[i] = 1
            
    # Iterate over each character in the second word (second_str)
    for j in second_str:
        # Check if the character (j) is already present in dict_second_str
        if j in dict_second_str:
            # If it is, increment its frequency by 1
            dict_second_str[j] += 1
        else:
            # If it is not, initialize its frequency to 1
            dict_second_str[j] = 1
    
    # Compare the two dictionaries to check if they have the same character frequencies
    return dict_first_str == dict_second_str

# Test the function by checking if 'geeksforgeeks' and 'geeksforseekg' are anagrams
ana = anagram('geeksforgeeks', 'geeksforseekg')
print(ana)
