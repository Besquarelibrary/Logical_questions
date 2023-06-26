			Find the kth smallest element in the given array
			------------------------------------------------

array = [1, 2, 3, 4, 5, 6, 7, 2, 3, 5, 6, 8, 7]
key = 3
sort_list = []
dict_1 = {}

for i in array:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1
print(dict_1)

count = [0] * len(l1)

for i in dict_1:
    count[i] += 1
print(i, count)
print(len(count))

for j in range(0, len(count)):
    sort_list += [j] * count[j]
print(sort_list)

print(sort_list[key-1])
