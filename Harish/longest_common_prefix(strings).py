def longest_common_prefix(strings):
    if not strings or len(strings) == 0:
        return ""

    strings.sort()
    print(strings)
    
    prefix = ""

    for i in range(len(strings[0])):
        if strings[0][i] == strings[-1][i]:
            prefix += strings[0][i]
        else:
            return prefix

    return prefix
    
    
    
strs=['geeksforgeeks','geeks','geek','geezer']
print(longest_common_prefix(strs))
