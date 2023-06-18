# Taking Array
array=[22,31,23,22,21,34,54,56,76]
# user input for kth number to get kth smallest element from array
k=int(input("Enter kth number for kth smallest element in array: "))
# using inbuilt sort method for sorting array
array.sort()
# comparing "kth" number is lees than equal to length of array
if k<=len(array):
    print(k,"smallest element in array",array[k])
else:
    print("Please enter less than a number length of array")