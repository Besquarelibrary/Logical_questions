num = int(input("enter a number:"))  # Enter a number to find whether it is perfect number or not
My_List = []  # Empty list to store the div numbers

# Method -- 1
for i in range(1, num // 2 + 1):  # loop to find div numbers
    if num % i == 0:  # dividing num with lower range  numbers
        My_List.append(i)  # adding using append method div numbers into list

if sum(My_List) == num:  # checking num whether it is perfect number or not
    print(num, "Is a perfect number")
else:
    print(num, "Not a perfect number")


# Method -- 2
for i in range(1, num // 2 + 1):  # loop to find div numbers
    if num % i == 0:  # dividing num with lower range  numbers
        My_List += [i]  # adding div numbers into list by list addition

if sum(My_List) == num:  # checking num whether it is perfect number or not
    print(num, "Is a perfect number")
else:
    print(num, "Not a perfect number")


