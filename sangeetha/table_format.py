# to find a string in a table format
n= int(input("enter the number:"))
str=input("enter the string:")
# to find the length of the given string
for i in range(len(str)):

    count = n * i
# if the count is less than the length of the given string
    if count<len(str):
# if the string count is not equal to empty string and the ascii values in between (97 to 122) or (65 to90)
        if str[count]!="" and (ord(str[count])>=97 and ord(str[count])<=122) or (ord(str[count])>=65 and ord(str[count])<=90):
# if the statement is true
            print(n, "*", i, "=", str[count])
        else:
# count will be incremented            
            print(n, "*", i, "=", str[count+1])


