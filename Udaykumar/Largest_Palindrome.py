# Find the largest palindrome in given list

My_List = [121, 255, 1552, 66, 7, 1001]
New_Dict = {}

# Method-1
for ele in My_List:
    if str(ele) == str(ele)[::-1]:
        New_Dict[ele] = len(str(ele))
print(New_Dict)
for key in New_Dict:
    if New_Dict[key] == max(New_Dict.values()):
        print(key)

# Method -2
for num in My_List:
    reversed_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    if num == reversed_num:
        New_Dict[num] = len(str(num))
print(New_Dict)
for key in New_Dict:
    if New_Dict[key] == max(New_Dict.values()):
        print(key)



