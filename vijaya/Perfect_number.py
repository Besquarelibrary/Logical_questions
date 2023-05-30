num = int(input("enter a number:"))  # Enter a number to find whether it is perfect number or not
My_List = []  # Empty list to store the div numbers
total = 0


# 1st method
 # loop to find div numbers
for i in range(1, num // 2 + 1):
    # dividing num with lower range  numbers
    if num % i == 0: 
         # adding using append method div numbers into list
        My_List.append(i)
 # checking num whether it is perfect number or not
if sum(My_List) == num: 
    print(num, "Is a perfect number")
else:
    print(num, "Not a perfect number")


#Method 2
 # loop to find div numbers
for i in range(1, num // 2 + 1):
    if num % i == 0:
        My_List += [i]  # adding div numbers into list by list addition

for ele in My_List: # Loop to add list of elements
    total += ele
if total == num:  # checking num whether it is perfect number or not
    print(num, "Is a perfect number")
else:
    print(num, "Not a perfect number")
