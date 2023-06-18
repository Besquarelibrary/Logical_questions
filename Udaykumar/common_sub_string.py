# To find common string from  given list of strings

# Input list of strings
My_List = ["uday", "udaykumar", "udaykumar amalakanti", "uday402", "ud"]

# To Store the resultant string in s
s = ""
# To store resultant sub strings into list.
Result = []

# Iterating max length string which is in the list.
for ele in max(My_List):
    # Storing resultant string in s
    s += ele
    # Checking availability of sub-string in each string
    if all(s in i for i in My_List):
        # Storing available sub-string into Result list
        Result += [s]

# Pick the max length common string from the result list.
print(max(Result), "-- Valid string")

