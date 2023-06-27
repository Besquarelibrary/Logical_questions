"""
Find the H.C.F of the given numbers
"""

def high_common_factor(first_num, second_num):
    result_first_num = []
    result_second_num = []
    final_result = []
    
    # find the maximum value of "first_num" & "second_num"
    max_value = max(first_num, second_num)
    
    # find factors of "first_num" & "second_num"
    for value in range(1, max_value + 1):
        if first_num%value == 0:
            # store the values in "result_first_num"
            result_first_num += [value]
        if second_num%value == 0:
            # store the values in "result_second_num"
            result_second_num += [value]
    
    # get the common highest factors
    for num in result_first_num:
        if num in result_second_num:
            final_result += [num]
    # return "final_result"
    return final_result


# calling "high_common_factor" function
H_C_F = high_common_factor(300, 1000)
print(H_C_F)
