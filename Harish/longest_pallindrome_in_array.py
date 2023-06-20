list=[11,121,2551552,3234,13,234334]
pallindrome_number_list=[]
for number in list:
    if str(number)==str(number)[::-1]:
        pallindrome_number_list.append(number)
print(pallindrome_number_list)
print(max(pallindrome_number_list))
