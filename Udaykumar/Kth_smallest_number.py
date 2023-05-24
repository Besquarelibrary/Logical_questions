# Input List
My_List=[1, 4, 7, 8, 3, 2, 4, 6]
# To pick the number from list
K = int(input("enter a number:"))
# To eliminate duplicate values
Set = set(My_List)
# New list for without duplicate elements
New_List = []
# comparing index number with length of input list
if K <= len(Set):
    # adding set elements into list
    for ele in Set:
        New_List += [ele]
    # Iterating and comparing with given element
    for i in range(len(Set)):
        if i == K:
            print(K,"th smallest number in list:", New_List[i])
else:
    print("Enter a number less than length of list")
