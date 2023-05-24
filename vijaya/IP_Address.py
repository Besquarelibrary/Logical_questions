# To validate the Ip address
ip_address = "255.234.0.1"
empty_list = []
empty_string = ""
#  to find the dot in a string
for i in ip_address:
    if i == ".":
        # if the above condition is true then append to empty_list
        empty_list.append(empty_string)
        # Refreshing the empty_string
        empty_string = ""
        print(empty_list)
    else:
        # If i != "." ,then store the "i" in empty_string.
        empty_string = empty_string + i
        print(empty_string)
# to the last value of the empty_string , we are appending to empty_list
empty_list.append(empty_string)
print(empty_list)
# To store the values if the given condition is true.
count = 0
# to find the length
length = 0
# We have sperated each value and stored it in a list
for i in empty_list:
    # To find length we are incrementing.
    length = length + 1
    # To get the values which are in between 0 - 255
    if int(i) >=0 and int(i) <= 255:
        # If the above condition is true then, we are incrementing count.
        count += 1
print(count)
# If both length and count are equal then only the given IP address is Valid.
if count == length :
    print("Valid IP address")
else:
    print("Invalid IP address")
