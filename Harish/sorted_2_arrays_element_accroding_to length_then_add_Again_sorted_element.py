list_1=[1,2,4,3,6]
list_2=[6,7,5,4,8,9,6]
list_1_length=len(list_1)
list_2_length=len(list_2)
list_3=list_1+list_2
list_3.sort()
list_4_sorted_according_to_list_1=list_3[0:len(list_1)]
list_5_sorted_according_to_list_2=list_3[len(list_1):]
print(list_4_sorted_according_to_list_1)
print(list_5_sorted_according_to_list_2)

    