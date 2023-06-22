# Find the combinations of the given list and pickup number is "3"
lst = [2, 4, 6, 8, 3]
# to find the range of the given list
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            list1 = [lst[i], lst[j], lst[k]]
            # To find the max value and it is stored in "n"
            n = max(list1)
            # To find the min value and it is stored in "m"
            m = min(list1)
            # "n" and "m" values are stored in "s"
            s = n-m+3
            # If the length of the given list is equal to "s"
            if len(lst) == s:
                print(list1, s)
