# Input list of strings
Input_List = ["vijaya", "vijayaLakshmi", "vijayavijaya", "vijji", "vij"]

# To Store the result string in s
string_Empty = ""
# To store result sub strings into list.
Result = []

# Iterating max length string which is in the list.
for ele in max(Input_List):
    # Storing result string in s
    string_Empty += ele
    # Checking the sub-string in each string
    if all(s in i for i in Input_List):
        Result += [string_Empty]

# take the max length common string from the result list.
print(max(Result), "-- Valid string")
